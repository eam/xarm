#!/usr/bin/python3

#from xarm.wrapper import XArmAPI
#print("hello, running")
#arm = XArmAPI.Controller('USB')

import xarm
import time

arm = xarm.Controller('USB')
print('Battery voltage in volts:', arm.getBatteryVoltage())

servo = xarm.Servo(1, 300)

print('servo ID:', servo.servo_id)
print('servo position:', servo.position)
print('servo angle:', servo.angle)

arm.setPosition(6, 0)
