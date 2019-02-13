"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Tim Wilson.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #run_test_drive_system()
    #run_test_arm()
    real_thing()


def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Respond_to_GUI_message(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(.01)

def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()

def run_test_drive_system():
    robot = rosebot.RoseBot()
    #robot.drive_system.go_straight_for_seconds(5, 70)
    #time.sleep(5)
    #robot.drive_system.go_straight_for_inches_using_time(7, 70)
    #robot.drive_system.go_straight_for_inches_using_encoder(8, -70)
    #robot.drive_system.go_straight_until_color_is('Blue',100)
    robot.drive_system.go_straight_until_color_is_not('Blue',100)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()