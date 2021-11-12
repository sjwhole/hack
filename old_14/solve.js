const url = "https://webhacking.kr/challenge/js-1/";
let ul = url;
ul = ul.indexOf(".kr");
ul = ul * 30;

const ans = url + "?" + ul * ul;
console.log(ans)