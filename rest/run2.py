
from flask import Flask

from app.dept import dept
from app.user import user

app = Flask(__name__)

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(dept, url_prefix='/dept')


if __name__ =='__main__':
    app.run()