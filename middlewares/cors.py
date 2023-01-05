from app import app
from sanic import response

@app.middleware("request")
async def cors(request):
    if request.method == "OPTIONS":
        return response.HTTPResponse(status=200)