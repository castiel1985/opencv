from flask import Blueprint  # 仅仅用于run.py

musics = Blueprint('misics', __name__)  # 创建一个blueprint对象。第一个参数可看做该blueprint对象的姓名


# 在一个app里，姓名不能与其余的Blueprint对象姓名重复
# 第二个参数__name__用作初始化

@musics.route("/music")  # 将蓝图对象当做‘app’那样使用
def music():
    return '这里是一首音乐~'