# information-extraction-of-express
基于OpenCV、目标检测对快递单进行识别并提取有用的信息进行处理


# git_express

### 1、利用OpenCV的二值化、滤波、形态学处理得到最大的数字区域
**express detection.py**
结果：
<div align=center>![Alt text](https://github.com/weijiawu/information-extraction-of-express/raw/master/image/1533113515(1).png)


### 2、运用霍夫变换检测直线得到目标信息
**houghlines_detection.py**
<div align=center>![Alt text](https://github.com/weijiawu/information-extraction-of-express/raw/master/image/1532961320(1).png)

### 3、文本识别：DenseNet + CTC
**ocr_recognition**
效果：
![Alt text](https://github.com/weijiawu/information-extraction-of-express/raw/master/image/1534857600(1).png)

