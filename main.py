# pylint: disable=missing-module-docstring
import asyncio
import os
import sys

import aiofiles
import aiohttp
import dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


async def read_file_content(file_path):
    """
    This is an asynchronous function that reads the content of a file and returns it.

    Args:
    file_path: The file path parameter is a string that specifies the location of the file to be
    read. It can be an absolute or relative path to the file.

    Returns:
    The function `read_file_content` returns the content of the file located at `file_path` as a
    string. The content is read asynchronously using the `aiofiles` library.
    """
    async with aiofiles.open(file_path, "r", encoding="utf-8") as file:
        return await file.read()


async def write_file_content(file_path, content):
    """
    This is an asynchronous Python function that writes content to a file at a specified file path.

    Args:
    - file_path: The file path is a string that specifies the location and name of the file that you
    want to write to. It should include the file extension (e.g. ".txt", ".csv", etc.) and the
    full path if the file is not in the current working directory.
    - content: The content parameter is a string that represents the text content that will be
    written to the file.
    """
    async with aiofiles.open(file_path, "w", encoding="utf-8") as file:
        await file.write(content)


class CodewarsLogger:
    """ "..."""

    def __init__(self):
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
        self.kata_categories = {
            "reference": [],  # Equivalent to the "Fundamentals" category
            "algorithms": [],
            "bug_fixes": [],
            "refactoring": [],
            "games": [],  # Equivalent to the "Puzzles" category
        }

        self.options = Options()
        self.options.add_argument("--headless")
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.implicitly_wait(0.5)

        self.username, self.email, self.password = self.get_credentials()

        self.completed_katas_url = (
            f"https://www.codewars.com/api/v1/users/{self.username}/"
            "code-challenges/completed"
        )
        self.kata_info_url = "https://www.codewars.com/api/v1/code-challenges/"
        self.main_folder_path = "./katas"
        self.total_completed_katas = 0
        self.counter = 0

        self.error_list = []

    async def main(self):
        """
        This is an async function that scrapes completed katas from Codewars, creates folders and
        files for each kata, and generates an index file.
        """

        self.sign_in_to_codewars(self.browser, self.email, self.password)

        os.makedirs(self.main_folder_path, exist_ok=True)

        async with aiohttp.ClientSession() as client:
            response = await client.get(self.completed_katas_url)
            response_json = await response.json()
            self.total_completed_katas = response_json["totalItems"]
            number_of_pages = response_json["totalPages"]

            tasks = []

            for page in range(number_of_pages):
                response = await client.get(f"{self.completed_katas_url}?page={page}")
                response_json = await response.json()
                completed_katas = response_json["data"]

                for kata in completed_katas:
                    response = await client.get(f"{self.kata_info_url}{kata['id']}")
                    kata_details = await response.json()

                    kata_folder_path = os.path.join(self.main_folder_path, kata["slug"])

                    self.kata_categories[kata_details["category"]].append(
                        f'- [{kata["name"]}](./katas/{kata["slug"]})'
                    )

                    self.counter += 1
                    print(
                        f"\rDownloading kata {self.counter} of {self.total_completed_katas}...",
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

                    for language in kata["completedLanguages"]:
                        tasks.append(
                            asyncio.create_task(
                                self.create_solution_file(
                                    kata_folder_path, kata, language
                                )
                            )
                        )

            await asyncio.gather(*tasks)

        await self.create_index_file()
        print("\nDone.")

        print("\nErrors:")
        print("\n".join(self.error_list))

        self.browser.quit()

    def get_credentials(self):
        """
        This function loads environment variables and returns a tuple of Codewars credentials.

        Returns:
        A tuple containing the values of the environment variables "CODEWARS_USERNAME",
        "CODEWARS_EMAIL", and "CODEWARS_PASSWORD".
        """
        dotenv.load_dotenv()
        return (
            os.getenv("CODEWARS_USERNAME"),
            os.getenv("CODEWARS_EMAIL"),
            os.getenv("CODEWARS_PASSWORD"),
        )

    def sign_in_to_codewars(
        self, driver: WebDriver, codewars_email: str, codewars_password: str
    ):
        """
        This function signs in to Codewars using a given email and password through a web driver.

        Args:
        - driver (WebDriver): WebDriver is an object that controls the web browser and allows
        the script to interact with it.
        - codewars_email (str): The email address associated with the Codewars account that you
        want to sign in to.
        - codewars_password (str): The password for the Codewars account that the user wants to
        sign in to.
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
    ):
        """
        This function creates a README.md file in a specified folder path with information about a
        coding problem.

        Args:
        - kata_folder_path: The path to the folder where the README.md file will be created or
        updated.
        - kata: A dictionary containing information about a specific CodeWars kata, including its
        name, ID, completion date, and completed languages.
        - kata_details: The `kata_details` parameter is a dictionary containing details about a
        specific coding challenge or kata, such as its description, tags, and rank.
        """
        file_path = os.path.join(kata_folder_path, "README.md")
        content = (
            f"# [{kata['name']}](https://www.codewars.com/kata/{kata['id']})\n\n"
            f"- **Completed at:** {kata['completedAt']}\n\n"
            f"- **Completed languages:** {', '.join(kata['completedLanguages'])}\n\n"
            f"- **Tags:** {', '.join(kata_details['tags'])}\n\n"
            f"- **Rank:** {kata_details['rank']['name']}\n\n"
            f"## Description\n\n{kata_details['description']}"
        )

        try:
            if os.path.exists(file_path):
                if content != await read_file_content(file_path):
                    await write_file_content(file_path, content)
            else:
                await write_file_content(file_path, content)
        except OSError:
            self.error_list.append(
                f"An error occurred while creating the problem description file of {kata['name']}."
            )

    async def create_solution_file(self, kata_folder_path, kata, language):
        """
        This function creates a solution file for a given kata and language by scraping the code
        from the newest solution on the kata's Codewars page.

        Args:
        - kata_folder_path: The path to the folder where the solution file will be created.
        - kata: The kata parameter is a dictionary containing information about a specific coding
        challenge on Codewars, such as its ID, name, and description.
        - language: The programming language of the solution file to be created.
        """
        try:
            self.browser.get(
                f"https://www.codewars.com/kata/{kata['id']}/solutions/{language}/me/newest"
            )

            solutions_list = self.browser.find_element(By.ID, "solutions_list")
            solution_item = solutions_list.find_element(By.TAG_NAME, "div")
            solution_code = solution_item.find_element(By.TAG_NAME, "pre").text

            file_path = os.path.join(
                kata_folder_path, f"solution.{self.language_extensions[language]}"
            )

            if os.path.exists(file_path):
                if solution_code != await read_file_content(file_path):
                    await write_file_content(file_path, solution_code)
            else:
                await write_file_content(file_path, solution_code)
        except TimeoutError:
            self.error_list.append(
                f"The driver took too much time for {kata['name']} (${language})."
            )
        except NoSuchElementException:
            self.error_list.append(
                "A web element was not found on the page (create solution file step) of "
                f"{kata['name']} (${language})."
            )
        except OSError:
            self.error_list.append(
                "There was a problem while creating the solution file for "
                f"{kata['name']} (${language})."
            )

    async def create_index_file(self):
        """
        This function creates an index file with a list of completed code challenges sorted
        by category.
        """
        file_path = "./README.md"

        for problems in self.kata_categories.values():
            problems.sort()

        content = (
            "# Index of katas by its category/discipline\n\n"
            + f"These are the {self.total_completed_katas} code challenges I have completed:"
            + "\n## Fundamentals\n\n"
            + "\n".join(self.kata_categories["reference"])
            + "\n## Algorithms\n\n"
            + "\n".join(self.kata_categories["algorithms"])
            + "\n## Bug Fixes\n\n"
            + "\n".join(self.kata_categories["bug_fixes"])
            + "\n## Refactoring\n\n"
            + "\n".join(self.kata_categories["refactoring"])
            + "\n## Puzzles\n\n"
            + "\n".join(self.kata_categories["games"])
        )

        try:
            if os.path.exists(file_path):
                if content != await read_file_content(file_path):
                    await write_file_content(file_path, content)
            else:
                await write_file_content(file_path, content)
        except OSError:
            self.error_list.append("There was a problem while creating the index file.")


if __name__ == "__main__":
    codewars_logger = CodewarsLogger()
    asyncio.run(codewars_logger.main())
