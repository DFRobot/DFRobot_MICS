 /*!
  * @file  enablePower.ino
  * @brief Enable the power, and the information is printed on the serial port.
  * @n When using IIC device, select I2C address, set the dialing switch A0, A1 (Address_0 is [0 0]), (Address_1 is [1 0]), (Address_2 is [0 1]), (Address_3 is [1 1]).
  * @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  * @licence     The MIT License (MIT)
  * @author      ZhixinLiu(zhixin.liu@dfrobot.com)
  * @version     V1.2
  * @date        2021-06-18
  * @get         from https://www.dfrobot.com
  * @url         https://github.com/dfrobot/DFRobot_MICS
  */
#include "DFRobot_MICS.h"

#define CALIBRATION_TIME   3                      // Default calibration time is three minutes

// When using I2C communication, use the following program to construct an object by DFRobot_MICS_I2C
/**!
    iic slave Address, The default is ADDRESS_0
       ADDRESS_0               0x75             // i2c device address
       ADDRESS_1               0x76
       ADDRESS_2               0x77
       ADDRESS_3               0x78
*/
#define Mics_I2C_ADDRESS ADDRESS_0
DFRobot_MICS_I2C mics(&Wire, Mics_I2C_ADDRESS);

void setup() 
{
  Serial.begin(115200);
  while(!Serial);
  while(!mics.begin()){
    Serial.println("NO Deivces !");
    delay(1000);
  } Serial.println("Device connected successfully !");
}

void loop() 
{
  /**!
    Gets the power mode of the sensor
    The sensor is in sleep mode when power is on,so it needs to wake up the sensor. 
    The data obtained in sleep mode is wrong
  */
  if(SLEEP_MODE == mics.getPowerState()){
    mics.wakeUpMode();
    Serial.println("sleep mode,   wake up sensor success!");
  }else{
    mics.sleepMode();
    Serial.println("wake up mode, sleep sensor success!");
  }
  delay(3000);
}