# DFRobot_MICS

DFRobot's MICS

![]

## DFRobot_MICS
---------------------------------------------------------
DFRobot_MICS

## 产品链接（https://www.dfrobot.com/）
    SKU：SEN0377 SEN0440 SEN0441
rouge
## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)
<snippet>
<content>

## Summary

## Installation

To use this library download the zip file, uncompress it to a folder named DFRobot_MICS.
Download the zip file first to use this library and uncompress it to a folder named DFRobot_MICS.

## Methods

```C++
  /*!
   *  @brief Waiting time for warm-up
   *  @param minute Units of minutes
   *  @return true  is warm-up success
   *          false is wait warm-up
   */
  bool warmUpTime(uint8_t minute);

  /*!
   *  @brief Read sensor ADC data
   *  @param mode:
   *           OX_MODE
   *           RED_MODE
   *  @return adcValue (0-1024)
   */
  int16_t getADCData(uint8_t mode);

  /**!
   *  @brief Read the concentration of the gas
   *  @param type:
   *    Methane          (CH4)    (1000 - 25000)PPM
   *    Ethanol          (C2H5OH) (10   - 500)PPM
   *    Hydrogen         (H2)     (1    - 1000)PPM
   *    Ammonia          (NH3)    (1    - 500)PPM
   *    Carbon Monoxide  (CO)     (1    - 1000)PPM
   *    Nitrogen Dioxide (NO2)    (0.1  - 10)PPM
   *  @return concentration Units of PPM
   */
  float getGasData(uint8_t type);

  /**!
   *  @brief Read whether the gas is present
   *  @param gas:
   *    CO       = 0x01  (Carbon Monoxide)
   *    CH4      = 0x02  (Methane)
   *    C2H5OH   = 0x03  (Ethanol)
   *    C3H8     = 0x04  (Propane)
   *    C4H10    = 0x05  (Iso Butane)
   *    H2       = 0x06  (Hydrogen)
   *    H2S      = 0x07  (Hydrothion)
   *    NH3      = 0x08  (Ammonia)
   *    NO       = 0x09  (Nitric Oxide)
   *    NO2      = 0x0A  (Nitrogen Dioxide)
   *  @return state
   *            NO_EXIST
   *            EXIST
   */
  int8_t getGasExist(uint8_t gas);

  /**!
   *  @brief Sleep sensor
   */
  void sleepMode(void);

  /**!
   *  @brief wakeup sensor
   */
  void wakeUpMode(void);

  /**!
   *  @brief Gets the power mode of the sensor
   *  @return mode
   *            SLEEP_MODE
   *            WAKE_UP_MODE
   */
  uint8_t getPowerState(void);

```

## Compatibility

| MCU                | Work Well | Work Wrong | Untested | Remarks |
| ------------------ | :-------: | :--------: | :------: | ------- |
| Arduino uno        |     √     |            |          |         |
| FireBeetle esp32   |     √     |            |          |         |
| FireBeetle esp8266 |     √     |            |          |         |
| FireBeetle m0      |     √     |            |          |         |
| Leonardo           |     √     |            |          |         |
| Microbit           |     √     |            |          |         |
| Arduino MEGA2560   |     √     |            |          |         |

## History

- January 13, 2021 - Version 1.0 released.
- April   20, 2021 - Version 1.1 released.  add breakout version
- June    18, 2021 - Version 1.2 released.  add demo and Modify comments

## Credits

Written by ZhixinLiu(zhixin.liu@dfrobot.com), 2021. (Welcome to our [website](https://www.dfrobot.com/))