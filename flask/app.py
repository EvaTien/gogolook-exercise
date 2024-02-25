from flask import Flask
from database import engine
from models import Base


def create_app():
    app = Flask(__name__)
    Base.metadata.create_all(bind=engine)
    return app


app = create_app()


@app.route("/")
def index():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
