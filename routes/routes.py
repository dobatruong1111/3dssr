from app import app
from sanic.blueprints import Blueprint
from sanic import response
from logic import dicom

blueprint = Blueprint("App")

@blueprint.get("/")
async def handlerHome(request):
    return response.text("Home")

@blueprint.post("/dicom3d")
async def handlerDicom(request):
    return response.raw(dicom.Dicom3D().getBytes(request.json), headers={"content-type":"image/png"})
    
app.blueprint(blueprint)