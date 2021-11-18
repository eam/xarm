#!/usr/bin/python3

import xarm

arm = xarm.Controller('USB')
print('Battery voltage in volts:', arm.getBatteryVoltage())

arm.setPosition(1, 500)
arm.setPosition(2, 500)
arm.setPosition(3, 500)
arm.setPosition(4, 500)
arm.setPosition(5, 500)
arm.setPosition(6, 500)
