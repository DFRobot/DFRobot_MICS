 /*!
  * @file  getADCData.ino
  * @brief Reading MICS sensor ADC original value
  * @n When using IIC device, select I2C address, set the dialing switch A0, A1 (Address_0 is [0 0]), (Address_1 is [1 0]), (Address_2 is [0 1]), (Address_3 is [1 1]).
  * @n When using the Breakout version, connect the adcPin and PowerPin
  * @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  * @licence     The MIT License (MIT)
  * @author      ZhixinLiu(zhixin.liu@dfrobot.com)
  * @version     V1.2
  * @date        2021-06-18
  * @get         from https://www.dfrobot.com
  * @url         https://github.com/dfrobot/DFRobot_MICS
  */
#include "DFRobot_MICS.h"

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

// When using the Breakout version, use the following program to construct an object from DFRobot_MICS_ADC
/**!
  adcPin is A0~A5
  powerPin is General IO
*/
#define ADC_PIN   A0
#define POWER_PIN 10
//DFRobot_MICS_ADC mics(/*adcPin*/ADC_PIN, /*powerPin*/POWER_PIN);

void setup() 
{
  Serial.begin(115200);
  while(!Serial);
  while(!mics.begin()){
    Serial.println("NO Deivces !");
    delay(1000);
  } Serial.println("Device connected successfully !");

  /**!
    Gets the power mode of the sensor
    The sensor is in sleep mode when power is on,so it needs to wake up the sensor. 
    The data obtained in sleep mode is wrong
   */
  uint8_t mode = mics.getPowerState();
  if(mode == SLEEP_MODE){
    mics.wakeUpMode();
    Serial.println("wake up sensor success!");
  }else{
    Serial.println("The sensor is wake up mode");
  }
}

void loop() 
{
  int16_t ox_data  = 0;
  int16_t red_data = 0;
  /**!
    MICS-5524 Only OX_MODE ADC data can be obtained
    MICS-2714 Only RED_MODE ADC data can be obtained
    MICS-4514 Gravity can obtain AllMode ADC data
  */
  ox_data  = mics.getADCData(OX_MODE);
  //red_data = mics.getADCData(RED_MODE);
  Serial.print("ox  data = ");
  Serial.println(ox_data);
  //Serial.print("red data = ");
  //Serial.println(red_data);
  delay(1000);
}