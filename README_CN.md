# DFRobot_MICS
- [English Version](./README.md)

这是一款由DFRobot推出的3.3/5V兼容的MEMS气体浓度传感器,支持CO,C2H5OH(Alcohol),H2,NO2,NH3等多种气体浓度的检测,代码中集成了各种气体的浓度换算公式,方便传感器的测试和使用。支持3.3~5.5V宽电压输入,支持I2C输出方式,兼容Arduino、ESP32、树莓派等主流的主控设备,具有良好的兼容性。<br>

![正反面svg效果图](resources/images/SEN0377.jpg)

## 产品链接(https://www.dfrobot.com.cn/goods-3317.html)

    SKU:SEN0377

## 目录

* [概述](#概述)
* [库安装](#库安装)
* [方法](#方法)
* [兼容性](#兼容性y)
* [历史](#历史)
* [创作者](#创作者)

## 概述

- 检测物理量:CO,C2H5OH(Alcohol),H2,NO2,NH3,CH4的气体浓度<br>
- 工作电压: 3.3～5.5V DC<br>
- 功耗:0.45W(5V)<br>
- 输出信号: I2C(0~3V)<br>
- 测量范围:<br>
1 – 1000ppm(一氧化碳 CO )<br>
0.05 – 10ppm(二氧化氮 NO2)<br>
10 – 500ppm(乙醇 C2H5OH )<br>
1 – 1000ppm(氢气 H2)<br>
1 – 500ppm(氨气 NH3 )<br>
1000 - ∞ ppm(甲烷 CH4 )<br>
- 工作温度: -30～85℃<br>
- 工作湿度: 5～95%RH (无凝结)<br>
- 存储温度: -40~85℃<br>
- 寿 命: >2 年(空气中)<br>
- 电路板尺寸:27mm*37mm<br>
- 安装孔尺寸:内径3.1mm/外径6mm<br>

## 库安装
这里提供两种使用本库的方法:<br>
1.打开Arduino IDE,在状态栏中的Tools--->Manager Libraries 搜索"DFRobot_MICS"并安装本库.<br>
2.首先下载库文件,将其粘贴到\Arduino\libraries目录中,然后打开examples文件夹并在该文件夹中运行演示.<br>

## 方法

```C++
  /**
   * @fn warmUpTime
   * @brief 加热时间
   * @param minute 
   * @return bool type
   * @retval true  加热完成
   * @retval false 正在加热中
   */
  bool warmUpTime(uint8_t minute);

  /**
   * @fn getADCData
   * @brief 获取传感器的adc数据
   * @param mode 氧化模式 还原模式
   * @n     OX_MODE
   * @n     RED_MODE
   * @return adcValue (0-1024)
   */
  int16_t getADCData(uint8_t mode);

  /**
   * @fn getGasData
   * @brief 读取气体的浓度
   * @param type 气体类型
   * @n   Methane          (CH4)    (1000 - 25000)PPM
   * @n   Ethanol          (C2H5OH) (10   - 500)PPM
   * @n   Hydrogen         (H2)     (1    - 1000)PPM
   * @n   Ammonia          (NH3)    (1    - 500)PPM
   * @n   Carbon Monoxide  (CO)     (1    - 1000)PPM
   * @n   Nitrogen Dioxide (NO2)    (0.1  - 10)PPM
   * @return 气体浓度,单位 ppm
   */
  float getGasData(uint8_t type);

   /**
   * @fn getGasExist
   * @brief 获取气体是否存在
   * @param gas
   * @n   CO       = 0x01  (Carbon Monoxide)
   * @n   CH4      = 0x02  (Methane)
   * @n   C2H5OH   = 0x03  (Ethanol)
   * @n   C3H8     = 0x04  (Propane)
   * @n   C4H10    = 0x05  (Iso Butane)
   * @n   H2       = 0x06  (Hydrogen)
   * @n   H2S      = 0x07  (Hydrothion)
   * @n   NH3      = 0x08  (Ammonia)
   * @n   NO       = 0x09  (Nitric Oxide)
   * @n   NO2      = 0x0A  (Nitrogen Dioxide)
   * @return state
   * @retval NO_EXIST
   * @retval EXIST
   */
  int8_t getGasExist(uint8_t gas);

  /**
   * @fn sleepMode
   * @brief 睡眠传感器
   */ 
  void sleepMode(void);

  /**
   * @fn wakeUpMode
   * @brief 唤醒传感器
   */ 
  void wakeUpMode(void);

  /**
   * @fn getPowerState
   * @brief 获取传感器电源模式
   * @return state
   * @retval SLEEP_MODE
   * @retval WAKE_UP_MODE
   */ 
  uint8_t getPowerState(void);
```

## 兼容性

| 主板        | 通过 | 未通过 | 未测试 | 备注 |
| ----------- | :--: | :----: | :----: | ---- |
| Arduino uno |  √   |        |        |      |
| Mega2560    |  √   |        |        |      |
| Leonardo    |  √   |        |        |      |
| ESP32       |  √   |        |        |      |
| micro:bit   |      |        |   √    |      |


## 历史

- 2021/1/13 - V1.0.0 版本
- 2021/4/20 - V1.1.0 版本
- 2021/7/18 - V1.2.0 版本

## 创作者

Written by ZhixinLiu(zhixin.liu@dfrobot.com), 2020. (Welcome to our [website](https://www.dfrobot.com/))