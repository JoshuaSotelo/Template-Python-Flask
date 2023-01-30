from views.views import views
from flask import Flask

from extensions import db
# flask instance creation
app = Flask(__name__)
app.register_blueprint(views)
app.app_context().push()

app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {
    'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xml'}

db.init_app(app)


with app.app_context():
    db.create_all()

if __name__ == '__app__':
    app.run(debug=True)
