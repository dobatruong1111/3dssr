from sanic import Sanic
from settings import settings

app = Sanic(__name__)
settings.load_settings(app)