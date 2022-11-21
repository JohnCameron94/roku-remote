import speech_recognition as s_r 
import pyaudio


class FindMicrophone(object):
    """
    :class FindMicrophone - class used to find microphone
    on the system this application is running on. The mic must
    be specified by name. If mic is not specified it will use the default 
    microphone that is within the list first. Must have channels or else 
    it is output device.
    """

    _index: int # Device index, pyaudio searches by index
    _p = pyaudio.PyAudio() # Instantiate PyAudio object

    # def __init__(self,name: str)-> None:
    #     """
    #     :construtor - Set's microphone name that the user is looking for
    #     """
    #     # Device name
    #     self._name = name


    def get_microphone(self)-> s_r.Microphone:
        """
        :method - get_microphone: Searches for the microphone within your system.
        :return - s_r Microphone:: returns the microphone if found or else returns IOError. 
        If the max channels of the device is 0 then method return OSError since device is most likely
        and output device.
        """
        # Search for Mic by name
        print(f'Searching for Microphone')
        index = None
        for i in range(self._p.get_device_count()):
            # If device is equal to specified name if found break out of loop
            if self._p.get_device_info_by_index(i)['maxInputChannels'] > 0 : 
                # Store in var
                dev = self._p.get_device_info_by_index(i)
                # set index
                index = i
                print(f"Found Microphone - Index:{index}, Name:{dev['name']}, Max Channels: { dev['maxInputChannels'] }")
                break
    
        
        # terminate PyAudio Instance
        self._p.terminate()
        # Return speach recognition microphone object.
        return s_r.Microphone(device_index=index)
