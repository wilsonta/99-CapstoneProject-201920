
import time
import rosebot


def turn_using_encoder(robot,speed,inches):
    inches_per_degree = robot.drive_system.wheel_circumference / 360
    degrees = inches / inches_per_degree

    robot.drive_system.left_motor.reset_position()
    robot.drive_system.go(speed, -speed)
    while True:
        print(robot.drive_system.left_motor.get_position())
        if abs(robot.drive_system.left_motor.get_position()) >= degrees:
            robot.drive_system.stop()
            break



def draw_square(robot,speed,side_length):
    for _ in range(4):
        robot.drive_system.go_straight_for_inches_using_encoder(side_length, speed)
        turn_using_encoder(robot,speed,5.45)


def draw_triangle(robot,speed,side_length):
    for _ in range(3):
        robot.drive_system.go_straight_for_inches_using_encoder(side_length, speed)
        turn_using_encoder(robot, speed, 7.3)

def draw_pentagon(robot,speed,side_length):
    for _ in range(5):
        robot.drive_system.go_straight_for_inches_using_encoder(side_length, speed)
        turn_using_encoder(robot, speed, 4.48)

def draw_any_shape(robot,speed,side_lenth,number_of_sides):
    turn_distance = ((180 - ((180 + (number_of_sides - 3) * 180))/number_of_sides) * 6.3)/90
    for _ in range(number_of_sides):
        robot.drive_system.go_straight_for_inches_using_encoder(side_lenth,speed)
        turn_using_encoder(robot,speed,turn_distance)

def unknown_operation(object, num_of_sides):
    for k in range(len(object)):
        x = handle(for button)['command'] lambda:





def go_to_store(robot,speed):
    pass


