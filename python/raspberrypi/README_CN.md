# DFRobot_MICS
- [English Version](./README.md)

这是一款由DFRobot推出的3.3/5V兼容的MEMS气体浓度传感器,支持CO,C2H5OH(Alcohol),H2,NO2,NH3等多种气体浓度的检测,代码中集成了各种气体的浓度换算公式,方便传感器的测试和使用。支持3.3~5.5V宽电压输入,支持I2C输出方式,兼容Arduino、ESP32、树莓派等主流的主控设备,具有良好的兼容性。<br>

![正反面svg效果图](../../resources/images/SEN0377.jpg)


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
使用此库前,请首先下载库文件,将其粘贴到树莓派的自定义目录中,然后打开examples文件夹并在该文件夹中运行演示。

## 方法

```python
  '''!
    @brief 睡眠传感器
  '''
  def sleep_mode(self):
  
  '''!
    @brief 唤醒传感器
  '''
  def wakeup_mode(self):

  '''!
    @breif 获取电源模式
    @return mode SLEEP_MODE or WAKEUP_MODE
  '''
  def get_power_mode(self):
  
  '''!
    @brief 等待传感器加热
    @param 传感器加热时间 单位分钟
  '''
  def warm_up_time(self, minute):
  
  '''!
    @brief 获取传感器adc 的数据
    @param 模式,氧化模式、还原模式
    @return adc 数据
  '''
  def get_adc_data(self, mode):
  
  '''!
    @brief 获取传感器浓度
    @param 气体类型
    @param CO        0x01  (Carbon Monoxide)
    @param CH4       0x02  (Methane)
    @param C2H5OH    0x03  (Ethanol)
    @param H2        0x06  (Hydrogen)
    @param NH3       0x08  (Ammonia)
    @param NO2       0x0A  (Nitrogen Dioxide)
    @return 气体浓度,(单位 ppm)
  '''
  def get_gas_ppm(self, gas_type):
  
  '''!
    @brief 获取气体是否存在
    @param 气体类型
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
    @return 气体是否存在
  '''
  def get_gas_exist(self, gas_type):
```

## 兼容性

* RaspberryPi Version

| Board        | 正常运行  | 运行失败   | 未测试    | 备注
| ------------ | :-------: | :--------: | :------: | :-----: |
| RaspberryPi2 |           |            |    √     |         |
| RaspberryPi3 |           |            |    √     |         |
| RaspberryPi4 |     √     |            |          |         |

* Python版本

| Python  | 正常运行  | 运行失败   | 未测试    | 备注
| ------- | :-------: | :--------: | :------: | :-----: |
| Python2 |     √     |            |          |         |
| Python3 |     √     |            |          |         |


## 历史

- 2021/1/13 - V1.0.0 版本
- 2021/4/20 - V1.1.0 版本
- 2021/7/18 - V1.2.0 版本

## 创作者

Written by ZhixinLiu(zhixin.liu@dfrobot.com), 2020. (Welcome to our [website](https://www.dfrobot.com/))