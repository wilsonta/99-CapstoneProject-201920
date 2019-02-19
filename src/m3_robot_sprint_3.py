import rosebot
import ev3dev.ev3 as ev3
import time
import math

def chase(robot, speed):
    print('chasing')
    while True:
        blob = robot.sensor_system.camera.get_biggest_blob()
        #print(blob)
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
                distance = float(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
                print(distance)
                if distance < 1.5:
                    robot.arm_and_claw.raise_arm()