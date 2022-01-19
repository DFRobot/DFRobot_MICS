# -*- coding: utf-8 -*
'''!
  @file DFRobot_MICS.py
  @brief DFRobot_MICS Class infrastructure, implementation of underlying methods
  @copyright Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license The MIT License (MIT)
  @author [ZhixinLiu](zhixin.liu@dfrobot.com)
  @version V1.2
  @date 2020-09-09
  @url https://github.com/DFRobot/DFRobot_MICS
'''
import serial
import time
import smbus

MICS_ADDRESS_0            = 0x75
MICS_ADDRESS_1            = 0x76
MICS_ADDRESS_2            = 0x77
MICS_ADDRESS_3            = 0x78

ERROR                     = -1.0
OX_MODE                   = 0x00
RED_MODE                  = 0x01

OX_REGISTER_HIGH          = 0x04
OX_REGISTER_LOW           = 0x05
RED_REGISTER_HIGH         = 0x06
RED_REGISTER_LOW          = 0x07
POWER_REGISTER_HIGH       = 0x08
POWER_REGISTER_LOW        = 0x09
POWER_REGISTER_MODE       = 0x0a

SLEEP_MODE                = 0x00
WAKEUP_MODE               = 0x01

## Carbon Monoxide
CO                        = 0x01
## Methane
CH4                       = 0x02
## Ethanol
C2H5OH                    = 0x03
## Propane
C3H8                      = 0x04
## Iso Butane
C4H10                     = 0x05
## Hydrogen
H2                        = 0x06
## Hydrothion
H2S                       = 0x07
## Ammonia
NH3                       = 0x08
## Nitric Oxide
NO                        = 0x09
## Nitrogen Dioxide
NO2                       = 0x0a
  
class DFRobot_MICS(object):
  ## mode flag
  __m_flag   = 0
  ## acquisition count
  __count    = 0
  ## i2c send buffer
  __txbuf        = [0]
  ## alcohol data
  __alcoholdata  = [0]*101
  __uart_i2c     =  0
  __r0_ox        =  1.0
  __r0_red       =  1.0
  def __init__(self, bus):
    self.i2cbus = smbus.SMBus(bus)

  def sleep_mode(self):
    '''!
      @brief sleep sensor
    '''
    rslt = [0]*1
    rslt[0] = SLEEP_MODE
    self.write_reg(POWER_REGISTER_MODE, rslt)

  def wakeup_mode(self):
    '''!
      @brief wake up sensor
    '''
    rslt = [0]*1
    rslt[0] = WAKEUP_MODE
    self.write_reg(POWER_REGISTER_MODE, rslt)

  def get_power_mode(self):
    '''!
      @breif get power mode
      @return mode SLEEP_MODE or WAKEUP_MODE
    '''
    rslt = self.read_reg(POWER_REGISTER_MODE, 1)
    return rslt[0]

  def warm_up_time(self, minute):
    '''!
      @brief Waiting time for warm-up
      @param minute Units of minutes
    '''
    second = minute*60
    print("Start calibration Sensor!")
    while (second):
      second = second - 1
      time.sleep(1)
      print("Please wait calibration!")
    for i in range(10):
      rslt = self.get_mics_data()
      self.__r0_ox  = self.__r0_ox  + rslt[0]
      self.__r0_red = self.__r0_red + rslt[1]
      time.sleep(1)
      print("Please wait calibration!")
    self.__r0_ox  = (int)(self.__r0_ox  / 10)
    self.__r0_red = (int)(self.__r0_red / 10)
    print("calibration success!")

  def get_adc_data(self, mode):
    '''!
      @brief get ADC data
      @param mode OX_MODE or RED_MODE
      @return adc data
    '''
    rslt = self.get_mics_data()
    if mode ==  OX_MODE:
      return rslt[0]
    elif mode == RED_MODE:
      return rslt[1]
    else:
      return ERROR
  
  def get_gas_ppm(self, gas_type):
    '''!
      @brief get the gas data, units of PPM
      @param gas_type is gas type
      @param CO        0x01  (Carbon Monoxide)
      @param CH4       0x02  (Methane)
      @param C2H5OH    0x03  (Ethanol)
      @param H2        0x06  (Hydrogen)
      @param NH3       0x08  (Ammonia)
      @param NO2       0x0A  (Nitrogen Dioxide)
      @return gas concentration, (units PPM)
    '''
    rslt = self.get_mics_data()
    rs_r0_red_data = rslt[1]
    rs_r0_red_data = float(rs_r0_red_data) / float(self.__r0_red)
    rs_ro_ox_data  = rslt[0]
    rs_ro_ox_data  = float(rs_ro_ox_data) / float(self.__r0_ox)
    if gas_type ==  CO:
      return self.getCarbonMonoxide(rs_r0_red_data)
    elif gas_type == CH4:
      return self.getMethane(rs_r0_red_data)
    elif gas_type == C2H5OH:
      return self.getEthanol(rs_r0_red_data)
    elif gas_type == H2:
      return self.getHydrogen(rs_r0_red_data)
    elif gas_type == NH3:
      return self.getAmmonia(rs_r0_red_data)
    elif gas_type == NO2:
      return self.getNitrogenDioxide(rs_ro_ox_data)
    else:
      return ERROR

  def get_gas_exist(self, gas_type):
    '''!
      @brief Detect the presence of gas
      @param gas_type is gas type
      @param CO        0x01  (Carbon Monoxide)
      @param CH4       0x02  (Methane)
      @param C2H5OH    0x03  (Ethanol)
      @param C3H8      0x04  (Propane)
      @param C4H10     0x05  (Iso Butane)
      @param H2        0x06  (Hydrogen)
      @param H2S       0x07  (Hydrothion)
      @param NH3       0x08  (Ammonia)
      @param NO        0x09  (Nitric Oxide)
      @param NO2       0x0A  (Nitrogen Dioxide)
      @return Whether gas is present
    '''
    rslt = self.get_mics_data()
    rs_r0_red_data = rslt[1]
    rs_r0_red_data = float(rs_r0_red_data) / float(self.__r0_red)
    rs_ro_ox_data  = rslt[0]
    rs_ro_ox_data  = float(rs_ro_ox_data) / float(self.__r0_ox)
    if gas_type == CO:
      return self.existCarbonMonoxide(rs_r0_red_data)
    elif gas_type == CH4:
      return self.existMethane(rs_r0_red_data)
    elif gas_type == C2H5OH:
      return self.existEthanol(rs_r0_red_data)
    elif gas_type == C3H8:
      return self.existPropane(rs_r0_red_data)
    elif gas_type == C4H10:
      return self.existIsoButane(rs_r0_red_data)
    elif gas_type == H2:
      return self.existHydrogen(rs_r0_red_data)
    elif gas_type == H2S:
      return self.existHydrothion(rs_r0_red_data)
    elif gas_type == NH3:
      return self.existAmmonia(rs_r0_red_data)
    elif gas_type == NO:
      return self.existNitricOxide(rs_ro_ox_data)
    elif gas_type == NO2:
      return self.existNitrogenDioxide(rs_ro_ox_data)
    else:
      return ERROR

  def get_mics_data(self):
    '''!
      @brief get sensor adc data
      @return ox register red register power register
    '''
    rslt = self.read_reg(OX_REGISTER_HIGH, 6)
    oxdata = rslt[0]*256 + rslt[1]
    reddata = rslt[2]*256 + rslt[3]
    powerdata = rslt[4]*256 + rslt[5]
    if (powerdata - oxdata) <= 0:
      rslt[0] = 0
    else:
      rslt[0] = powerdata - oxdata
    if (powerdata - reddata) < 0:
      rslt[1] = 0
    else:
      rslt[1] = powerdata - reddata
    rslt[2] = powerdata
    return rslt

  def getCarbonMonoxide(self, data):
    if data > 0.425:
      return 0.0
    co = (0.425 - data) / 0.000405
    if co > 1000.0:
      return 1000.0
    if co < 1.0:
      return 0.0
    return co

  def getMethane(self, data):
    if data > 0.786:
      return 0.0
    methane = (0.786 - data) / 0.000023
    if methane > 25000.0:
      return 25000.0
    if methane < 1000.0:
      return 0.0
    return methane

  def getEthanol(self, data):
    if data > 0.306:
      return 0.0
    ethanol = (0.306 - data) / 0.00057
    if ethanol > 500.0:
      return 500.0
    if ethanol < 10.0:
      return 0.0
    return ethanol

  def getHydrogen(self, data):
    if data > 0.279:
      return 0.0
    hydrogen = (0.279 - data) / 0.00026
    if hydrogen > 1000.0:
      return 1000.0
    if hydrogen < 1.0:
      return 0.0
    return hydrogen

  def getAmmonia(self, data):
    if data > 0.8:
      return 0.0
    ammonia = (0.8 - data) / 0.0015
    if ammonia > 500.0:
      return 500.0
    if ammonia < 10.0:
      return 0.0
    return ammonia

  def getNitrogenDioxide(self, data):
    if data < 1.1:
      return 0.0
    nitrogendioxide = (data - 0.045) / 6.13
    if nitrogendioxide > 10.0:
      return 10.0
    if nitrogendioxide < 0.1:
      return 0.0
    return nitrogendioxide

  def existPropane(self, data):
    if data > 0.18:
      return -1
    else:
      return 1

  def existNitricOxide(self, data):
    if data > 0.8:
      return -1
    else:
      return 1

  def existIsoButane(self, data):
    if data > 0.65:
      return -1
    else:
      return 1

  def existHydrothion(self, data):
    if data > 0.58 and data < 0.69:
      return 1
    if data < 0.201:
      return 1
    return -1

  def existCarbonMonoxide(self, data):
    if data > 0.425:
      return -1
    else:
      return 1

  def existMethane(self, data):
    if data > 0.786:
      return -1
    else:
      return 1

  def existEthanol(self, data):
    if data > 0.306:
      return -1
    else:
      return 1

  def existHydrogen(self, data):
    if data > 0.279:
      return -1
    else:
      return 1

  def existAmmonia(self, data):
    if data > 0.8:
      return -1
    else:
      return 1

  def existNitrogenDioxide(self, data):
    if data < 1.1:
      return -1
    else:
      return 1

class DFRobot_MICS_I2C(DFRobot_MICS): 
  def __init__(self, bus, addr):
    self.__addr = addr;
    super(DFRobot_MICS_I2C, self).__init__(bus)

  def write_reg(self, reg, data):
    while 1:
      try:
        self.i2cbus.write_i2c_block_data(self.__addr, reg, data)
        return
      except:
        print("please check connect!")
        time.sleep(1)

  def read_reg(self, reg, len):
    while 1:
      try:
        rslt = self.i2cbus.read_i2c_block_data(self.__addr, reg, len)
        return rslt
      except:
        print("please check connect!")
        time.sleep(1)