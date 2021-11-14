function mv(cd) {
    kk(star.style.left - 50, star.style.top - 50);
    if (cd == 100) star.style.left = parseInt(star.style.left + 0, 10) + 50 + "px";
    if (cd == 97) star.style.left = parseInt(star.style.left + 0, 10) - 50 + "px";
    if (cd == 119) star.style.top = parseInt(star.style.top + 0, 10) - 50 + "px";
    if (cd == 115) star.style.top = parseInt(star.style.top + 0, 10) + 50 + "px";
    if (cd == 124) location.href = String.fromCharCode(cd) + ".php"; // do it!
}

function kk(x, y) {
    let rndc = Math.floor(Math.random() * 9000000);
    document.body.innerHTML += "<font color=#" + rndc + " id=aa style=position:relative;left:" + x + ";top:" + y + " onmouseover=this.innerHTML=''>*</font>";
}

const url = "https://webhacking.kr/challenge/js-3/"
console.log(url + String.fromCharCode(124) + ".php")


