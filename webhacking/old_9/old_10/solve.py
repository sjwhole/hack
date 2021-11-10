import requests

if __name__ == '__main__':
    url = "https://webhacking.kr/challenge/code-1/?go=1600px"
    headers = {"Referer": "https://webhacking.kr/challenge/code-1/"}
    cookies = {"PHPSESSID": ""}
    response = requests.get(url, headers=headers, cookies=cookies)
    print(response.text)
