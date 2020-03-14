# 车牌识别

#### 介绍
车牌识别：yolov3-keras + tr(OCR)

#### 软件架构
代码主要分为两大部分：
1. 检测车牌区域：Keras 实现 YOLOv3 网络模型进行训练：[keras-yolo3](https://github.com/experiencor/keras-yolo3)
    - 预训练模型下载地址：[预训练](https://bit.ly/2tIpvPl)（需翻墙）
2. 识别车牌文本：使用开源的一个OCR检测方法:[tr-master](https://github.com/myhub/tr)
    - 安装好即可使用，无需再训练



#### 安装教程

 **检测车牌区域——keras-yolo3:** 
- conda create --name py36-keras python=3.6
- git clone https://github.com/experiencor/keras-yolo3.git
- cd keras-yolo3
- pip install -r requirements.txt

 **车牌文本识别——tr：** 
- git clone https://github.com/myhub/tr.git
- cd ./tr
- sudo python setup.py install



#### 使用说明

 **检测车牌区域** 
    - 训练：`python train.py -c config_license_plates.json`(zoo中提供json文件）
    - 预测：`python predict.py -c config_license_plates.json -i /path/to/image/or/video`
            直接将检测出的车牌区域裁剪出并缩小一倍（以便加速OCR的识别），并保存到‘/tr/cut/’文件夹中

 **车牌文本识别** 
    - `python test.py`（需根据自己的数据集路径进行修改）


