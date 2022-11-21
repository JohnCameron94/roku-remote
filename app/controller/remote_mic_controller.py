import speech_recognition as s_r
import pyaudio
from controller.find_microphone import FindMicrophone
from controller.mic_listener import Listener


class RemoteMicrophoneController(object):
    _listening : bool
    _clicks = 0
    _mic: s_r.Microphone


    def __init__(self) -> None:

        self._listening = True


    def stop_listening()-> None:
        self._listening = False

    def _evaluate_text(self, text: str, controller) -> bool:
        if text.lower() == 'volume up':
            controller.plus_volume()
            return True
        elif text.lower() == 'volume down':
            controller.minus_volume()
            return True
        else: return False


    def run(self, controller):
        """
        method: Run - runs the backend speech recognition server by 
        searching for the specified device in the command line 
        arguments. 
        """
        # Get Device
        try:
            mic = FindMicrophone().get_microphone()
        
        # Can't find device
        except IOError as ioerr:
            IOError('Device Not Found! - StackTrace :', ioerr)
        # Device has no channels, could be output device
        except OSError as oserr:
            OSError('Error, Not enough Channels - StackTrace:', oserr)

        # Run Server
        server = Listener(mic)

        cmd = True
        # Until user says "Exit" continue running
        while cmd:
            # Speech recognition string
            text = server.listen()
            cmd = self._evaluate_text(text, controller)