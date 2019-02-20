import rosebot
import ev3dev.ev3 as ev3
import time
import math

def chase(robot, speed):
    print('chasing')
    robot = rosebot.RoseBot()
    while True:
        blob = robot.sensor_system.camera.get_biggest_blob()
        distance = float(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        if distance < 0.5:
            distance = float(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
            if distance < 0.5:
                robot.arm_and_claw.raise_arm()
                break
        if blob.get_area() > 100:
            if blob.center.x > 185:
                robot.drive_system.go(speed, -speed)
            elif blob.center.x < 135:
                robot.drive_system.go(-speed, speed)
            else:
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

def follow(length, speed):
    print('following')
    robot = rosebot.RoseBot()
    start = time.time()
    while True:
        blob = robot.sensor_system.camera.get_biggest_blob()
        distance = float(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        while distance < 5:
            while distance < 5:
                distance = float(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
                robot.drive_system.stop()
        if blob.get_area() > 100:
            if blob.center.x > 185:
                robot.drive_system.go(speed, -speed)
            elif blob.center.x < 135:
                robot.drive_system.go(-speed, speed)
            else:
                robot.drive_system.go(speed, speed)
        robot.drive_system.go(speed, speed)
        if time.time() - start >= length:
            break
    robot.drive_system.stop()