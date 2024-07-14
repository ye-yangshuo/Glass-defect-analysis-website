# &#x20;                   玻璃缺陷分析网站

## 1.简介：

该网站使用的是vue前端加flask后端开发的网站，是与智能玻璃缺陷检测系统配套的网站（智能玻璃缺陷检测系统见我的另外一个开源项目glass-detect）。

**使用技术：**

前端：vue    后端：flask

**使用前提：**

1.前端：已经安装好node.js，配置好npm

2.后端：已经构建好python虚拟环境

**适用群体：**

1.初学vue，flask     2.想要构建vue与flask结合的项目

**目前实现功能：**

1.登录        2.数据查看        3.数据分析

后续可能会持续更新

## 2.使用指南

本章我会引导各位运行本项目：

1.下载或直接克隆本项目到本地，打开本项目。

    https://github.com/ye-yangshuo/Glass-defect-analysis-website.git

2.在创建好的python虚拟环境中运行命令：

    pip install -r requirements.txt     #安装该项目后端所需要用到的库

3.在run.py文件中修改：

    app.run(host= '192.168.123.84',port=8081)

俩种修改方法：

*   直接删除里面的参数，默认直接使用127.0.0.1:5000

*   修改host为自己此时的ip，端口可以任意设置，但注意不要设置通用的端口不然会报错

4.修改：

在文件夹app下的config.py中修改：

将每个功能使用的到的文件夹路径修改为自己的路径，具体修改路径的文件夹在static下

在文件夹static下的user文件夹中的user.txt中修改：

将登陆信息修改为自己的，第一个是编号，第二个是用户名，第三个密码。

5.终端cd进入glass\_vue，运行命令：

    npm install        #下载项目前端使用到的依赖

6.在ImageView\.vue，DataAnalyze.vue中修改：

具体路径：\
![image](README_imgs/32d99780-41bd-11ef-96dd-83d6321fcfd1_20240714164353.jpeg?v=1\&type=image\&token=V1%3A5ny-_my9BM7mQLBH_aRpXVC0VZqHXEyPmBZlSsRSMyk)

修改内容Baseurl：将基地址修改为刚刚在第3步你自己设置的ip与端口

![image](README_imgs/62ae9e10-41bd-11ef-96dd-83d6321fcfd1_20240714164513.jpeg?v=1\&type=image\&token=V1%3At60FC0YZKFn_69dY4x9jJqn_LUEseHETeBNvGvEr76c)

7.在glass\_vue路径下，运行命令：

    npm run serve         #运行前端部分

8.运行run.py文件（运行后端部分）
