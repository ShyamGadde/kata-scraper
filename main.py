# pylint: disable=missing-module-docstring
import asyncio
import os
import sys

import aiohttp
import dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CodewarsLogger:
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

        self.username, self.email, self.password = self.get_credentials()

        self.completed_katas_url = f"https://www.codewars.com/api/v1/users/{self.username}/code-challenges/completed"
        self.kata_info_url = "https://www.codewars.com/api/v1/code-challenges/"
        self.main_folder_path = "./katas"

    async def main(self):
        """
        TODO: Add docstring.
        """
        os.makedirs(self.main_folder_path, exist_ok=True)

        self.sign_in_to_codewars(self.browser, self.email, self.password)

        async with aiohttp.ClientSession() as client:
            response = await client.get(self.completed_katas_url)
            response_json = await response.json()
            number_of_pages = response_json["totalPages"]
            print(number_of_pages)

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
            print("The driver took too much time.")
            sys.exit(1)

        try:
            sign_in_form: WebElement = driver.find_element(By.ID, "new_user")
            driver.find_element(By.ID, "user_email").send_keys(codewars_email)
            driver.find_element(By.ID, "user_password").send_keys(codewars_password)
            sign_in_form.find_element(
                By.CSS_SELECTOR, 'button.is-red[type="submit"]'
            ).click()
        except NoSuchElementException:
            print("A web element was not found on the page (sign-in step).")
            sys.exit(1)


codewars_logger = CodewarsLogger()
asyncio.run(codewars_logger.main())


# async def main():
#     credentials = read_user_credentials()

#     options = Options()
#     options.headless = True
#     options.set_capability("geckodriverPath", "usr/local/bin/geckodriver")
#     driver = webdriver.Firefox(options=options)

#     codewars_username = ""
#     email = ""
#     codewars_password = ""

#     try:
#         codewars_username = credentials[0]
#         email = credentials[1]
#         codewars_password = credentials[2]
#     except IndexError:
#         print("You must pass all the credentials.")
#         return

#     completed_katas_url = f"https://www.codewars.com/api/v1/users/{codewars_username}/code-challenges/completed"
#     kata_info_url = "https://www.codewars.com/api/v1/code-challenges/"
#     main_folder_path = "./Katas"

#     await sign_in_to_codewars(driver, email, codewars_password)

#     main_response = requests.get(completed_katas_url)
#     main_response_json = main_response.json()
#     number_of_pages = main_response_json["totalPages"]

#     tasks = []
#     for page in range(number_of_pages):
#         response = requests.get(f"{completed_katas_url}?page={page}")
#         kata_object = response.json()

#         for kata in kata_object["data"]:
#             response_kata_info = requests.get(f"{kata_info_url}{kata['id']}")
#             kata_info_object = response_kata_info.json()
#             kata_folder_path = os.path.join(main_folder_path, kata["slug"])

#             tasks.append(
#                 create_main_file_async(
#                     kata_folder_path,
#                     kata["name"],
#                     kata["id"],
#                     kata["completedAt"],
#                     kata["completedLanguages"],
#                     kata_info_object["description"],
#                     kata_info_object["rank"],
#                     kata_info_object["tags"],
#                 )
#             )
#             await asyncio.sleep(0.1)

#     await asyncio.gather(*tasks)
#     await create_index_file_async()

#     driver.quit()

#     if not exceptions:
#         print("\nAll data was loaded successfully.")
#     else:
#         print(
#             f"\nAll data was loaded successfully except {len(exceptions)} katas: {', '.join(exceptions)}."
#         )

#     input("Press any key to exit.")


# def read_user_credentials():
#     credentials = []
#     print(
#         "CodewarsLogger, v1.2.0. Source code: https://github.com/JoseDeFreitas/CodewarsLogger"
#     )
#     credentials.append(input("Enter your Codewars username: "))
#     credentials.append(input("Enter your email: "))
#     credentials.append(input("Enter your Codewars password: "))
#     return credentials


# async def create_main_file_async(
#     folder, name, id, date, languages, description, rank, tags
# ):
#     file_path = os.path.join(folder, "README.md")
#     with open(file_path, "w") as file:
#         file.write("# " + name + "\n\n")
#         file.write("## Description\n\n")
#         file.write(description + "\n\n")
#         file.write("## Details\n\n")
#         file.write("Kata ID: " + id + "\n\n")
#         file.write("Completed Date: " + date + "\n\n")
#         file.write("Completed Languages: " + ", ".join(languages) + "\n\n")
#         file.write("Rank: " + rank["name"] + " - " + rank["color"] + "\n\n")
#         file.write("Tags: " + ", ".join(tags) + "\n\n")
#         file.write("## Solutions\n\n")
#         file.write("This kata has been solved in the following languages:\n\n")

#         for language in languages:
#             file.write("- " + language + "\n")


# async def create_index_file_async():
#     main_folder_path = "./Katas"
#     index_file_path = os.path.join(main_folder_path, "index.md")
#     index_text = "# Codewars Kata Index\n\n"

#     for root, dirs, files in os.walk(main_folder_path):
#         if root == main_folder_path:
#             for directory in sorted(dirs):
#                 index_text += "- [" + directory + "](./" + directory + "/README.md)\n"

#     with open(index_file_path, "w") as index_file:
#         index_file.write(index_text)


# asyncio.run(main())
