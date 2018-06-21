from flask import Flask
from app import img,video
from flask_script import Manager, Command


app = Flask(__name__)
manage = Manager(app)

@manage.command
def hello():
    print("hello cmd")


vid = video.video()
@manage.command
def video():
    vid.show()



image = img.img()

@manage.command
def img():
    print("*************")
    image.totest()
    print("*************")


@manage.command
def togray():
    image.togray()

@manage.command
def toshow():
    image.toshow()

if __name__ == "__main__":
    manage.run()