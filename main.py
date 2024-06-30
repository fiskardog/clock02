def dispCol(num: number, col: number):
    global nn
    nn = num
    setPixel(4, col, nn % 2 == 1)
    nn = int(nn / 2)
    setPixel(3, col, nn % 2 == 1)
    nn = int(nn / 2)
    setPixel(2, col, nn % 2 == 1)
    nn = int(nn / 2)
    setPixel(1, col, nn % 2 == 1)

def on_button_pressed_a():
    global n
    n += 1
    dispTime(n)
input.on_button_pressed(Button.A, on_button_pressed_a)

def dispTime(time: number):
    global min2, m1, m10, hr, h1, h10
    min2 = time % 60
    m1 = min2 % 10
    m10 = Math.idiv(min2, 10)
    hr = int(time / 60)
    h1 = hr % 10
    h10 = int(hr / 10)
    dispCol(h10, 0)
    dispCol(h1, 1)
    dispCol(12, 2)
    dispCol(m10, 3)
    dispCol(m1, 4)

def on_button_pressed_ab():
    global n
    n += 60
    dispTime(n)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global n
    n += -1
    dispTime(n)
input.on_button_pressed(Button.B, on_button_pressed_b)

def setPixel(row: number, col2: number, setclr: bool):
    if setclr:
        led.plot(col2, row)
    else:
        led.unplot(col2, row)
h10 = 0
h1 = 0
hr = 0
m10 = 0
m1 = 0
min2 = 0
nn = 0
n = 0
led.set_brightness(50)
n = 1439
"""

Increment time (n)

"""

def on_forever():
    global n
    n += 1
    if n > 1440:
        n = 0
    basic.pause(60000)
basic.forever(on_forever)

"""

Blink Ticker

"""

def on_in_background():
    for index in range(30):
        led.plot(0, 0)
        led.unplot(4, 0)
        basic.pause(1000)
        led.unplot(0, 0)
        led.plot(4, 0)
        basic.pause(1000)
control.in_background(on_in_background)

"""

Display Time and

wait 1 min

"""

def on_in_background2():
    dispTime(n)
    basic.pause(60000)
control.in_background(on_in_background2)
