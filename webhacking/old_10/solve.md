- js code를 보고 style.left == 1600이면 ?go=1600px주소로 이동하는 것을 알아냄  
- 그러나 https://webhacking.kr/challenge/code-1/?go=1600px 이동시 no hack 문구가 뜬다.  
- style.left를 1599로 바꾸고 a태그를 통해서 주소를 접속했다. 
이랬더니 정상적으로 클리어


## 두 접속의 차이점
### Referer
- 찾아봤더니 바로 Header에 **Referer**가 다름
- Referer를 통해 어디서 접속하는지 확인하고 있던 것
- Referer를 https://webhacking.kr/challenge/code-1/ 설정하고 https://webhacking.kr/challenge/code-1/?go=1600px 접속하면 정상적으로 해결!
