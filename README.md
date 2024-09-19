# 基于Flask的android前后端模型部署

### 后端

1. 基于Flask框架部署在本地，需要在#同一个局域网内#

   windows通过系统命令行的ipconfig可以查看自己的ip

   linux通过命令行的ifconfig可以查看自己的ip

2. server.py为服务器代码，其中注释了处理开始和处理结束的节点，把中间的部分修改成自己的模型

3. emotion_detection_model.h5为模型

4. test.py为模型加载代码，对外给出接口def detect_emotion(img)用于使用模型训练，输入为图片（numpy的矩阵形式），输出为带结果标签的图片

5. testNet.py为服务器测试代码，需要把ip修改为服务器的ip

   img.png为测试输入图片，resimg.png为保存的测试输出图片

   

   

### 前端

1. android端app，需要和服务器在一个局域网内，可以通过电脑部署服务器，打开热点由手机连接wifi
2. 如果完整的copy项目到本地，需要修改的地方：
   	1. local.properties：把sdk改为本地的sdk路径
    	2. mainActivity中的server_url：修改为服务器的ip

3. 如果实在build失败，请自行打开一个新的项目，把自己的主体代码（包括文件夹mainfests、java、res）替换为这个代码，然后导入对应的包