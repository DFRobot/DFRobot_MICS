 /*!
  * @file  getGasPPM.ino
  * @brief Reading Gas concentration, A concentration of one part per million (PPM).
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

  /**!
     Do not touch the sensor probe when preheating the sensor.
     Place the sensor in clean air.
     The default calibration time is 3 minutes.
  */
  while(!mics.warmUpTime(CALIBRATION_TIME)){
    Serial.println("Please wait until the warm-up time is over!");
    delay(1000);
  }
}

void loop() 
{
  /**!
    Gas type:
    MICS-4514 You can get all gas concentration
    MICS-5524 You can get the concentration of CH4, C2H5OH, H2, NH3, CO
    MICS-2714 You can get the concentration of NO2
      CO       = 0x01  (Carbon Monoxide)  (1    - 1000)PPM
      CH4      = 0x02  (Methane)          (1000 - 25000)PPM
      C2H5OH   = 0x03  (Ethanol)          (10   - 500)PPM
      H2       = 0x06  (Hydrogen)         (1    - 1000)PPM
      NH3      = 0x08  (Ammonia)          (1    - 500)PPM
      NO2      = 0x0A  (Nitrogen Dioxide) (0.1  - 10)PPM
  */
  float gasdata = mics.getGasData(C2H5OH);
  Serial.print(gasdata,1);
  Serial.println(" PPM");
  delay(1000);
  //mics.sleepMode();
}