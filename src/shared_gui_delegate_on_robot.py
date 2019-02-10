"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Matthew White, Tim Wilson, and Greg Wenning.
  Winter term, 2018-2019.
"""
import rosebot
class Respond_to_GUI_message(object):

    def __init__(self,robot):
        """
        :type robot: rosebot.Rosebot
        """


        self.robot = robot

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



