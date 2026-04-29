from motor_class import Motor
import time 


motor1 = Motor(23,24) 
# insert the pin numbers as connected 
# change this based on the pins we use 

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








