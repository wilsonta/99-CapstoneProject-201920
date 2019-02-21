import tkinter as ttk
import time
import rosebot


def get_m3_sprint_3_frame(window, mqtt_sender):
    frame = ttk.Frame(window, borderwidth=5, relief="ridge")
    frame.grid()

    square_button = ttk.Button(frame, text='Square')
    square_button.grid(row=0, column=1)
    speed_to_clean_entry = ttk.Entry(frame, width=10)
    speed_to_clean_entry.grid(row=1, column=1)
    speed_to_clean_label = ttk.Label(frame, text = 'Speed')
    speed_to_clean_label.grid(row = 2, column=1)
    triangle_button = ttk.Button(frame, text='Triangle')
    triangle_button.grid(row=0, column=0)
    side_length_entry = ttk.Entry(frame,width=10)
    side_length_entry.grid(row=1,column=0)
    side_length_label = ttk.Label(frame, text = 'Side Length')
    side_length_label.grid(row = 2, column =0)

    pentagon_button = ttk.Button(frame,text='Pentagon')
    pentagon_button.grid(row = 0,column=2)

    custom_shape_button = ttk.Button(frame, text = 'Draw Custom Shape')
    custom_shape_button.grid(row=5,column=5)

    number_of_sides_entry = ttk.Entry(frame,width=10)
    number_of_sides_entry.grid(row = 4,column = 5)
    number_of_sides_label = ttk.Label(frame, text='Desired Number of Sides')
    number_of_sides_label.grid(row = 4,column = 4)


    square_button['command'] = lambda: handle_square_button(mqtt_sender,speed_to_clean_entry,side_length_entry)
    triangle_button['command'] = lambda: handle_triangle_button(mqtt_sender,speed_to_clean_entry,side_length_entry)
    pentagon_button['command'] = lambda: handle_pentagon_button(mqtt_sender,speed_to_clean_entry,side_length_entry)
    custom_shape_button['command'] = lambda: handle_custom_shapes_button(mqtt_sender,speed_to_clean_entry,side_length_entry,number_of_sides_entry)

    return frame

def handle_square_button(mqtt_sender,speed_to_clean_entry,side_length_entry):
    print('Drawing a Square')
    mqtt_sender.send_message('draw_square_m2',[int(speed_to_clean_entry.get()),int(side_length_entry.get())])

def handle_triangle_button(mqtt_sender,speed_to_clean_entry,side_length_entry):
    print('Drawing a Triangle')
    mqtt_sender.send_message('draw_triangle_m2',[int(speed_to_clean_entry.get()),int(side_length_entry.get())])

def handle_pentagon_button(mqtt_sender,speed_to_clean_entry,side_length_entry):
    print('Drawing a Pentagon')
    mqtt_sender.send_message('draw_pentagon_m2',[int(speed_to_clean_entry.get()),int(side_length_entry.get())])

def handle_custom_shapes_button(mqtt_sender,speed_to_clean_entry,side_length_entry,number_of_sides_entry):
    print('Drawing Custom Shape')
    mqtt_sender.send_message('draw_custom_shape_m2',[int(speed_to_clean_entry.get()),int(side_length_entry.get()),int(number_of_sides_entry.get())])