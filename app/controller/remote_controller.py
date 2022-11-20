import requests
import re
import socket
import subprocess
from controller.remote_key_map import key_map
from controller.remote_keys import(
    KeyGroups,
    ArrowKeys,
    ActionKeys
)
from errors.roku_device_not_found import RokuDeviceNotFound

class RemoteController(object):
    """
    :class - RemoteController: this class controls all possible commands
             a user can generate by a button click from the UI or any
             other action a user may take.
    """
    _url: str  # Built URL



    def __init__(self) -> None:
        """
        :constructore - Initializing all class variables
                        used to perform HTTP calls to roku api.
        """
        self._url = self._find_roku_device()


    def _find_roku_device(self) -> str:
        """
        :method - build_url is a private function within the Remote
                  Controller class that is used to initialize and build
                  the class variable URL.
        """
        # Regex pattern for IPV4 addresses
        IPV4_PATTERN = "(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
        # arp -a command on terminal
        shell_cmd = ['arp', '-a']
        # Execute Arp command
        _ = subprocess.check_output(shell_cmd)
        # Get IP output and decode
        output = _.decode('utf-8')
        # Find IP's using regex pattern
        ips = re.findall(IPV4_PATTERN, output)
        url = None
        for ip in ips:
            try:
                # Add timeout since we are expecting some failure, or invalid connections
                resp = requests.get(f'http://{ip}:8060/query/device-info', timeout=1)
                if resp.status_code == 200:
                    url=f'http://{ip}:8060/'
            except Exception as e:
                pass # Do Nothing, possible it will not connect
        
        if url == None:
            raise RokuNotFound()

        return url

    
    def down(self)-> str:
        """
        :function - down: function that implements the down arrow 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ARROW.value][ArrowKeys.DOWN.value] }'
        )
        return response

    def up(self) -> str:
        """
        :function - up: function that implements the up arrow 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ARROW.value][ArrowKeys.UP.value] }'
        )
        return response
    
    def left(self) -> str:
        """
        :function - left: function that implements the left arrow 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{self._url}/{key_map[KeyGroups.ARROW.value][ArrowKeys.LEFT.value]}'
        )
        return response
    
    def right(self) -> str:
        """
        :function - right: function that implements the right arrow 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ARROW.value][ArrowKeys.RIGHT.value]}'
        )
        return response
    
    def back(self) -> str:
        """
        :function - back: function that implements the back 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.BACK.value]}'
        )
        return response
    
    def ok(self) -> str:
        """
        :function - ok: function that implements the ok
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.OK.value] }'
        )
        return response
    
    def power(self)-> str:
        """
        :function - power: function that implements the power  
                           key for remote. Post call to the Roku Api
                           using ECP protocol (http).
                           This function first checks if the TV is on.
                           If it is, then user wishes to turn off tv, 
                           if it isn't, then user wishes to turn on tv.
        """
        # GET Device info
        response = requests.get(
            f'{ self._url }/query/device-info'
        )
        # Check if tv is currently on
        if 'PowerOn' in str(response.content):
            # if so turn off
            response = requests.post(
                f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.POWER_OFF.value]}'
            )
            return response
        # if tv is off user wants to turn on.
        elif 'Ready' in str(response.content):
            response = requests.post(
                f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.POWER_ON.value]}'
            )
            return response

        else: return None

    def home(self)-> str:
        """
        :function - home: function that implements the home 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.HOME.value]}'
        )
        return response

    def plus_volume(self) -> str:
        """
        :function - plus_volume: function that implements the increase volume 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.VOLUME_PLUS.value]}'
        )
        return response
    
    def minus_volume(self) -> str:
        """
        :function - minus_volume: function that implements the decrease volume 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.VOLUME_MINUS.value]}'
        )
        return response
    
    def mute(self) -> str:
        """
        :function - mute: function that implements the mute volume 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.MUTE.value]}'
        )
        return response

    def channel_up(self) -> str:
        """
        :function - channel_up: function that implements the channel up  
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.CHANNEL_UP.value]}'
        )
        return response
    def channel_down(self) -> str:
        """
        :function - channel_down: function that implements the channel down 
                          key for remote. Post call to the Roku Api
                          using ECP protocol (http).
        """
        response = requests.post(
            f'{ self._url }/{ key_map[KeyGroups.ACTIONS.value][ActionKeys.CHANNEL_DOWN.value]}'
        )
        return response


