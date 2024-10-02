from re import template
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastrao")
async def cadastro(request: Request):
    return templates.TemplateResponse("Cadastrar.html", {"request": request})

@app.post("/post_cadastro")
async def postar_cadastro(
    nome: str = Form(...), 
    descricao: str = Form(...),
    estoque: str = Form(...),
    preco: str = Form(...), 
    categoria: str = Form(...), 
    confirmacao_senha: str = Form(...))
    return RedirectResponse("/cadastro", 303)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)