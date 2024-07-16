# &#x20;                   玻璃缺陷分析网站

## 一、简介：

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

## 二、使用指南

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

7.在axios.js中修改自己设置的ip与端口：

![image](README_imgs/e9f03830-4261-11ef-b233-03b40ca9e964.jpeg?v=1\&type=image)

8.在glass\_vue路径下，运行命令：

    npm run serve         #运行前端部分

9.运行run.py文件（运行后端部分）

## 三、目录结构解答

本章节，我将通过介绍本项目的目录结构使读者深入了解本项目的运作与编写流程

由于作者也是刚入门，所以项目结构会出现不标准现象，但大概就这这样（buhsi）

### 1.总体结构：

这是本项目的外部结构，由三大部分与一些小文件组成：

![](README_imgs/c2daf990-41c8-11ef-be91-bb7ecf96b99b_20240714180639.jpeg?v=1\&type=image\&token=V1%3AH25zFylff9p6VzLWt21gZuzkcWAWdG6nacgF9m9D-r4)

*   app:放置了所有的后端代码（出来启动文件）

*   glass\_vue:放置了所有的前端代码

*   static：放置了本项目实现的功能所使用到的相关文件

*   example.py：没什么用，忽略

*   requirements.txt：记录了运行后端用到的库

*   run.py：启动后端的启动文件

### 2.后端结构：

后端主要功能：

1.对前端api请求的接受，处理，返回响应。

2.与数据库的联系。

进入app文件夹，也就是进入了后端区域：

![](README_imgs/cf460840-41c9-11ef-be91-bb7ecf96b99b_20240714181409.jpeg?v=1\&type=image\&token=V1%3AXinU004QTswO9BAULssY7AfKgjYcBpsLD2MoNfIZlEE)

*   pycache：不用管，应该是运行时的缓存

*   routes：路由的主要作用是对前端api请求的接受，并返回响应。

*   service：存放对应的函数负责处理请求，执行必要的逻辑。

*   templates：存放着每个功能的html文件，不与前端连接直接启动后端即可查看的页面（这部分没有更新，目前无法使用，即只运行后端无法查看页面）

*   init.py：初始化路由的文件

*   config.py：记录着static文件夹中各文件夹/文件的路径

后端运行流程：

run.py运行后端——run.py进入init.py初始化routes——后端等待前端调用api——前端请求使用后端的某个api——后端通过routes进入对应的service——service处理请求——返回相应

### 3.前端结构：

前端主要功能：

1.对用户展示页面

2.对后端发送api请求

3.处理从后端返回的响应

前端我使用vue进行搭建，vue最大的特点我认为就是组件化。

进入glass\_vue文件夹，使用vue\_cli脚手架(npm install -g @vue/cli)搭建基本的vue结构(vue create my-vue-app)，进入src文件夹中：

![](README_imgs/e5698bf0-41cf-11ef-be91-bb7ecf96b99b_20240714185744.jpeg?v=1\&type=image\&token=V1%3AwapbqXvlHoT08Q0mqtf5f8mYuJRSPT1Dmeegs8G6oII)

*   assets：我在搭建时没有使用到

*   components：存放着vue的组件

*   plugins：使用插件vuetify时获得的，不下载就不会有，不用可以不下载

*   router：使用路由可以在多个组件或页面中跳转

*   utils：存放这axios的文件，定义了发送api的基地址

*   views：存放通过使用组件组合成的页面

*   App.vue：全部vue组件的挂载点，即根目录

*   main.js：前端启动文件

vue前端主要就是对组件的编写以及定义对应的路由，最后通过组件组合成一个个展示出来的页面，而每个页面使用组件时只要通过定义好的路由即可直接调用，而不需要在页面中再写一份组件代码，提高了组件的利用率。

