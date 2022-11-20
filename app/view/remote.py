import tkinter as tk
from tkinter import ttk
import os
from controller.remote_controller import RemoteController


class RemoteWindow(object):
    """
    :class Remote - Class that initializes the remote GUI. This class uses
                    Python Tkinter to created a Roku Remote Control UI.

                    Future Consideration -> Make Controller prettier.
    """
    # Place holder for All Icons visible on the remote control
    _images = {
            "up":os.path.join(os.path.dirname(__file__),'./icons/up-arrow.png'),
            "down":os.path.join(os.path.dirname(__file__), './icons/down-arrow.png'),
            "right":os.path.join(os.path.dirname(__file__),'./icons/right-arrow.png'),
            "left":os.path.join(os.path.dirname(__file__),'./icons/left-arrow.png'),
            "ok": os.path.join(os.path.dirname(__file__),'./icons/ok-icon.png'),
            "power": os.path.join(os.path.dirname(__file__),'./icons/powerbutton.png'),
            "back": os.path.join(os.path.dirname(__file__),'./icons/back-button.png'),
            "home":os.path.join(os.path.dirname(__file__),'./icons/home-button.png'),
            "mic":os.path.join(os.path.dirname(__file__),'./icons/mic-button.png'),
            "sleep":os.path.join(os.path.dirname(__file__),'./icons/moon-button.png'),
            "plus":os.path.join(os.path.dirname(__file__),'./icons/plus-button.png'),
            "minus":os.path.join(os.path.dirname(__file__),'./icons/minus.png'),
            "mute":os.path.join(os.path.dirname(__file__),'./icons/mute-button.png'),
            "channeldown":os.path.join(os.path.dirname(__file__),'./icons/channel-down-button.png'),
            "channelup":os.path.join(os.path.dirname(__file__),'./icons/channel-up-button.png')
    }

    def __init__(self, controller: RemoteController) -> None:
        """
        :constructor - this constructor is the main initializer / creator
                       for all tkinter components.
        """

        # Main Window
        window = tk.Tk()                    
        window.minsize(width=350, height=500)
        window.maxsize(width=350, height=500)
        window.title("Roku Remote")
        

        # Create all main containers
        frame_height = 500 / 2
        top_frame = tk.Frame(window, width=350, height=150, padx=3, pady=3)
        middle_frame = tk.Frame(window,width=350, height=100, padx=3, pady=3)
        bottom_frame = tk.Frame(window,width=350, height=200, padx=3, pady=3)

       
        # Layout frames in window
        window.rowconfigure(1,weight=1)
        window.columnconfigure(0, weight=1)

        top_frame.grid(row=0, column=0)
        middle_frame.grid(row=1, column=0)
        bottom_frame.grid(row=2, column=0)


        ########################
        # TOP Frame Widgets
        #   GRID:
        #   |B|_|U|_|P|
        #   |_|L|K|R|_|
        #   |_|_|D|_|_|
        ########################
        
        #UP Arrow Key
        u_btn_img = tk.PhotoImage(file=self._images['up']) # Icon 
        u_btn_label = tk.Label(image=u_btn_img) # Label 
        u_btn = tk.Button(  # Button Attributes
            top_frame, 
            image=u_btn_img, 
            command=lambda:controller.up()
        )
        # Grid Frame
        u_btn.grid(row=0, column=2)
       
        # DOWN
        d_btn_img = tk.PhotoImage(file=self._images['down'])
        d_btn_label = tk.Label(image=d_btn_img)
        d_btn = tk.Button(
            top_frame, 
            image=d_btn_img, 
            command=lambda:controller.down()
        )
        d_btn.grid(row=2, column=2)
        
        # RIGHT
        r_btn_img = tk.PhotoImage(file=self._images['right'])
        r_btn_label = tk.Label(image=r_btn_img)
        r_btn = tk.Button(
            top_frame, 
            image=r_btn_img, 
            command=lambda:controller.right()
        )
        r_btn.grid(row=1, column=3)
        

        # LEFT
        l_btn_img = tk.PhotoImage(file=self._images['left'])
        l_btn_label = tk.Label(image=l_btn_img)
        l_btn = tk.Button(
            top_frame, 
            image=l_btn_img, 
            command=lambda:controller.left()
        )
        l_btn.grid(row=1, column=1)
        

        # OK Button
        ok_btn_img = tk.PhotoImage(file=self._images['ok'])
        ok_btn_label = tk.Label(image=ok_btn_img)
        ok_btn = tk.Button(
            top_frame,
            image=ok_btn_img,
            command=lambda:controller.ok()
        )
        ok_btn.grid(row=1, column=2)

        # Power Button
        power_btn_img = tk.PhotoImage(file=self._images['power'])
        power_btn_label = tk.Label(image=power_btn_img)
        power_btn = tk.Button(
            top_frame,
            image=power_btn_img,
            command=lambda:controller.power()
        )
        power_btn.grid(row=0, column=4)

        # Power Button
        back_btn_img = tk.PhotoImage(file=self._images['back'])
        back_btn_label = tk.Label(image=back_btn_img)
        back_btn = tk.Button(
            top_frame,
            image=back_btn_img,
            command=lambda:controller.back()
        )
        back_btn.grid(row=0, column=0)


        # MIDDLE FRAME WIDGETS
        ########################
        # MIDDLE Frame Widgets
        #   GRID:
        #   |H|M|S|
        #   |_|_|_|
        #   |U|M|CU|
        #   |D|_|CD|
        ########################
        # configure layout
        # Home button
        home_button_img = tk.PhotoImage(file=self._images['home'])
        home_button_label = tk.Label(image=home_button_img)
        home_button = tk.Button(
            middle_frame,
            image=home_button_img,
            command=lambda:controller.home()
        )
        home_button.grid(row=0,column=0)

        # Microphone Button -> TODO implement speach recognition
        mic_button_img = tk.PhotoImage(file=self._images['mic'])
        mic_button_label = tk.Label(image=mic_button_img)
        mic_button = tk.Button(
            middle_frame,
            image=mic_button_img,
            command=lambda:controller.mic()
        )
        mic_button.grid(row=0,column=2)

        # Sleep button -> TODO cannot modify sleep on TV yet
        sleep_button_img = tk.PhotoImage(file=self._images['sleep'])
        sleep_button_label = tk.Label(image=sleep_button_img)
        sleep_button = tk.Button(
            middle_frame,
            image=sleep_button_img,
            command=lambda:controller.sleep()
        )
        sleep_button.grid(row=0,column=4)

        # Button for increasing volume
        plus_button_img = tk.PhotoImage(file=self._images['plus'])
        plus_button_label = tk.Label(image=plus_button_img)
        plus_button = tk.Button(
            bottom_frame,
            image=plus_button_img,
            command=lambda:controller.plus_volume()
        )
        plus_button.grid(row=2,column=0)

        # Button for decreasing volume
        minus_button_img = tk.PhotoImage(file=self._images['minus'])
        minus_button_label = tk.Label(image=minus_button_img)
        minus_button = tk.Button(
            bottom_frame,
            image=minus_button_img,
            command=lambda:controller.minus_volume()
        )
        minus_button.grid(row=3,column=0)
        
        # Mute button
        mute_button_img = tk.PhotoImage(file=self._images['mute'])
        mute_button_label = tk.Label(image=mute_button_img)
        mute_button = tk.Button(
            bottom_frame,
            image=mute_button_img,
            command=lambda:controller.mute()
        )
        mute_button.grid(row=2,column=1, rowspan=2)

        # Channel Up button
        cup_button_img = tk.PhotoImage(file=self._images['channelup'])
        cup_button_label = tk.Label(image=cup_button_img)
        cup_button = tk.Button(
            bottom_frame,
            image=cup_button_img,
            command=lambda:controller.channel_up()
        )
        cup_button.grid(row=2,column=2)
        
        # Channel Down button
        cdown_button_img = tk.PhotoImage(file=self._images['channeldown'])
        cdown_button_label = tk.Label(image=cdown_button_img)
        cdown_button = tk.Button(
            bottom_frame,
            image=cdown_button_img,
            command=lambda:controller.channel_down()
        )
        cdown_button.grid(row=3,column=2)

        # Main Loop
        window.mainloop()                 


