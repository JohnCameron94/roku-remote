
def RokuDeviceNotFound(Exception):

    def __init__(self,message="Roku Device Not Found on Local Network...."):
        self.message = message
        super().__init__(self.message)