var enco = '';
var enco2 = 126;
var enco3 = 33;

for (i = 1; i < 122; i++) {
    enco = enco + String.fromCharCode(i, 0);
}

function enco_(x) {
    return enco.charCodeAt(x);
}

let ans = "=" + String.fromCharCode(enco_(240)) + String.fromCharCode(enco_(220)) + String.fromCharCode(enco_(232)) + String.fromCharCode(enco_(192)) + String.fromCharCode(enco_(226)) + String.fromCharCode(enco_(200)) + String.fromCharCode(enco_(204)) + String.fromCharCode(enco_(222 - 2)) + String.fromCharCode(enco_(198)) + "~~~~~~" + String.fromCharCode(enco2) + String.fromCharCode(enco3);

let ansUrl = `https://webhacking.kr/challenge/code-3/?ans${ans}`
console.log(`Answer URL: ${ansUrl}`)