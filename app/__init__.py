from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)



from app import routes, models
models.db.initialize_db(app)


if __name__ == "__main__":
    app.run()
