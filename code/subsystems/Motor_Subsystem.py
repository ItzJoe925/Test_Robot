import logging
log = logging.Logger('P212-robot')
import wpilib
import commands2 
import phoenix6
import wpimath.controller
import wpimath.trajectory

from constants import ELEC

class MotorSubsystemClass(commands2.Subsystem):

    def __init__(self) -> None:

        self.my_motor = phoenix6.hardware.TalonFX(ELEC.my_motor_CAN_ID)
        #self.my_motor.setNeutralMode(self.brakemode)

    def go_forward(self):
        self.my_motor.setNeutralMode(self.brakemode)
    
    def goReverse(self):
        self.my_motor.set(ELEC.my_motor_reverse)
        
    def stop(self):
        self.my_motor.set(ELEC.my_motor_reverse)
   