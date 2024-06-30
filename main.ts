function dispCol (num: number, col: number) {
    nn = num
    setPixel(4, col, nn % 2 == 1)
    nn = Math.trunc(nn / 2)
    setPixel(3, col, nn % 2 == 1)
    nn = Math.trunc(nn / 2)
    setPixel(2, col, nn % 2 == 1)
    nn = Math.trunc(nn / 2)
    setPixel(1, col, nn % 2 == 1)
}
input.onButtonPressed(Button.A, function () {
    n += 1
    dispTime(n)
})
function dispTime (time: number) {
    min2 = time % 60
    m1 = min2 % 10
    m10 = Math.idiv(min2, 10)
    hr = Math.trunc(time / 60)
    h1 = hr % 10
    h10 = Math.trunc(hr / 10)
    dispCol(h10, 0)
    dispCol(h1, 1)
    dispCol(12, 2)
    dispCol(m10, 3)
    dispCol(m1, 4)
}
input.onButtonPressed(Button.AB, function () {
    n += 60
    dispTime(n)
})
input.onButtonPressed(Button.B, function () {
    n += -1
    dispTime(n)
})
function setPixel (row: number, col2: number, setclr: boolean) {
    if (setclr) {
        led.plot(col2, row)
    } else {
        led.unplot(col2, row)
    }
}
let h10 = 0
let h1 = 0
let hr = 0
let m10 = 0
let m1 = 0
let min2 = 0
let nn = 0
let n = 0
led.setBrightness(50)
n = 1439
// Increment time (n)
basic.forever(function () {
    n += 1
    if (n > 1440) {
        n = 0
    }
    basic.pause(60000)
})
// Blink Ticker
control.inBackground(function () {
    for (let index = 0; index < 30; index++) {
        led.plot(0, 0)
        led.unplot(4, 0)
        basic.pause(1000)
        led.unplot(0, 0)
        led.plot(4, 0)
        basic.pause(1000)
    }
})
// Display Time and
// 
// wait 1 min
control.inBackground(function () {
    dispTime(n)
    basic.pause(60000)
})
