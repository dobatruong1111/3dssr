from app import app
from sanic.blueprints import Blueprint
from sanic import response
from sanic_openapi import swagger_blueprint
from logic import dicom

blueprint = Blueprint("App")

@blueprint.get("/")
async def handlerHome(request):
    return response.text("Home")

@blueprint.post("/dicom")
async def handlerDicom(request):
    return response.raw(dicom.getBytes(request.json), headers={"content-type":"image/png"})
    
app.blueprint(blueprint)
app.blueprint(swagger_blueprint)