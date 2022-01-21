# DFRobot_MICS
- [中文版](./README_CN.md)

This is a 3.3/5V compatible MEMS gas concentration sensor from DFRobot. This sensor supports the detection of various gas concentrations like CO, C2H5OH (Alcohol), H2, NO2, NH3, and integrates various gas concentration conversion formulas in the code to facilitate the testing and use of sensors. With I2C output and 3.3~5.5V wide voltage input, it is compatible with Arduino, ESP32, Raspberry Pi and other mainstream controllers.<br>

![效果图](../../resources/images/SEN0377.jpg)

## Product Link(https://www.dfrobot.com/product-2417.html)

    SKU:SEN0377

## Table of Contents

* [Summary](#Summary)
* [Installation](#Installation)
* [Methods](#Methods)
* [Compatibility](#Compatibility)
* [History](#History)
* [Credits](#Credits)

## Summary

- Detection of Physical Quantities: gas concentration of CO,C2H5OH(Alcohol), H2, NO2, NH3, CH4<br>
- Operating Voltage: 3.3～5.5V DC<br>
- Power Dissipation: 0.45W(5V)<br>
- Output Signal: I2C(0~3V)<br>
- Measuring Range:<br>
1 – 1000ppm(Carbon monoxide CO )<br>
0.05 – 10ppm(Nitrogen dioxide NO2 )<br>
10 – 500ppm( Ethanol C2H5OH )<br>
1 – 1000ppm(Hydrogen H2)<br>
1 – 500ppm(Ammonia NH3 )<br>
1000 - ∞ ppm(Methane CH4 )<br>
- Working Temperature: -30～85℃<br>
- Working Humidity: 5～95%RH (No condensation)<br>
- Storage Temperature: -40~85℃<br>
- Lifespan: >2 years (in the air)<br>
- Circuit Board Size: 27mm*37mm<br>
- Mounting Hole Size: inner diameter 3.1mm/outer diameter 6mm<br>

## Installation
Download the library file before use, paste it into the custom directory for Raspberry Pi, then open the examples folder and run the demo in the folder.

## Methods

```python
  '''!
    @brief sleep sensor
  '''
  def sleep_mode(self):
  
  '''!
    @brief wake up sensor
  '''
  def wakeup_mode(self):

  '''!
    @breif get power mode
    @return mode SLEEP_MODE or WAKEUP_MODE
  '''
  def get_power_mode(self):
  
  '''!
    @brief Waiting time for warm-up
    @param minute Units of minutes
  '''
  def warm_up_time(self, minute):
  
  '''!
    @brief get ADC data
    @param mode OX_MODE or RED_MODE
    @return adc data
  '''
  def get_adc_data(self, mode):
  
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
  def get_gas_ppm(self, gas_type):
  
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
  def get_gas_exist(self, gas_type):
```

## Compatibility

* RaspberryPi Version

| Board        | Work Well | Work Wrong | Untested | Remarks |
| ------------ | :-------: | :--------: | :------: | ------- |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |     √     |            |          |         |
| RaspberryPi4 |           |            |    √     |         |

* Python Version

| Python  | Work Well | Work Wrong | Untested | Remarks |
| ------- | :-------: | :--------: | :------: | ------- |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |


## History

- 2021/1/13 - V1.0.0 Version
- 2021/4/20 - V1.1.0 Version
- 2021/7/18 - V1.2.0 Version

## Credits

Written by ZhixinLiu(zhixin.liu@dfrobot.com), 2020. (Welcome to our [website](https://www.dfrobot.com/))
