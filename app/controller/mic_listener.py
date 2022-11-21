import speech_recognition as s_r 

class Listener(object):
    """
    :class Listener - Listens from the specified microphone
    and translate the speech into text.
    """
    # Reconizer from speech recognition library
    _r = s_r.Recognizer()
    
    def __init__(self, mic: s_r.Microphone) -> None:
        # Device from FindMicrophone
        self._device = mic 


    
    def listen(self) -> str:
        # Listen Microphone speach input
        with self._device as source:
            # adjust for the background noise
            self._r.adjust_for_ambient_noise(source)
            # listen through mic
            audio = self._r.listen(source)
        try:
            # Translate speach using google speach recognition api
            return self._r.recognize_google(audio,language="en-EN")
        except s_r.UnkownValueError:
            # If google can't recognize speach
            raise s_r.UnkownValueError