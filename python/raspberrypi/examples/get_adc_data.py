# -*- coding:utf-8 -*-
'''!
  @file get_mics_adc_data.py
  @brief Read sensor red and ox adc.
  @n step: we must first determine the i2c device address, will dial the code switch A0, A1 (MICS_ADDRESS_0 for [0 0]), (MICS_ADDRESS_1 for [1 0]), (MICS_ADDRESS_2 for [0 1]), (MICS_ADDRESS_3 for [1 1]).
  @copyright Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license The MIT License (MIT)
  @author [ZhixinLiu](zhixin.liu@dfrobot.com)
  @version V1.2
  @date 2021-6-18
  @url https://github.com/DFRobot/DFRobot_MICS
'''

import sys
import os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
sys.path.append("../")
from DFRobot_MICS import *

CALIBRATION_TIME = 0x03            # calibration time
I2C_BUS          = 0x01            # default use I2C1
'''
   The first  parameter is to select i2c0 or i2c1
   The second parameter is the i2c device address
   The default address for i2c is MICS_ADDRESS_0
     MICS_ADDRESS_0              0x75
     MICS_ADDRESS_1              0x76
     MICS_ADDRESS_2              0x77
     MICS_ADDRESS_3              0x78
'''
mics = DFRobot_MICS_I2C (I2C_BUS ,MICS_ADDRESS_0)

def setup():
  '''
    Gets the power mode of the sensor
    The sensor is in sleep mode when power is on,so it needs to wake up the sensor. 
    The data obtained in sleep mode is wrong
  '''
  if mics.get_power_mode() == SLEEP_MODE:
    mics.wakeup_mode()
    print("wake up sensor success")
  else:
    print("the sensor is wake up mode")

def loop():
  '''
    read sensor adc data
      OX_MODE  0x00
      RED_MODE 0x01
  '''
  ox_data = mics.get_adc_data(OX_MODE)
  #red_data = mics.get_adc_data(RED_MODE);
  print ("ox adc is %d"%ox_data)
  #print ("red adc is %d"%red_data)
  time.sleep(1)
  #mics.sleep_mode()

if __name__ == "__main__":
  setup()
  while True:
    loop()