distance = 0
basic.show_leds("""
    # . . . #
        # # . # #
        . . # . .
        # # . # #
        . # . # .
""")
Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
Tinybit.RGB_Car_Program().clear()
Tinybit.RGB_Car_Program().clear()

def on_forever():
    if distance <= 5:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_BACK, 60)
    elif distance > 5 and distance < 200:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 60)
    else:
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
basic.forever(on_forever)

def on_forever2():
    global distance
    distance = Tinybit.Ultrasonic_Car()
    if distance <= 5:
        Tinybit.RGB_Car_Big2(0, 0, 255)
    elif distance > 5 and distance < 200:
        Tinybit.RGB_Car_Big2(0, 255, 0)
    else:
        Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
basic.forever(on_forever2)

def on_forever3():
    if distance < 5:
        basic.show_arrow(ArrowNames.NORTH)
    elif distance > 5 and distance < 200:
        basic.show_arrow(ArrowNames.SOUTH)
    else:
        basic.clear_screen()
basic.forever(on_forever3)
