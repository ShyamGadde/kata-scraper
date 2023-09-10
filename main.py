"""
This script is a program for scraping completed katas from Codewars, organizing them
into folders and files, and generating an index file. It utilizes Selenium and aiohttp
libraries for web scraping and asynchronous file operations.
"""

import asyncio
import os
import sys
from collections import defaultdict

import aiofiles
from aiohttp import ClientSession
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


async def read_file_content_async(file_path) -> str:
    """
    This is an asynchronous function that reads the content of a file and returns it.

    Args:
    file_path: The file path parameter is a string that specifies the location of the
    file to be read. It can be an absolute or relative path to the file.

    Returns:
    The function `read_file_content` returns the content of the file located at
    `file_path` as a string. The content is read asynchronously using the `aiofiles`
    library.
    """
    async with aiofiles.open(file_path, "r", encoding="utf-8") as file:
        return await file.read()


async def write_file_content_async(file_path, content) -> None:
    """
    This is an asynchronous Python function that writes content to a file at a
    specified file path.

    Args:
    - file_path: The file path is a string that specifies the location and name of the
    file that you want to write to. It should include the file extension
    (e.g. ".txt", ".csv", etc.) and the full path if the file is not in the current
    working directory.
    - content: The content parameter is a string that represents the text content that
    will be written to the file.
    """
    async with aiofiles.open(file_path, "w", encoding="utf-8") as file:
        await file.write(content)


class CodeWarsKataScrapper:
    """
    A class that represents a scrapper for retrieving completed katas from Codewars.

    This class scrapes completed katas from the user's Codewars profile, organizes them
    into folders and files, and generates an index file categorizing the completed
    katas. It uses Selenium for web scraping and aiohttp for asynchronous HTTP requests
    and file operations.

    Attributes:
        - language_extensions (dict): A dictionary mapping programming languages to
        their file extensions
        - kata_categories (dict): A dictionary mapping category names to lists of katas
        belonging to those categories
        - options (Options): Options for configuring the headless browser
        - browser (WebDriver): The web driver instance for interacting with the web
        browser
        - completed_katas_url (str): The URL for retrieving completed katas from the
        Codewars API
        - kata_info_url (str): The base URL for retrieving information about a specific
        kata from the Codewars API
        - main_folder_path (str): The path to the main folder where the katas will be
        organized
        - total_completed_katas (int): The total number of completed katas
        - counter (int): A counter for tracking the progress of kata processing
        - error_list (list): A list for storing any errors encountered during processing
    """

    def __init__(self) -> None:
        self.language_extensions = {
            "agda": "agda",
            "bf": "b",
            "c": "c",
            "cmlf": "cmfl",
            "clojure": "clj",
            "cobol": "cob",
            "coffeescript": "coffee",
            "commonlisp": "lisp",
            "coq": "coq",
            "cplusplus": "cpp",
            "crystal": "cr",
            "csharp": "cs",
            "dart": "dart",
            "elixir": "ex",
            "elm": "elm",
            "erlang": "erl",
            "factor": "factor",
            "forth": "fth",
            "fortran": "f",
            "fsharp": "fs",
            "go": "go",
            "groovy": "groovy",
            "haskell": "hs",
            "haxe": "hx",
            "idris": "idr",
            "java": "java",
            "javascript": "js",
            "julia": "jl",
            "kotlin": "kt",
            "lean": "lean",
            "lua": "lua",
            "nasm": "nasm",
            "nimrod": "nim",
            "objective": "m",
            "ocaml": "ml",
            "pascal": "pas",
            "perl": "pl",
            "php": "php",
            "powershell": "ps1",
            "prolog": "pro",
            "purescript": "purs",
            "python": "py",
            "r": "r",
            "racket": "rkt",
            "ruby": "rb",
            "rust": "rs",
            "scala": "scala",
            "shell": "sh",
            "sql": "sql",
            "swift": "swift",
            "typescript": "ts",
            "vb": "vb",
        }
        self.language_icons = {
            "python": "python/python-original.svg",
            "javascript": "javascript/javascript-original.svg",
        }
        self.kata_categories: dict[str, dict[str, list[dict[str, str]]]] = {}
        for category in [
            "reference",  # Equivalent to the "Fundamentals" category
            "algorithms",
            "bug_fixes",
            "refactoring",
            "games",  # Equivalent to the "Puzzles" category
        ]:
            self.kata_categories[category] = defaultdict(list)

        self.options = Options()
        self.options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.implicitly_wait(0.5)

        self.completed_katas_url = (
            f"https://www.codewars.com/api/v1/users/{self.get_credentials('username')}/"
            "code-challenges/completed"
        )
        self.kata_info_url: str = "https://www.codewars.com/api/v1/code-challenges/"
        self.main_folder_path: str = "./katas"
        self.total_completed_katas: int = 0
        self.counter: int = 0
        self.error_list: list[str] = []

    async def main(self) -> None:
        """
        This is an async function that scrapes completed katas from Codewars, creates
        folders and files for each kata, and generates an index file.
        """

        self.sign_in_to_codewars(
            self.browser,
            self.get_credentials("email"),
            self.get_credentials("password"),
        )

        os.makedirs(self.main_folder_path, exist_ok=True)

        async with ClientSession() as session:
            response = await session.get(self.completed_katas_url)
            response_content: dict = await response.json()
            self.total_completed_katas: int = response_content["totalItems"]
            number_of_pages: int = response_content["totalPages"]

            tasks = []

            for page in range(number_of_pages):
                response = await session.get(f"{self.completed_katas_url}?page={page}")
                response_content: dict = await response.json()
                completed_katas: list[dict] = response_content["data"]

                for kata in completed_katas:
                    response = await session.get(f"{self.kata_info_url}{kata['id']}")
                    kata_details: dict = await response.json()
                    await asyncio.sleep(0.5)

                    kata_folder_path: str = os.path.join(
                        self.main_folder_path, kata["slug"]
                    )

                    kata_object = {
                        "id": kata["id"],
                        "name": kata["name"],
                        "link": f'./katas/{kata["slug"]}',
                        "completed_languages": kata["completedLanguages"],
                        "tags": kata_details["tags"],
                    }

                    self.kata_categories[kata_details["category"]][
                        kata_details["rank"]["name"]
                    ].append(kata_object)

                    self.counter += 1
                    print(
                        f"\rProcessing kata {self.counter} "
                        f"of {self.total_completed_katas}...",
                        end="",
                    )

                    os.makedirs(kata_folder_path, exist_ok=True)

                    tasks.append(
                        asyncio.create_task(
                            self.create_problem_description_file(
                                kata_folder_path, kata, kata_details
                            )
                        )
                    )

                    tasks.extend(
                        asyncio.create_task(
                            self.create_solution_file(kata_folder_path, kata, language)
                        )
                        for language in kata["completedLanguages"]
                    )
            await asyncio.gather(*tasks)

        await self.create_index_file()
        print("\nDone.")

        if self.error_list:
            print("\nErrors:")
            print("\n".join(self.error_list))

        self.browser.quit()

    def get_credentials(self, key: str) -> str:
        """
        This function retrieves the credentials for a specific key from the environment
        variables.

        Args:
        key (str): The key parameter is a string that specifies which credential to
        retrieve. It can be one of three values: "username", "email", or "password".

        Returns:
        a string that corresponds to the value of the environment variable associated
        with the input key. If the key is "username", the function returns the value of
        the environment variable "CODEWARS_USERNAME". If the key is "email", the
        function returns the value of the environment variable "CODEWARS_EMAIL".
        If the key is "password", the function returns the value of the environment
        variable
        """
        load_dotenv()
        if key == "username":
            return os.getenv("CODEWARS_USERNAME")
        if key == "email":
            return os.getenv("CODEWARS_EMAIL")
        if key == "password":
            return os.getenv("CODEWARS_PASSWORD")

    def sign_in_to_codewars(
        self, driver: WebDriver, codewars_email: str, codewars_password: str
    ) -> None:
        """
        This function signs in to Codewars using a given email and password through a
        web driver.

        Args:
        - driver (WebDriver): WebDriver is an object that controls the web browser and
        allows the script to interact with it.
        - codewars_email (str): The email address associated with the Codewars account
        that you want to sign in to.
        - codewars_password (str): The password for the Codewars account that the user
        wants to sign in to.
        """
        try:
            driver.get("https://www.codewars.com/users/sign_in")
        except TimeoutError:
            print("The driver took too much time to sign in.")
            sys.exit(1)

        try:
            sign_in_form: WebElement = driver.find_element(By.ID, "new_user")
            driver.find_element(By.ID, "user_email").send_keys(codewars_email)
            driver.find_element(By.ID, "user_password").send_keys(codewars_password)
            sign_in_form.find_element(
                By.CSS_SELECTOR, 'button.is-red[type="submit"]'
            ).click()
            print("Signed in successfully.")
        except NoSuchElementException:
            print("A web element was not found on the page (sign-in step).")
            sys.exit(1)

    async def create_problem_description_file(
        self, kata_folder_path, kata, kata_details
    ) -> None:
        """
        This function creates a README.md file in a specified folder path with
        information about a coding problem.

        Args:
        - kata_folder_path: The path to the folder where the README.md file will be
        created or updated.
        - kata: A dictionary containing information about a specific CodeWars kata,
        including its name, ID, completion date, and completed languages.
        - kata_details: The `kata_details` parameter is a dictionary containing details
        about a specific coding challenge or kata, such as its description, tags,
        and rank.
        """
        file_path: str = os.path.join(kata_folder_path, "README.md")
        content: str = (
            f"# [{kata['name']}]({kata_details['url']})\n\n"
            f"- **Completed at:** {kata['completedAt']}\n\n"
            f"- **Completed languages:** {', '.join(kata['completedLanguages'])}\n\n"
            f"- **Tags:** {', '.join(kata_details['tags'])}\n\n"
            f"- **Rank:** {kata_details['rank']['name']}\n\n"
            f"## Description\n\n{kata_details['description']}"
        )

        try:
            if not os.path.exists(
                file_path
            ) or content != await read_file_content_async(file_path):
                await write_file_content_async(file_path, content)
        except OSError:
            self.error_list.append(
                f"An error occurred while creating the problem description \
                    file of {kata['name']}."
            )

    async def create_solution_file(self, kata_folder_path, kata, language) -> None:
        """
        This function creates a solution file for a given kata and language by scraping
        the code from the newest solution on the kata's Codewars page.

        Args:
        - kata_folder_path: The path to the folder where the solution file will be
        created.
        - kata: The kata parameter is a dictionary containing information about a
        specific coding challenge on Codewars, such as its ID, name, and description.
        - language: The programming language of the solution file to be created.
        """
        try:
            self.browser.get(
                f"https://www.codewars.com/kata/{kata['id']}/solutions/{language}/me/newest"
            )

            solutions_list = self.browser.find_element(By.ID, "solutions_list")
            solution_item = solutions_list.find_element(By.TAG_NAME, "div")
            solution_code: str = solution_item.find_element(By.TAG_NAME, "pre").text

            file_path: str = os.path.join(
                kata_folder_path, f"solution.{self.language_extensions[language]}"
            )

            if not os.path.exists(
                file_path
            ) or solution_code != await read_file_content_async(file_path):
                await write_file_content_async(file_path, solution_code)
        except TimeoutError:
            self.error_list.append(
                f"The driver took too much time for {kata['name']} ({language}). \
                    Skipping..."
            )
        except NoSuchElementException:
            self.error_list.append(
                f"Couldn't find the solution for {kata['name']} ({language}) "
                "on CodeWars. Failed to create solution file. Skipping..."
            )
        except OSError:
            self.error_list.append(
                "An error occurred while creating the solution file for "
                f"{kata['name']} ({language})."
            )

    async def create_index_file(self) -> None:
        """
        This function creates an index file with a list of completed code challenges
        sorted by category.
        """
        file_path: str = "./README.md"

        for category in self.kata_categories.values():
            for rank in category.values():
                rank.sort(key=lambda s: s["name"].lower())

        content: str = (
            "# KataVault\n\n"
            f"These are the {self.total_completed_katas} code challenges I have "
            "completed sorted by category and kyu:"
        )

        for category_name, category in self.kata_categories.items():
            if not category:
                continue

            if category_name == "reference":
                category_name = "fundamentals"
            elif category_name == "games":
                category_name = "puzzles"

            content += f"\n\n## {category_name.capitalize().replace('_', ' ')}\n\n"

            for rank, problems in category.items():
                problems.sort(key=lambda s: s["name"].lower())

                content += f"\n### {rank}\n\n"
                content += "| Kata | Languages | Tags |\n"
                content += "| ---- | --------- | :----: |\n"

                for problem in problems:
                    problem["completed_languages"] = map(
                        lambda s: '[<img height="15px" style="vertical-align: middle" '
                        'src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/'
                        f'{self.language_icons[s]}" />]'
                        f'({problem["link"]}/solution.{self.language_extensions[s]})',
                        problem["completed_languages"],
                    )

                    content += (
                        f"| [{problem['name']}]({problem['link']}) "
                        f"| {' '.join(problem['completed_languages'])} "
                        f"| {', '.join(problem['tags'])} |\n"
                    )

        try:
            if not os.path.exists(
                file_path
            ) or content != await read_file_content_async(file_path):
                await write_file_content_async(file_path, content)
        except OSError:
            self.error_list.append("There was a problem while creating the index file.")


if __name__ == "__main__":
    codewars_kata_scrapper = CodeWarsKataScrapper()
    asyncio.run(codewars_kata_scrapper.main())
