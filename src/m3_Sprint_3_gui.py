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
    #Labels

    #Entry
    interrogate_entry = ttk.Entry(frame, width=10)
    chase_speed_entry = ttk.Entry(frame, width=8)
    #Grid
    frame_label.grid(row=0, column=1)
    interrogate_button.grid(row=1, column=0)
    interrogate_entry.grid(row=2, column=0)
    chase_button.grid(row=1, column=1)
    chase_speed_entry.grid(row=2, column=1)
    capture_button.grid(row=3, column=1)
    #button callbacks
    interrogate_button['command'] = lambda: handle_interrogate(interrogate_entry, mqtt_sender)
    chase_button['command'] = lambda: handle_chase(chase_speed_entry, mqtt_sender)
    capture_button['command'] = lambda: handle_capture(mqtt_sender)

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


    return frame