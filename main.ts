input.onButtonPressed(Button.A, function on_button_pressed_a() {
    control.reset()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showNumber(최종도착시간)
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    if (name == "endtime") {
        music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
        최종도착시간 = value
        basic.showNumber(value)
    }
    
})
let 카운트 = 0
let 최종도착시간 = 0
let 도착초음파 = 100
radio.setGroup(78)
basic.forever(function on_forever() {
    
    도착초음파 = 100
    도착초음파 = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.Centimeters)
    if (12 > 도착초음파 && 도착초음파 > 0) {
        radio.sendString("end")
        basic.showIcon(IconNames.Heart)
        카운트 = 0
        basic.pause(5000)
    } else if (카운트 < 6) {
        카운트 += 1
        basic.pause(600)
        if (카운트 == 1) {
            basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    # . . . .
                    `)
        } else if (카운트 == 2) {
            basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . . . .
                    . # . . .
                    # # . . .
                    `)
        } else if (카운트 == 3) {
            basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . # . .
                    . # # . .
                    # # # . .
                    `)
        } else if (카운트 == 4) {
            basic.showLeds(`
                    . . . . .
                    . . . # .
                    . . # # .
                    . # # # .
                    # # # # .
                    `)
        } else {
            basic.showLeds(`
                    . . . . #
                    . . . # #
                    . . # # #
                    . # # # #
                    # # # # #
                    `)
        }
        
    } else {
        카운트 = 0
    }
    
})
