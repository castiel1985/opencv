# -*- coding:utf-8 -*-
from flask import Flask  # 不用多说
from app import musics  # 导入blueprints目录下musics.py与movies.py模块,

app = Flask(__name__)  # 创建 Flask()对象： app


@app.route('/')  # 使用了蓝图，app.route() 这种模式就仍可以使用，注意路由重复的问题
def hello_world():
    return 'hello my world !'


app.register_blueprint(musics.musics)  # 将musics模块里的蓝图对象musics注册到app
#app.register_blueprint(movies.movies)  # 将movies模块里的蓝图对象movies注册到app

if __name__ == '__main__':
    app.run(debug=True)