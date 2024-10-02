from re import template
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.get("/")
async def get_root(request: Request):
    return template.TemplatesResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)