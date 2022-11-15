from fastapi import FastAPI
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates=Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def showData(request: Request):
     
    return templates.TemplateResponse('registration.html', {"request": request})


@app.get("/items/{item_id}")    
def read_item(item_id:int):
    return {"item_id":item_id}