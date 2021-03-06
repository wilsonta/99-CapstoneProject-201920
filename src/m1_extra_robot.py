import time
import rosebot


def m1_pit_stop(robot, speed):
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

def m1_stop_off_track(robot, color, speed):
    #robot= rosebot.RoseBot()
    robot.drive_system.go_straight_until_color_is(color, speed)

def m1_avoid_collision(robot, speed):
    inches=1.5
    #robot= rosebot.RoseBot()
    robot.drive_system.go_forward_until_distance_is_less_than(inches, speed)

def m1_celebrate(robot, speed, area):
    #robot=rosebot.RoseBot()
    robot.drive_system.spin_clockwise_until_sees_object(speed, area)
    robot.drive_system.beep_as_it_runs(speed)
    robot.drive_system.left_motor.turn_on(speed)
    robot.drive_system.right_motor.turn_on(-speed)
    time.sleep(5)
    robot.drive_system.stop()

def m1_follow_pacecar(robot, speed):
    print('start')
    print('starting')
    time.sleep(3)
    while True:
        blob=robot.sensor_system.camera.get_biggest_blob()
        print(blob)
        if blob.get_area()>100:
            if blob.center.x>185:
                print('right')
                robot.drive_system.go(speed,-speed)

            elif blob.center.x<135:
                print('left')
                robot.drive_system.go(-speed,speed)
            else:
                print('forward')
                robot.drive_system.go(speed,speed)

def m1_speak_start_engines(robot, phrase):
    #robot=rosebot.RoseBot()
    print('statement')
    robot.sound_system.speech_maker.speak(phrase)

def m1_pass(robot,speed):
    robot.drive_system.go(speed, 0)
    time.sleep(.8)
    robot.drive_system.go(speed, speed)
    time.sleep(1)
    robot.drive_system.go(0, speed)
    time.sleep(.8)
    print('a')
    robot.drive_system.go(2*speed, 2*speed)
    print('b')
    time.sleep(4)
    robot.drive_system.go(0, speed)
    print('c')
    time.sleep(.8)
    robot.drive_system.go(speed, speed)
    print('d')
    time.sleep(1)
    robot.drive_system.go(speed, 0)
    print('e')
    time.sleep(.8)
    robot.drive_system.stop()

def m1_brake_lights(robot, speed):
    robot.drive_system.go(speed, speed)
    time.sleep(3)
    left_led=robot.led_system.left_led
    right_led=robot.led_system.right_led
    left_led.set_color_by_name(left_led.RED)
    right_led.set_color_by_name(right_led.RED)
    while True:
        if speed>0:
            speed=speed/2
        else:
            break
    robot.drive_system.stop()

def m1_green_lights_go(robot, speed):
    robot.drive_system.go(speed, speed)
    left_led = robot.led_system.left_led
    right_led = robot.led_system.right_led
    left_led.set_color_by_name(left_led.GREEN)
    right_led.set_color_by_name(right_led.GREEN)
    time.sleep(4)
    robot.drive_system.stop()



