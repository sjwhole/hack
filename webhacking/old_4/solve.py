import os
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    opts = Options()
    opts.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 RuxitSynthetic/1.0 v6780912532 t4984864254591130994 athfa3c3975 altpub cvcv=2 smf=0")

    path = "./chromedriver"

    driver = webdriver.Chrome(executable_path=path, options=opts)

    url = "https://webhacking.kr/login.php"
    driver.get(url)
    ID = "your_id"
    PASSWORD = "your_password"

    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/form/table/tbody/tr[1]/td[2]/input").send_keys(
        ID)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(
        PASSWORD)
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/form/input").click()

    while True:
        driver.get("https://webhacking.kr/challenge/web-04/")
        key = driver.find_element(By.XPATH, "/html/body/center/form/table/tbody/tr[1]/td/b").text

        if os.system(f"grep -n '{key}' rainbow_table.txt") == 0:
            print(f"{key} FOUND")
            os.system(f"grep -n '{key}' rainbow_table.txt > ans.txt")
            with open("ans.txt", "r") as f:
                line = f.readline()
                num = int((re.search(r"(\d+):.+", line).groups()[0])) + 10000000 - 1

            driver.find_element(By.XPATH, "/html/body/center/form/table/tbody/tr[2]/td[2]/input").send_keys(
                f"{num}salt_for_you")
            driver.find_element(By.XPATH, "/html/body/center/form/table/tbody/tr[2]/td[3]/input").click()
            input()
            break
        else:
            print(f"{key} NOT FOUND")
