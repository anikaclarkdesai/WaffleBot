from motor_class import Motor
import time 


motor1 = Motor(16, 18)
# Use BCM pin numbers (not board numbers)
# Change these based on your physical wiring 

motor1._clockwise() 
# turns motor clockwise 



time.sleep(7) 
# 7 second delay

motor1._counterclockwise()
# turns other way

time.sleep(5) 

motor1._clockwise() 

# clockwise again

time.sleep(10)
# 10 second delay

motor1._stop() 
# now the motor stops 








