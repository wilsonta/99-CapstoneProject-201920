# Tim Wilson Sprint 3 120 Capstone Project


import tkinter
from tkinter import ttk
import time
import rosebot

def get_m1_sprint_3_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    m1_speed_entry=ttk.Entry(frame, width=8)

    m1_speed_entry.grid(row=0, column=0)


    return frame