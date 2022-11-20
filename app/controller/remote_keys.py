from enum import Enum


class ArrowKeys(Enum):
    """
    :class - ArrowKeys inherits from Enum. This Enum class
             is used to map to the endpoint of your roku device
             EX: /down 
    """
    DOWN = 'down'
    UP = 'up'
    LEFT = 'left'
    RIGHT = 'right'

class ActionKeys(Enum):
    """
    :class - ActionKeys inherits from Enum. This class
             uses the same concept as ArrowKeys, but these keys
             I called actions keys since they keys that perform
             actions rather then moving around the TV screen
    """
    BACK = 'back'
    OK='ok'
    POWER_OFF='poweroff'
    POWER_ON='poweron'
    HOME='home'
    VOLUME_PLUS='v+'
    VOLUME_MINUS='v-'
    MUTE='mute'
    CHANNEL_UP='channelup'
    CHANNEL_DOWN='channeldown'

class KeyGroups (Enum):
    """
    :class KeyGroups is a Enum that groups both
           key type. It is intepreted that arrow keys
           are used to move the cursor arround the tv menu, rather
           then perform an action such as select or go back to home.
    """
    ARROW = 'arrow_keys'
    ACTIONS = 'actions'
    