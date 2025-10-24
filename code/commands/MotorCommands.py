import logging
logger = logging.getLogger("motorsubsystemlogger")



import commands2
import constants
from constants import OP



from subsystems.Motor_Subsystem import MotorSubsystemClass



class ForwardSpin(commands2.Command):

    def __init__(self, motorsubsystem: MotorSubsystemClass) -> None:
       
        self.motorsub = motorsubsystem


    def initialize(self):
        self.motorsub.go_forward()
        logger.info("Forward Command Initialized")



   # def execute(self):
        
        #self.motorsub.go_forward
        #logger.info("Forward Command Initialized")

    def isFinished(self):
     
        return True

    #def end(self, interrupted: bool):

        #self.motorsub.stop()


    class ReverseSpin(commands2.Command):
            
            def __init__(self, motorsubsystem: MotorSubsystemClass) -> None:

                #self.addRequirements(self.Motor_ss)
                self.motorsub = motorsubsystem

            def initialize(self):
                 self.motorsub.go_reverse()
            logger.info("Reverse Comand Initialized")
            
            
            #def execute(self):

                #self.motorsub.stop
                #logger.info("Stop Command Running")

            def isFinished(self):
                 
                 return True
            
            
    #def end(self, interrupted: bool):

        #self.motorsub.stop()

class  StopSpin(commands2.Command):

    def __init__(self, motorsubsystem: MotorSubsystemClass) -> None:

        #self.addRequirements(self.Motor_ss)
        self.motorsub = motorsubsystem

    def initialize(self):
        self.motorsub.stop()
        logger.info("Stop Command Initialized")

    #def execute(self):
        #self.motorsub.stop
        #logger.info("Stop Command Running")
    
    def isFinished (self):
        
        return True




