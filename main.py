from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from util import salvar_cadastro

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
async def cadastro(request: Request):
    return templates.TemplateResponse("Cadastro.html", {"request": request})

@app.post("/dados/cadastros")
async def postar_cadastro(request: Request,
    nome: str = Form(...), 
    descricao: str = Form(...),
    estoque: str = Form(...),
    preco: str = Form(...), 
    categoria: str = Form(...)):
    
    try:
        preco_float = float(preco)
    except ValueError:
        # Preço inválido, redireciona de volta para a página de cadastro
        return RedirectResponse("/cadastro", 303)

    salvar_cadastro(nome, descricao, estoque, preco_float, categoria)
    return RedirectResponse("/cadastro_recebido", 303)

@app.get("/cadastro_recebido")
async def cadastro_recebido(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
