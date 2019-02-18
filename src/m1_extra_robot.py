import time
import rosebot


def m1_pit_stop(robot, speed):
    robot= rosebot.RoseBot()
    robot.drive_system.go(0, speed)
    time.sleep(.8)
    robot.drive_system.go(speed, speed)
    time.sleep(1.5)
    robot.drive_system.go(speed, 0)
    time.sleep(.8)
    robot.drive_system.stop()
    arm_and_claw = robot.arm_and_claw
    arm_and_claw.calibrate_arm()
    robot.drive_system.go(speed, 0)
    time.sleep(.8)
    robot.drive_system.go(speed, speed)
    time.sleep(1.5)
    robot.drive_system.go(0, speed)
    time.sleep(.8)
    robot.drive_system.stop()