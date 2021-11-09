# 7 - SQL Injection
- \s 정규표현식 공백의미
- 2를 만들어야하나 +, -, *, /  등 연산 불가능
- 그러므로 char(50)을 이용해서 숫자 2를 만들면 된다
- https://webhacking.kr/challenge/web-07/index.php?val=3)union(select(50) 접속하다보 문제해결!