from motor_class import Motor
import Gmail_API
from Gmail_API import checkMail as CM
from Gmail_API import get_contents as gc
from Gmail_API import send_email_gmail
import time

#physical pins are not in motor class but are
# BCM pins 11 and 8 are used for the motor
motor1 = Motor(8,11 )

#boolean to track if the door is closed or not, starts as closed
closed = True

def testMotor():
    print("Testing motor clockwise...")
    motor1.clockwise()
    time.sleep(3)
    
    motor1.stop()
    


def Rotation():
    global closed

    while True:
        contents = CM()  # ✅ this already waits for a new email

        if not contents:
            print("No content received.")
            continue

        contents = contents.strip().lower()
       # print(f"[DEBUG] Command received: {repr(contents)}")

        #if you email 'open' door will ONLY open
        if contents == "open" and closed:
            print("Clockwise")
            
            #runs the motor clockwise for 7 seconds to open the door  
            motor1.clockwise()
            time.sleep(7)
            
            motor1.stop()
            #sets the door to open
            closed = False
            
        #if you email 'close' door will ONLY close
        elif contents == "close" and not closed:
            print("Counterclockwise")
            
            #runs the motor counterclockwise for 5 seconds to close the door
            motor1.counterclockwise()
            time.sleep(7)
            
            motor1.stop()
            #sets the door to closed
            closed = True
            
        #if you email 'waffle time' door will open, pause for 5 seconds, and close
        elif contents == "waffle time" and closed:
           
            print("Waffle Time! Opening door...")
            
            #runs the motor clockwise for 7 seconds to open the door  
            motor1.clockwise()
            time.sleep(3)
            print("Door is open! Waiting 5 seconds before closing...")
            
            #stops the motor and rests
            motor1.stop()
            time.sleep(5)
            
            print("Closing door...")
            #runs the motor counterclockwise for 5 seconds to close the door
            motor1.counterclockwise()
            time.sleep(5)
            
            #stops the motor
            motor1.stop()
            print("Cycle Complete!")
        
            #sets the door to closed
            closed = True       
        
        else:
            print("Invalid message received.")
               # ⚠️ You no longer have access to sender here
            print(f"[DEBUG] Received command: {repr(contents)}")
    
    
Rotation()

#testMotor()   






