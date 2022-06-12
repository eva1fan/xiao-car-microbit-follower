let distance = 0
basic.showLeds(`
    # . . . #
    # # . # #
    . . # . .
    # # . # #
    . # . # .
    `)
Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
Tinybit.RGB_Car_Program().clear()
Tinybit.RGB_Car_Program().clear()
basic.forever(function () {
    if (distance <= 5) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Back, 60)
    } else if (distance > 5 && distance < 200) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 60)
    } else {
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
    }
})
basic.forever(function () {
    distance = Tinybit.Ultrasonic_Car()
    if (distance <= 5) {
        Tinybit.RGB_Car_Big2(0, 0, 255)
    } else if (distance > 5 && distance < 200) {
        Tinybit.RGB_Car_Big2(0, 255, 0)
    } else {
        Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
    }
})
basic.forever(function () {
    if (distance < 5) {
        basic.showArrow(ArrowNames.North)
    } else if (distance > 5 && distance < 200) {
        basic.showArrow(ArrowNames.South)
    } else {
        basic.clearScreen()
    }
})
