from flask_script import Manager, Command

from flask import Flask

app = Flask(__name__)
manage = Manager(app)

@manage.command
def hello():
    print("hello cmd")

@manage.command
def video():
    print("this is video area")

@manage.command
def img():
    print("*************")

if __name__ == "__main__":
    manage.run()
