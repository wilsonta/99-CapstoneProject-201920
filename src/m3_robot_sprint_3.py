import rosebot
import ev3dev.ev3 as ev3
import time
import math

def chase(robot, speed):
    print('chasing')
    robot = rosebot.RoseBot()
    while True:
        blob = robot.sensor_system.camera.get_biggest_blob()
        #robot = rosebot.RoseBot()
        #print(blob)
        distance = float(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        print(distance)
        if distance < 1:
            distance = float(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
            print(distance)
            if distance < 1:
                robot.arm_and_claw.raise_arm()
                break
        if blob.get_area() > 100:
            if blob.center.x > 185:
                print('right')
                robot.drive_system.go(speed, -speed)

            elif blob.center.x < 135:
                print('left')
                robot.drive_system.go(-speed, speed)
            else:
                print('forward')
                robot.drive_system.go(speed, speed)
    robot.drive_system.stop()
def turn_on_lights(length):
    robot = rosebot.RoseBot()
    total = 0
    while True:
        robot.led_system.left_led.turn_on()
        time.sleep(0.1)
        robot.led_system.right_led.turn_on()
        time.sleep(0.1)
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_off()
        total = total +1
        if total > length:
            break

def siren(length):
    robot = rosebot.RoseBot()
    for k in range(2*length):
        frequency = 850
        robot.sound_system.tone_maker.play_tone(frequency, 500).wait()