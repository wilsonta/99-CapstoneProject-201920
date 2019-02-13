"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Greg Wenning, Tim Wilson, Mathew White.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time
import rosebot


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")
    inches_label = ttk.Label(frame, text="Number of inches to travel")
    time_label = ttk.Label(frame, text = "Number of seconds")
    color_sensor_label =ttk.Label(frame, text='Go to Color')
    desired_distance_for_ir_sensor_label = ttk.Label(frame, text='Desired Distance')
    delta_for_ir_sensor_label = ttk.Label(frame, text='+/- for Smart Distance')


    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")
    inches_entry = ttk.Entry(frame, width = 8)
    inches_entry.insert(0, "0")
    time_entry = ttk.Entry(frame, width = 8)
    time_entry.insert(0,"0")
    color_entry = ttk.Entry(frame, width=8)
    desired_distance_for_ir_sensor_entry = ttk.Entry(frame, width=8)
    delta_for_ir_sensor_entry = ttk.Entry(frame, width=8)

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")
    go_straight_seconds_button = ttk.Button(frame, text="Straight for Seconds")
    go_straight_for_inches_using_time_button = ttk.Button(frame, text="Straight for # of inches (time)")
    go_straight_for_inches_using_encoder_button = ttk.Button(frame, text="Straight for # of inches (encoders)")
    camera_data_button = ttk.Button(frame, text='camera data')
    go_until_color_is_button = ttk.Button(frame, text='Go to Color')
    desired_distance_for_ir_sensor_button_backwards = ttk.Button(frame, text = 'Move Backwards to Desired Distance')
    desired_distance_for_ir_sensor_button_forwards = ttk.Button(frame, text = 'Move Forwards to the Desired Distance')
    desired_distance_for_ir_sensor_button_smart = ttk.Button(frame, text = 'Smart Move to Distance')


    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)
    inches_label.grid(row=6 ,column=0)
    time_label.grid(row=6 ,column=1)
    time_entry.grid(row = 7, column=1)
    inches_entry.grid(row = 7,column = 0)
    camera_data_button.grid(row=9, column=0)
    color_sensor_label.grid(row=10, column=0)
    color_entry.grid(row=11, column=0)
    desired_distance_for_ir_sensor_label.grid(row=10, column=1)
    delta_for_ir_sensor_label.grid(row=10, column=2)
    desired_distance_for_ir_sensor_entry.grid(row=11,column=1)
    delta_for_ir_sensor_entry.grid(row=11,column=2)
    desired_distance_for_ir_sensor_button_backwards.grid(row=12,column=1)
    desired_distance_for_ir_sensor_button_forwards.grid(row=13,column=1)
    desired_distance_for_ir_sensor_button_smart.grid(row=14,column=1)


    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)
    go_straight_seconds_button.grid(row = 8,column = 0)
    go_straight_for_inches_using_time_button.grid(row = 8, column = 1)
    go_straight_for_inches_using_encoder_button.grid(row = 8, column = 2)
    go_until_color_is_button.grid(row=12, column=0)


    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    go_straight_seconds_button["command"] = lambda: handle_go_straight_for_seconds(mqtt_sender,
                                                                                   time_entry,right_speed_entry)
    go_straight_for_inches_using_time_button["command"] = lambda: handle_go_straight_for_inches_using_time(mqtt_sender,
                                                                                                           inches_entry,right_speed_entry)
    go_straight_for_inches_using_encoder_button["command"] = lambda: handle_go_straight_for_inches_using_encoder(mqtt_sender,
                                                                                                                 inches_entry,right_speed_entry)
    camera_data_button['command'] = lambda: handle_camera_data(mqtt_sender)
    go_until_color_is_button['command'] =lambda: handle_go_until_color_is(mqtt_sender,color_entry,right_speed_entry)

    desired_distance_for_ir_sensor_button_smart['command'] = lambda: handle_smart_to_distance(mqtt_sender,delta_for_ir_sensor_entry,desired_distance_for_ir_sensor_entry,right_speed_entry)
    desired_distance_for_ir_sensor_button_forwards['command'] = lambda: handle_forwards_to_distance(mqtt_sender,desired_distance_for_ir_sensor_entry,right_speed_entry)
    desired_distance_for_ir_sensor_button_backwards['command'] = lambda: handle_backwards_to_distance(mqtt_sender,desired_distance_for_ir_sensor_entry,right_speed_entry)




    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

def get_sound_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    frame.grid()

    frame_label = ttk.Label(frame, text='SoundSystem')
    beep_button = ttk.Button(frame, text='how many times to beep')
    tone_length_label = ttk.Label(frame, text='how long to tone')
    tone_frequncy_label = ttk.Label(frame, text='what frequency')
    beep_entry = ttk.Entry(frame, width=8)
    tone_length_entry = ttk.Entry(frame, width=8)
    tone_frequency_entry = ttk.Entry(frame, width=8)
    tone_button = ttk.Button(frame, text='test tone')
    speak_button = ttk.Button(frame, text='phrase to speak')
    speak_entry = ttk.Entry(frame, width=20)

    frame_label.grid(row=0, column=1)
    beep_button.grid(row=1, column=0)
    tone_length_label.grid(row=1, column=1)
    tone_frequncy_label.grid(row=1, column=2)
    beep_entry.grid(row=2, column=0)
    tone_length_entry.grid(row=2, column=1)
    tone_frequency_entry.grid(row=2, column=2)
    tone_button.grid(row=2, column=3)
    speak_button.grid(row=1, column=5)
    speak_entry.grid(row=2, column=5)

    beep_button['command'] = lambda: handle_beep(beep_entry, mqtt_sender)
    tone_button['command'] = lambda: handle_tone(tone_length_entry, tone_frequency_entry, mqtt_sender)
    speak_button['command'] = lambda: handle_speak(speak_entry, mqtt_sender)

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('forward',left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message('go',[int(left_entry_box.get()),int(right_entry_box.get())])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('backward',left_entry_box.get(),right_entry_box.get())
    left = -int(left_entry_box.get())
    right = -int(right_entry_box.get())
    mqtt_sender.send_message('go',[str(left),str(right)])

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('left',left_entry_box.get(),right_entry_box.get())
    left = int(left_entry_box.get())
    right = -int(right_entry_box.get())
    mqtt_sender.send_message('go',[str(left),str(right)])

def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('right',left_entry_box.get(),right_entry_box.get())
    left = -int(left_entry_box.get())
    right = int(right_entry_box.get())
    mqtt_sender.send_message('go',[str(left),str(right)])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    left = 0
    right = 0
    print('stop',left,right)
    mqtt_sender.send_message('go',[left,right])

def handle_camera_data(mqtt_sender):
    mqtt_sender.send_message('m3_camera_data')

def handle_backwards_to_distance(mqtt_sender, desired_distance_for_ir_sensor_entry, right_entry_box):
    mqtt_sender.send_message('',[desired_distance_for_ir_sensor_entry.get(),right_entry_box.get()])

def handle_forwards_to_distance(mqtt_sender, desired_distance_for_ir_sensor_entry, right_entry_box):
    mqtt_sender.send_message('',[desired_distance_for_ir_sensor_entry.get(),right_entry_box.get()])

def handle_smart_to_distance(mqtt_sender, delta_for_ir_sensor_entry, desired_distance_for_ir_sensor_entry, right_entry_box):
    mqtt_sender.send_message('',[delta_for_ir_sensor_entry.get(), desired_distance_for_ir_sensor_entry.get(),right_entry_box.get()])


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Arm Raising')

    mqtt_sender.send_message('raise_arm')


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('Arm Lowering')

    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Calibrating Arm")
    mqtt_sender.send_message('calibrate_arm')

def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('Moving Arm to Position: ',arm_position_entry.get())
    pos = int(arm_position_entry.get())
    mqtt_sender.send_message('move_arm_to_position',[pos])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """

#####################################################################
# handlers for bottuns in the Sound Frame
####################################################################
def go_straight_for_inches_using_time(self,inches,speed):
    self.robot.drive_system.go_straight_for_inches_using_time(inches, speed)

def handle_beep(beep_entry, mqtt_sender):
    beep = int(beep_entry.get())
    print('beeping', beep, 'times')
    mqtt_sender.send_message('beep', [beep])

def handle_tone(tone_length_entry, tone_frequency_entry, mqtt_sender):
     tone_length = int(tone_length_entry.get())
     tone_frequency = int(tone_frequency_entry.get())
     print('I am about to play a tone with a freq of ', tone_frequency, 'for ', tone_length, ' seconds')
     mqtt_sender.send_message('tone', [tone_length, tone_frequency])

def handle_speak(speak_entry, mqtt_sender):
    speak = speak_entry.get()
    print(speak)
    mqtt_sender.send_message('speak', [speak])

def handle_go_straight_for_seconds(mqtt_sender, right_speed_entry,time_entry):
    print('I will go straight for :', time_entry.get(),' sec, at a spped of: ', time_entry.get())
    seconds = int(time_entry.get())
    speed = int(right_speed_entry.get())
    mqtt_sender.send_message('go_straight_for_seconds',[seconds, speed])

def handle_go_straight_for_inches_using_time(mqtt_sender,inches_entry,right_speed_entry):
    print('I am going straight for', inches_entry.get(),' in at a speed of: ', right_speed_entry.get())
    inches = int(inches_entry.get())
    speed = int(right_speed_entry.get())

    mqtt_sender.send_message('go_straight_for_inches_using_time',[inches,speed])


def handle_go_straight_for_inches_using_encoder(mqtt_sender, inches_entry, right_speed_entry):
    print('I am going straight for', inches_entry.get(), ' in at a speed of: ', right_speed_entry.get())
    inches = int(inches_entry.get())
    speed = int(right_speed_entry.get())

    mqtt_sender.send_message('go_straight_for_inches_using_encoder', [inches, speed])

def handle_go_until_color_is(mqtt_sender, color_entry, right_speed_entry):
    print('I am going until', color_entry.get(), 'in a speed of:', right_speed_entry.get())

    mqtt_sender.send_message('go_until_color_is', [color_entry.get(), right_speed_entry.get()])