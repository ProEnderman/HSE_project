from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from utils.DFwork import filter_cars
from utils.DFwork import new_row
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def welcome(request: Request):
    return templates.TemplateResponse("Welcome.html", {"request": request})

@app.get("/hypothesis", response_class=HTMLResponse)
async def hypothesis(request: Request):
    return templates.TemplateResponse("hypothesis.html", {"request": request})

@app.get("/data", response_class=HTMLResponse)
async def data_form(request: Request):
    return templates.TemplateResponse("data.html", {"request": request, "result": None, "lst": None})

@app.post("/data", response_class=HTMLResponse)
async def data(
    request: Request,
    param1: str = Form(...),
    op1: str = Form(...),
    value1: str = Form(...),
    param2: str = Form(...),
    op2: str = Form(...),
    value2: str = Form(...),
    param3: str = Form(...),
    op3: str = Form(...),
    value3: str = Form(...),
):
    result, is_empty = filter_cars(param1, op1, value1, param2, op2, value2, param3, op3, value3)
    return templates.TemplateResponse("data.html", {"request": request, "result": result, "lst": None, "is_empty": is_empty})

@app.get("/add", response_class=HTMLResponse)
async def add(request: Request):
    # Pass result as None or some default value
    return templates.TemplateResponse("add.html", {"request": request, "result": None, "lst": None})

@app.post("/add", response_class=HTMLResponse)
async def add(
    request: Request,
    value1: str = Form(...),
    value2: int = Form(...),
    value3: str = Form(...),
    value4: str = Form(...),
    value5: str = Form(...),
    value6: str = Form(...),
    value7: str = Form(...),
    value8: str = Form(...),
    value9: str = Form(...),
    value10: str = Form(...),
    value11: str = Form(...),
    value12: str = Form(...),
):
    result, _ = new_row(
        value1, value2, value3, value4, value5, value6,
        value7, value8, value9, value10, value11, value12
    )
    return templates.TemplateResponse("add.html", {"request": request, "result": result, "lst": None})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5500)
#git init
#git add .
#git commit -m "Initial commit"
#git remote add origin https://github.com/ProEnderman/HSE_project
#git push -u origin main