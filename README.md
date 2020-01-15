# 阿里天池-智能算法赛：瓶装白酒疵品质检
单阶段目标检测模型YOLOv3<br>
原项目：https://github.com/qqwweee/keras-yolo3

# 环境
keras 2.2.0 <br>
tensorflow 1.10.0 <br>
Pillow <br>

# 训练
1、新建training_images 放入所有训练图片<br>
2、下载预训练权重yolo_weights.h5放入model_data文件夹下<br>
   链接：https://pan.baidu.com/s/1joPFjX-9O4wa41MLn_R7zA 提取码：4b6x <br>
3、运行train.py

# 测试并生成json文件
1、新建testing_images 放入所有测试图片<br>
2、运行test.py<br>

# 训练效果
![alt text](https://github.com/shadow12138/tianchi_bottle/blob/master/result/training_set_mAP.png)<br>