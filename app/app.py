import configparser as parser
from controller.remote_controller import RemoteController
from view.remote import RemoteWindow
from errors.roku_device_not_found import RokuDeviceNotFound
from view.error import RokuDeviceNotFoundWindow
import os


def run(): 
    # # Open View
    try:
        remote = RemoteWindow(
            controller=RemoteController()
        )
    except RokuDeviceNotFound as e:
        RokuDeviceNotFoundWindow()
        

if __name__ == "__main__":
    run()