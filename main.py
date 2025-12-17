from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''SELECT * FROM catalog''')
catalog_items = cursor.fetchall()
print(catalog_items)

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(name='index.html', context={'request': request, 'catalog': catalog_items})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

