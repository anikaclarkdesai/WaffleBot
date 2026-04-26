from motor_class import Motor
import time 


motor1 = Motor(1,2) 
# insert the pin numbers as connected 

motor1.clockwise() 
# turns motor clockwise 


time.sleep(7) 
# 7 second delay

motor1.anticlockwise()
# turns other way

time.sleep(3) 

motor1.clockwise() 

# clockwise again

time.sleep(3)

motor1.stop() 
# now the motor stops 








