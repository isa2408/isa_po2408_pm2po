from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get("/index", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request })

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
