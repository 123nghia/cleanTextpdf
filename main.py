from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Import router từ api
from api.endpoints import router as api_router

app = FastAPI()

# Mount static + temp
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/temp", StaticFiles(directory="temp"), name="temp")

# Templates
templates = Jinja2Templates(directory="templates")

# Include router API
app.include_router(api_router)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
