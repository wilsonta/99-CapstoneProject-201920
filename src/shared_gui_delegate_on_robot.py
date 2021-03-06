"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Matthew White, Tim Wilson, and Greg Wenning.
  Winter term, 2018-2019.
"""
import rosebot
import m1_extra_robot
import m3_robot_sprint_3
import m2_robot_sprint_3
class Respond_to_GUI_message(object):

    def __init__(self,robot):
        """
        :type robot: rosebot.Rosebot
        """


        self.robot = robot

        self.stop_program = False

    def go(self, left_wheel_speed, right_wheel_speed):
        left = int(left_wheel_speed)
        right = int(right_wheel_speed)
        self.robot.drive_system.go(left,right)

    def move_arm_to_position(self,desired_pos):
        self.robot.arm_and_claw.move_arm_to_position(int(desired_pos))

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()

    def beep(self,number_of_beep_s):
        for _ in range(number_of_beep_s):
            self.robot.sound_system.beeper.beep().wait()

    def tone(self, tone_length, tone_frequency):
        self.robot.sound_system.tone_maker.play_tone(tone_frequency,tone_length)

    def speak(self, phrase):
        self.robot.sound_system.speech_maker.speak(phrase).wait()

    def m3_camera_data(self):
        self.robot.drive_system.display_camera_data()

    def spin_clockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, area)

    def spin_counterclockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)

    def go_straight_for_seconds(self, seconds, speed):
        print('go_straight_for_seconds')
        self.robot.drive_system.go_straight_for_seconds(seconds, speed)

    def go_straight_for_inches_using_time(self,inches,speed):
        print('o_straight_for_inches_using_time')
        self.robot.drive_system.go_straight_for_inches_using_time(inches, speed)

    def go_straight_for_inches_using_encoder(self,inches,speed):
        print('delegate success, go_straight_for_inches_using_encoder')
        print(inches, speed)
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(speed))

    def quit(self):
        self.stop_program = True

    def go_until_color_is(self,color, speed):
        self.robot.drive_system.go_straight_until_color_is(color,speed)

    def go_straight_until_color_is_not(self, color, speed):
        self.robot.drive_system.go_straight_until_color_is_not(color,speed)

    def go_forward_distance_is_less_than(self, inches, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(inches,speed)

    def go_backward_distance_is_greater_than(self, inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(inches, speed)

    def go_distance_is_within(self, delta, inches, speed):
        self.robot.drive_system.go_until_distance_is_within(delta, inches, speed)

    def increasing_tone(self,speed,orig_tone,delta_tone):
        self.robot.drive_system.tone_as_you_get_closer(orig_tone,delta_tone,speed)

    def beep_as_it_runs(self, speed):
        self.robot.drive_system.beep_as_it_runs(speed)

    def cycle_LED_lights(self, LED_initial_rate, LED_rate_cycle_increase):
        self.robot.drive_system.cycle_LED_lights(LED_initial_rate, LED_rate_cycle_increase)

    def smart_clockwise_m2(self,area_entry,speed_entry,tone_freq_entry,delta_tone_entry):
        self.robot.drive_system.spin_clockwise_until_sees_object(speed_entry,area_entry)
        self.robot.drive_system.tone_as_you_get_closer(tone_freq_entry,delta_tone_entry,speed_entry)

    def smart_counter_clockwise_m2(self,area_entry,speed_entry,tone_freq_entry,delta_tone_entry):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed_entry,area_entry)
        self.robot.drive_system.tone_as_you_get_closer(tone_freq_entry,delta_tone_entry,speed_entry)

    def smart_clockwise_m3(self, area, speed, LED_initial_rate, LED_rate_cycle_increase):
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, area)
        self.robot.drive_system.cycle_LED_lights(LED_initial_rate, LED_rate_cycle_increase)

    def smart_counter_m3(self, area, speed, LED_initial_rate, LED_rate_cycle_increase):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)
        self.robot.drive_system.cycle_LED_lights(LED_initial_rate, LED_rate_cycle_increase)

    def smart_clockwise_m1(self, area, speed):
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, area)
        self.robot.drive_system.beep_as_it_runs(speed)

    def smart_counter_m1(self, area, speed):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)
        self.robot.drive_system.beep_as_it_runs(speed)

    def m1_pit_stop(self,speed):
        m1_extra_robot.m1_pit_stop(self.robot,speed)

    def m1_stop_off_track(self,color,speed):
        m1_extra_robot.m1_stop_off_track(self.robot, color, speed)

    def m1_avoid_collision(self, speed):
        m1_extra_robot.m1_avoid_collision(self.robot, speed)

    def m1_celebrate(self, speed, area):
        m1_extra_robot.m1_celebrate(self.robot, speed, area)

    def m1_follow_pacecar(self,speed):
        m1_extra_robot.m1_follow_pacecar(self.robot, int(speed))

    def m1_speak_start_engines(self, phrase):
        m1_extra_robot.m1_speak_start_engines(self.robot,phrase)

    def m1_pass(self, speed):
        m1_extra_robot.m1_pass(self.robot, int(speed))

    def m1_brake_lights(self, speed):
        m1_extra_robot.m1_brake_lights(self.robot, int(speed))

    def m1_green_lights_go(self,speed):
        m1_extra_robot.m1_green_lights_go(self.robot, int(speed))

    def m3_chase(self, speed):
        m3_robot_sprint_3.chase(self.robot, speed)

    def draw_square_m2(self, speed,side_length):
        print('delegate')
        m2_robot_sprint_3.draw_square(self.robot,speed,side_length)

    def draw_triangle_m2(self,speed,side_length):
        m2_robot_sprint_3.draw_triangle(self.robot,speed,side_length)

    def draw_pentagon_m2(self,speed,side_length):
        m2_robot_sprint_3.draw_pentagon(self.robot,speed,side_length)

    def draw_custom_shape_m2(self,speed,side_length,number_of_sides):
        m2_robot_sprint_3.draw_any_shape(self.robot,speed,side_length,number_of_sides)

