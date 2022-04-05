import app
import flask_script as script
from flask_sqlalchemy import SQLAlchemy

app = app.create_application()
db = SQLAlchemy(app)
manager = script.Manager(app)


if __name__=="__main__":
    manager.run()