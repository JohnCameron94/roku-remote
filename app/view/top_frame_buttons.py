import tkinter as tk
from controller.remote_controller import RemoteController
import os


class ArrowKeys(object):
    # Arrow Key
    _images = {
        "up":os.path.join(os.path.dirname(__file__),'./icons/up-arrow.png'),
        "down":os.path.join(os.path.dirname(__file__), './icons/down-arrow.png'),
        "right":os.path.join(os.path.dirname(__file__),'./icons/right-arrow.png'),
        "left":os.path.join(os.path.dirname(__file__),'./icons/left-arrow.png'),
        "ok": os.path.join(os.path.dirname(__file__),'./icons/ok-icon.png')
    }

    def build_frame(self, controller: RemoteController, window: tk.Tk) -> tk.Frame:
        # Main Frame that holds the arrow keys
        mfrm = tk.Frame(window)

    
       
        # Init Arrow Keys
        # UP
        u_btn_img = tk.PhotoImage(file=self._images['up'])
        u_btn_label = tk.Label(image=u_btn_img)
        u_btn = tk.Button(
            window, 
            image=u_btn_img, 
            command=lambda:controller.up()
        ).grid(row=0, column=1)
       

       

        # DOWN
        d_btn_img = tk.PhotoImage(file=self._images['down'])
        d_btn_label = tk.Label(image=d_btn_img)
        d_btn = tk.Button(
            window, 
            image=d_btn_img, 
            command=lambda:controller.down()
        ).grid(row=2, column=1)
        

        # RIGHT
        r_btn_img = tk.PhotoImage(file=self._images['right'])
        r_btn_label = tk.Label(image=r_btn_img)
        r_btn = tk.Button(
            window, 
            image=r_btn_img, 
            command=lambda:controller.right()
        ).grid(row=1, column=2)
        

        # LEFT
        l_btn_img = tk.PhotoImage(file=self._images['left'])
        l_btn_label = tk.Label(image=l_btn_img)
        l_btn = tk.Button(
            window, 
            image=l_btn_img, 
            command=lambda:controller.left()
        ).grid(row=1, column=0)
        

        # OK Button
        ok_btn_img = tk.PhotoImage(file=self._images['ok'])
        ok_btn_label = tk.Label(image=ok_btn_img)
        ok_btn = tk.Button(
            window,
            image=ok_btn_img,
            command=lambda:controller.ok()
        ).grid(row=1, column=1)
        
        
        # mfrm.pack()

        # return mfrm


