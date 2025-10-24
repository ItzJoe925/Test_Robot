import logging
log = logging.Logger('P212-robot')

from wpilib import DigitalInput
import commands2
from constants import ELEC
import phoenix6


class MotorSubsystem(commands2.Subsystem):
    """
   This is the subsystem for the MOTORS
    """
    def __init__(self) -> None:
        """Creates a new ExampleSubsystem"""
        super().__init__()
        # Create sensors here, and assign them to instance variables.
        # (Define the DIO port or CAN bus ID that your sensor uses in
        #  constants.py)


        # Create actuators here, and assign them to instance variables.
        # (Define the DIO port or CAN bus ID that your actuator uses in
        #  constants.py)

        ## TODO: Change this for your robot!
        ##       (Use your actuators and constants; change the variable name.)
        self.my_motor = phoenix6.hardware.TalonFX(
            ELEC.my_motor_CAN_ID,
            ) 
 

    def stop(self):
        """
        Example method that stops everything on the robot
        """
        self.my_motor.set(0.0)

    def go_forward(self): 
        self.my_motor.set(ELEC.my_motor_speed)

    def go_reverse(self): 
        self.my_motor.set(ELEC.my_motor_speed_reverse)
        