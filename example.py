from flask import Flask

# Flask 是一个类，我们可以点进去看详细的描述。app是Flask这个类创建出来的对象。
# __name__是获取当前文件的名字，我们可以尝试print(__name__)，就会看见结果是：__main__。
#print(app.config)                               # 可以通过app.config查看所有参数。
app = Flask(__name__)


@app.route('/')                             # 路由
def hello_world():                              # 在此路由下的视图（函数）
    return 'Hello World!'

if __name__ == '__main__':
    #app.run()                                  # 启动flask内部服务器，主机地址和端口号选取默认值
    app.run(port=3300,host="127.0.0.13")        # 启动flask内部服务器，主机地址和端口号可自定义
