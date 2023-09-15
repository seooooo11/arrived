def on_button_pressed_a():
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(최종도착시간)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global 최종도착시간
    if name == "endtime":
        music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
            music.PlaybackMode.UNTIL_DONE)
        최종도착시간 = value
        basic.show_number(value)
radio.on_received_value(on_received_value)

카운트 = 0
최종도착시간 = 0
도착초음파 = 100
radio.set_group(78)

def on_forever():
    global 도착초음파, 카운트
    도착초음파 = 100
    도착초음파 = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
    if 12 > 도착초음파 and 도착초음파 > 0:
        radio.send_string("end")
        basic.show_icon(IconNames.HEART)
        카운트 = 0
        basic.pause(5000)
    else:
        if 카운트 < 6:
            카운트 += 1
            basic.pause(600)
            if 카운트 == 1:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    # . . . .
                    """)
            elif 카운트 == 2:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . . . .
                    . # . . .
                    # # . . .
                    """)
            elif 카운트 == 3:
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . # . .
                    . # # . .
                    # # # . .
                    """)
            elif 카운트 == 4:
                basic.show_leds("""
                    . . . . .
                    . . . # .
                    . . # # .
                    . # # # .
                    # # # # .
                    """)
            else:
                basic.show_leds("""
                    . . . . #
                    . . . # #
                    . . # # #
                    . # # # #
                    # # # # #
                    """)
        else:
            카운트 = 0
basic.forever(on_forever)
