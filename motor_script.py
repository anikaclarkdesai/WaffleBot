from motor_class import Motor
import time 


motor1 = Motor(1,2) 
# insert the pin numbers as connected 

motor1._clockwise() 
# turns motor clockwise 


time.sleep(7) 
# 7 second delay

motor1._anticlockwise()
# turns other way

time.sleep(3) 

motor1._clockwise() 

# clockwise again

time.sleep(3)

motor1._stop() 
# now the motor stops 








