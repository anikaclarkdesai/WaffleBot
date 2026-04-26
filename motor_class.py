import RPi.GPIO as GPIO 

class Motor:
     # init method setting up pins as forward backward etc 
    def __init__(self,pin1,pin2): 
        # init method sets forward and backward values for the pin and its rotation 
        self.pin1= pin1
        self.pin2 = pin2
        # setmode sets up the sequence of pins and numbers them
        GPIO.setmode(GPIO.BOARD)
        
        # setting up GPIO pins as output 
        GPIO.setup(self.pin1,GPIO.OUT)
        GPIO.setup(self.pin2,GPIO.OUT)
        

        # time 7 seconds 
        # stop delay 2 seconds 
        # delay 7 seconds   


    
    def _del(self): 

        GPIO.cleanup()
    
    #cleans up open pin output using destructor 

    def _clockwise(self): 
        # clockwise rotation
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
    
    def _counterclockwise(self): 
        # counterclock wise rotation
        GPIO.output(self.pin1, GPIO.LOW)
        GPIO.output(self.pin2, GPIO.HIGH)

    
    def _stop(self): 
        # stopping the motor from spinning
        GPIO.output(self.pin1,GPIO.LOW)
        GPIO.output(self.pin2,GPIO.LOW)

        
    

    





    