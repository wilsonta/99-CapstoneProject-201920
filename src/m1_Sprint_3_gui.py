# Tim Wilson Sprint 3 120 Capstone Project


import tkinter
from tkinter import ttk
import time
import rosebot

def get_m1_sprint_3_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    m1_sprint_3_label= ttk.Label(frame, text='Racecar')
    m1_speed_entry=ttk.Entry(frame, width=8)
    m1_speed_entry.insert(0,"100")
    m1_speed_label=ttk.Label(frame, text='Speed')
    m1_color_entry= ttk.Entry(frame, width=8)
    m1_color_entry.insert(0,'')
    m1_color_label= ttk.Label(frame, text='Color')
    pit_stop_button=ttk.Button(frame, text='Pit Stop')
    celebrate_button= ttk.Button(frame, text='Celebrate')
    follow_pacecar_button= ttk.Button(frame, text='Follow Pace Car')
    stop_off_track_button= ttk.Button(frame, text='Stop off Track')
    avoid_collision_button= ttk.Button(frame, text='Avoid Collision')
    start_engine_button= ttk.Button(frame, text='Start Engine')
    m1_area_entry= ttk.Entry(frame, width=8)
    m1_area_entry.insert(0,'1000')
    m1_area_label=ttk.Label(frame, text='Area')
    m1_speech_entry=ttk.Entry(frame, width=8)
    m1_speech_entry.insert(0, 'Start your Engines')
    m1_speech_label=ttk.Label(frame, text='Speak')
    pass_button=ttk.Button(frame, text='Pass')
    brake_lights_button=ttk.Button(frame, text='Brake Lights')
    green_lights_go_button=ttk.Button(frame, text= 'Green Lights')


    m1_sprint_3_label.grid(row=0, column=1)
    m1_speed_entry.grid(row=1, column=0)
    m1_speed_label.grid(row=2, column=0)
    m1_color_entry.grid(row=1, column=1)
    m1_color_label.grid(row=2,column=1)
    m1_area_entry.grid(row=1,column=2)
    m1_area_label.grid(row=2, column=2)
    m1_speech_entry.grid(row=1, column=3)
    m1_speech_label.grid(row=2, column=3)
    pit_stop_button.grid(row=3, column=0)
    celebrate_button.grid(row=3, column=1)
    follow_pacecar_button.grid(row=4, column=0)
    stop_off_track_button.grid(row=4, column=1)
    avoid_collision_button.grid(row=4, column=2)
    start_engine_button.grid(row=5, column=1)
    pass_button.grid(row=5, column=2)
    brake_lights_button.grid(row=5, column=3)
    green_lights_go_button.grid(row=4, column=3)


    pit_stop_button['command']= lambda: handle_pit_stop(mqtt_sender, m1_speed_entry)
    stop_off_track_button['command']= lambda: handle_m1_stop_off_track(mqtt_sender, m1_color_entry, m1_speed_entry)
    avoid_collision_button['command']= lambda: handle_avoid_collision(mqtt_sender, m1_speed_entry)
    celebrate_button['command']= lambda: handle_celebrate(mqtt_sender, m1_speed_entry, m1_area_entry)
    follow_pacecar_button['command']= lambda: handle_follow_pacecar(mqtt_sender, m1_speed_entry)
    start_engine_button['command']= lambda: handle_m1_speak_start_engines(mqtt_sender, m1_speech_entry)
    pass_button['command']= lambda: handle_m1_pass(mqtt_sender, m1_speed_entry)
    brake_lights_button['command']= lambda: handle_m1_brake_lights(mqtt_sender, m1_speed_entry)
    green_lights_go_button['command']= lambda: handle_m1_green_lights_go(mqtt_sender, m1_speed_entry)



    return frame



def handle_m1_stop_off_track(mqtt_sender, m1_color_entry, m1_speed_entry):
    print('I am going until', m1_color_entry.get(), 'in a speed of:', m1_speed_entry.get())

    mqtt_sender.send_message('m1_stop_off_track', [m1_color_entry.get(), m1_speed_entry.get()])

def handle_pit_stop(mqtt_sender, m1_speed_entry):
    mqtt_sender.send_message('m1_pit_stop', [m1_speed_entry.get()])

def handle_avoid_collision(mqtt_sender, m1_speed_entry):
    mqtt_sender.send_message('m1_avoid_collision', [m1_speed_entry.get()])

def handle_celebrate(mqtt_sender, m1_speed_entry, m1_area_entry):
    m1_speed_entry=int(m1_speed_entry.get())
    m1_area_entry=int(m1_area_entry.get())
    mqtt_sender.send_message('m1_celebrate', [m1_speed_entry, m1_area_entry])

def handle_follow_pacecar(mqtt_sender, m1_speed_entry):
    m1_speed_entry=int(m1_speed_entry.get())
    mqtt_sender.send_message('m1_follow_pacecar', [m1_speed_entry])

def handle_m1_speak_start_engines(mqtt_sender, m1_speech_entry):
    mqtt_sender.send_message('m1_speak_start_engines', [m1_speech_entry.get()])

def handle_m1_pass(mqtt_sender, m1_speed_entry):
    m1_speed_entry=int(m1_speed_entry.get())
    mqtt_sender.send_message('m1_pass', [m1_speed_entry])

def handle_m1_brake_lights(mqtt_sender, m1_speed_entry):
    m1_speed_entry=int(m1_speed_entry.get())
    mqtt_sender.send_message('m1_brake_lights', [m1_speed_entry])

def handle_m1_green_lights_go(mqtt_sender, m1_speed_entry):
    m1_speed_entry=int(m1_speed_entry.get())
    mqtt_sender.send_message('m1_green_lights_go', [m1_speed_entry])