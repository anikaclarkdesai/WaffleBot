from gpiozero import OutputDevice


class Motor:
    # init method setting up pins as forward backward etc 
    def __init__(self, pin1, pin2):
        # init method sets forward and backward values for the pin and its rotation 
        # Use BCM pin numbering (pin numbers like 24, 23 instead of board numbers)
        self.pin1 = OutputDevice(pin1, active_high=True, initial_value=False)
        self.pin2 = OutputDevice(pin2, active_high=True, initial_value=False)

        # time 7 seconds 
        # stop delay 2 seconds 
        # delay 7 seconds   

    def _clockwise(self):
        # clockwise rotation
        self.pin1.on()
        self.pin2.off()
    
    def _counterclockwise(self):
        # counterclockwise rotation
        self.pin1.off()
        self.pin2.on()

    def _stop(self):
        # stopping the motor from spinning
        self.pin1.off()
        self.pin2.off()

    def __del__(self):
        self._stop()
    
    # cleans up open pin output using destructor 


    





    
