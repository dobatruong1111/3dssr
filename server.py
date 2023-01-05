from app import app
from routes import routes

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=app.config.DEBUG, workers=app.config.WORKERS)