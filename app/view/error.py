import tkinter as tk
from tkinter import messagebox
from errors.roku_device_not_found import RokuDeviceNotFound

class RokuDeviceNotFoundWindow():
    def __init__(self) -> None:
        msg_box = messagebox.showerror('Roku Remote Error', 'Roku Device Not found. Make sure Roku device is connect to local network.',
                                        icon='warning')
        button1 = tk.Button(root, text='Exit Application', command=exit_application, bg='brown', fg='white')
