# DFRobot mics concentration sensor

This RaspberryPi mics sensor board can communicate with RaspberryPi via I2C.<br>
mics sensor Long service life.<br>

## DFRobot mics Library for RaspberryPi

Provide the Raspberry Pi library for the DFRobot_micsSensor module.

## Table of Contents

* [Summary](#summary)
* [Feature](#feature)
* [Installation](#installation)
* [Methods](#methods)
* [History](#history)
* [Credits](#credits)

## Summary

mics module.

## Feature

1. The module has two modes, one is active data acquisition and the other is passive data acquisition. <br>
2. You can measure the concentration of (co no no2 h2 ch4 c2h5oh) in the air. <br>

## Installation

This Sensor should work with DFRobot_NicsSensor on RaspberryPi. <br>
Run the program:

```
$> python get_gas_exist.py
$> python get_gas_ppm.py
$> python get_adc_data.py
$> python enable_power.py
```

## Methods

```py

  '''
    @brief sleep sensor
  '''
  def sleep_mode(self):

  '''
    @brief wake up sensor
  '''
  def wakeup_mode(self):

  '''
    @breif get power mode
    @return mode
              SLEEP_MODE
              WAKEUP_MODE
  '''
  def get_power_mode(self):

  '''
    @brief Waiting time for warm-up
    @param minute Units of minutes
  '''
  def warm_up_time(self, minute):

  '''
    @brief get ADC data
    @param mode OX_MODE or RED_MODE
    @return adc data
  '''
  def get_adc_data(self, mode):

  '''
    @brief get the gas data, units of PPM
    @param gas_type is gas type
    @return gas concentration, (units PPM)
  '''
  def get_gas_ppm(self, gas_type):

  '''
    @brief Detect the presence of gas
    @param gas_type is gas type
    @return Whether gas is present
  '''
  def get_gas_exist(self, gas_type):
```
## History

- January 13, 2021 - Version 1.0 released.
- April   20, 2021 - Version 1.1 released.  add breakout version
- June    18, 2021 - Version 1.2 released.  add demo and Modify comments

## Credits

Written by ZhixinLiu(zhixin.liu@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))