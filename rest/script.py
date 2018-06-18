from flask import Flask
from flask_script import Manager
from flask_script import Command
from app import img,video

app = Flask(__name__)
manager = Manager(app)


class toimg(Command):
    def run(self):
        img.test()

class tovideo(Command):
    def run(self):
        video.show()


#manager.add_command('hello', set())
manager.add_command('img', toimg())
manager.add_command('video', tovideo())

if __name__ == '__main__':
    manager.run()