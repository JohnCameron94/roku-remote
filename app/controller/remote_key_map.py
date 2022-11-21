
"""
:map - Map declared and corespond to the Enum classes declared 
       in remote_keys. This map, maps the enum values to the 
       api endpoint our request must hit in order to perform
       the wanted behavior on the tv screen.
"""
key_map = {
    'arrow_keys' : {
        'down': 'keypress/down',
        'up': 'keypress/up',
        'left': 'keypress/left',
        'right': 'keypress/right',
    },
    'actions':{
        'back': 'keypress/back',
        'ok': 'keypress/select',
        'poweroff':'keypress/poweroff',
        'poweron':'keypress/poweron',
        'home':'keypress/home',
        'v+': 'keypress/volumeup',
        'v-': 'keypress/volumedown',
        'mute': 'keypress/volumemute',
        'channelup':'keypress/channelup',
        'channeldown': 'keypress/channeldown',
    }
}