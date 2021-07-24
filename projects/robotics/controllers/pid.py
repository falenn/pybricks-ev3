'''PID Class'''
class PID:
    ''' PID controller'''

    # while (drive=true)
    #   do 
    #      drive forward with line to the left of the sensor
    #      turning slightly to the left
    #    until
    #      line is detected
    #   turn to the right
    #// loop

    #  
    #  PID=(target-value)kp+(integral+error)ki+(error-last_error)kd
    #  Target = ColorSensor value for black (line color)
    #  value = current ColorSensor value 
    #  kp,ki,kd = tuning constants
    #  PID = p_gain + i_gain + d_gain

    def __init__(self, target, kp, ki, kd, direction):

        self.integral=0 # sum of error for integral gain
        self.direction=direction # 1 on left side of line,-1 on right side
        self.last_error=0 #error calculated from last loop for d_gain

        # target sensor input for Pid to control
        self.target = target
        # Tuning for PID
        self._kp = kp
        self._ki = ki
        self._kd = kd

    def displayTuning(self):
        print("kp: ", self._kp ,"ki: ", self._ki, "kd: ", self._kd)

    def displayStatus(self):
        print("integral: ", self.integral, "lastError: ", self.last_error)
    
    def updateTarget(self,target):
        self.target = target

    # Ensures value is between -100 and 100
    def limit(self,value):
        return min(max(value,-100),100)
        
    #compute the error
    def error(self,current):
        return self.target - current

    # Calculate proportional gain - proportion cares for the present!
    def p_gain(self,error):
        return (error)*self._kp

    # Calculate integral gain - integral cares for the past!
    def i_gain(self,error):
        integral=self.integral+(error*self._ki)
        return integral

    # Calculate derivative gain - derivative cares for the future!
    def d_gain(self,error):
        return(error*self._kd - self.last_error)

    # Reset the integral
    def reset_i_gain(self):
        self.integral=0

    def calc(self, current):
        error = self.error(current)
        return self.p_gain(error) + self.i_gain(error) + self.d_gain(error)





