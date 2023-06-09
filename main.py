import asyncio
import os

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


async def main():
    credentials = read_user_credentials()

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, executable_path="./geckodriver")

    codewars_username = ""
    email = ""
    codewars_password = ""

    try:
        codewars_username = credentials[0]
        email = credentials[1]
        codewars_password = credentials[2]
    except IndexError:
        print("You must pass all the credentials.")
        return

    completed_katas_url = f"https://www.codewars.com/api/v1/users/{codewars_username}/code-challenges/completed"
    kata_info_url = "https://www.codewars.com/api/v1/code-challenges/"
    main_folder_path = "./Katas"

    os.makedirs(main_folder_path, exist_ok=True)

    await sign_in_to_codewars(driver, email, codewars_password)

    main_response = requests.get(completed_katas_url)
    main_response_json = main_response.json()
    number_of_pages = main_response_json["totalPages"]

    tasks = []
    for page in range(number_of_pages):
        response = requests.get(f"{completed_katas_url}?page={page}")
        kata_object = response.json()

        for kata in kata_object["data"]:
            response_kata_info = requests.get(f"{kata_info_url}{kata['id']}")
            kata_info_object = response_kata_info.json()
            kata_folder_path = os.path.join(main_folder_path, kata["slug"])

            tasks.append(
                create_main_file_async(
                    kata_folder_path,
                    kata["name"],
                    kata["id"],
                    kata["completedAt"],
                    kata["completedLanguages"],
                    kata_info_object["description"],
                    kata_info_object["rank"],
                    kata_info_object["tags"],
                )
            )
            await asyncio.sleep(0.1)

    await asyncio.gather(*tasks)
    await create_index_file_async()

    driver.quit()

    if not exceptions:
        print("\nAll data was loaded successfully.")
    else:
        print(
            f"\nAll data was loaded successfully except {len(exceptions)} katas: {', '.join(exceptions)}."
        )

    input("Press any key to exit.")


def read_user_credentials():
    credentials = []
    print(
        "CodewarsLogger, v1.2.0. Source code: https://github.com/JoseDeFreitas/CodewarsLogger"
    )
    credentials.append(input("Enter your Codewars username: "))
    credentials.append(input("Enter your email: "))
    credentials.append(input("Enter your Codewars password: "))
    return credentials


async def sign_in_to_codewars(driver, email, codewars_password):
    try:
        driver.get("https://www.codewars.com/users/sign_in")
    except:
        print("The driver took too much time.")
        return

    try:
        sign_in_form = driver.find_element(By.ID, "new_user")
        driver.find_element(By.ID, "user_email").send_keys(email)
        driver.find_element(By.ID, "user_password").send_keys(codewars_password)
        sign_in_form.find_element(By.CLASS_NAME, "is-red").click()
    except:
        print("A web element was not found on the page (sign-in step).")


async def create_main_file_async(
    folder, name, id, date, languages, description, rank, tags
):
    file_path = os.path.join(folder, "README.md")
    with open(file_path, "w") as file:
        file.write("# " + name + "\n\n")
        file.write("## Description\n\n")
        file.write(description + "\n\n")
        file.write("## Details\n\n")
        file.write("Kata ID: " + id + "\n\n")
        file.write("Completed Date: " + date + "\n\n")
        file.write("Completed Languages: " + ", ".join(languages) + "\n\n")
        file.write("Rank: " + rank["name"] + " - " + rank["color"] + "\n\n")
        file.write("Tags: " + ", ".join(tags) + "\n\n")
        file.write("## Solutions\n\n")
        file.write("This kata has been solved in the following languages:\n\n")

        for language in languages:
            file.write("- " + language + "\n")


async def create_index_file_async():
    main_folder_path = "./Katas"
    index_file_path = os.path.join(main_folder_path, "index.md")
    index_text = "# Codewars Kata Index\n\n"

    for root, dirs, files in os.walk(main_folder_path):
        if root == main_folder_path:
            for directory in sorted(dirs):
                index_text += "- [" + directory + "](./" + directory + "/README.md)\n"

    with open(index_file_path, "w") as index_file:
        index_file.write(index_text)


asyncio.run(main())
