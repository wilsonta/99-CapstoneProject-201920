import rosebot
import tkinter
from tkinter import ttk
import time

def get_m3_sprint_3_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text='Police')
    #Buttons
    interrogate_button = ttk.Button(frame, text='Interrogate')
    chase_button = ttk.Button(frame, text='chase')
    capture_button = ttk.Button(frame, text='capture')
    release_button = ttk.Button(frame, text='release')
    lights_button = ttk.Button(frame, text='lights')
    siren_button = ttk.Button(frame, text='siren')
    follow_buton = ttk.Button(frame, text='follow')
    #Labels
    light_length_label = ttk.Label(frame, text='How long lights on?')
    siren_length_label = ttk.Label(frame, text='How long siren?')
    chase_speed_label = ttk.Label(frame, text='What speed to chase?')
    interrogate_phrase = ttk.Label(frame, text='What phrase?')
    follow_length_label = ttk.Label(frame, text='How long to follow?')
    follow_speed_label = ttk.Label(frame, text='What speed to follow?')
    #Entry
    interrogate_entry = ttk.Entry(frame, width=10)
    chase_speed_entry = ttk.Entry(frame, width=8)
    lights_length_entry = ttk.Entry(frame, width=8)
    siren_length_entry = ttk.Entry(frame, width=8)
    follow_length_entry = ttk.Entry(frame, width=8)
    follow_speed_entry = ttk.Entry(frame, width=8)
    #Grid
    frame_label.grid(row=0, column=1)
    interrogate_button.grid(row=1, column=0)
    interrogate_entry.grid(row=3, column=0)
    interrogate_phrase.grid(row=2, column=0)
    chase_button.grid(row=1, column=1)
    chase_speed_entry.grid(row=3, column=1)
    chase_speed_label.grid(row=2, column=1)
    capture_button.grid(row=4, column=0)
    release_button.grid(row=5, column=0)
    lights_button.grid(row=1, column=2)
    light_length_label.grid(row=2, column=2)
    lights_length_entry.grid(row=3, column=2)
    siren_button.grid(row=1, column=3)
    siren_length_label.grid(row=2, column=3)
    siren_length_entry.grid(row=3, column=3)
    follow_buton.grid(row=4, column=1)
    follow_length_entry.grid(row=6, column=1)
    follow_length_label.grid(row=5, column=1)
    follow_speed_entry.grid(row=8, column=1)
    follow_speed_label.grid(row=7, column=1)
    #button callbacks
    interrogate_button['command'] = lambda: handle_interrogate(interrogate_entry, mqtt_sender)
    chase_button['command'] = lambda: handle_chase(chase_speed_entry, mqtt_sender)
    capture_button['command'] = lambda: handle_capture(mqtt_sender)
    release_button['command'] = lambda: handle_release(mqtt_sender)
    lights_button['command'] = lambda: handle_lights(mqtt_sender, lights_length_entry)
    siren_button['command'] = lambda: handle_siren(mqtt_sender, siren_length_entry)
    follow_buton['command'] = lambda: handle_follow(mqtt_sender, follow_length_entry, follow_speed_entry)

############################################################################################
    def handle_interrogate(interrogate_entry, mqtt_sender):
        interrogate = interrogate_entry.get()
        print(interrogate)
        mqtt_sender.send_message('speak', [interrogate])

    def handle_chase(chase_speed_entry, mqtt_sender):
        speed = int(chase_speed_entry.get())
        print(speed)
        mqtt_sender.send_message('m3_chase', [speed])

    def handle_capture(mqtt_sender):
        print('capturing')
        mqtt_sender.send_message('raise_arm')

    def handle_release(mqtt_sender):
        print('releasing')
        mqtt_sender.send_message('lower_arm')

    def handle_lights(mqtt_sender, lights_length_entry):
        print('lighting')
        legnth = int(lights_length_entry.get())
        mqtt_sender.send_message('m3_lights', [legnth])

    def handle_siren(mqtt_sender, siren_length_entry):
        print('sirening')
        length = int(siren_length_entry.get())
        mqtt_sender.send_message('m3_siren', [length])

    def handle_follow(mqtt_sender, follow_length_entry, follow_speed_entry):
        print('following')
        length = int(follow_length_entry.get())
        speed = int(follow_speed_entry.get())
        mqtt_sender.send_message('m3_follow', [length, speed])

    return frame