from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from repositories.produto_repo import inserir, criar_tabela  # Importa o repositório de produto
from models.produto_model import Produto  # Importa o modelo Produto

app = FastAPI()
templates = Jinja2Templates(directory="templates")
criar_tabela()


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
    estoque: int = Form(...),
    preco: str = Form(...), 
    categoria: str = Form(...)):
    
    try:
        preco_float = float(preco)
    except ValueError:
        # Preço inválido, redireciona de volta para a página de cadastro
        return RedirectResponse("/cadastro", 303)

    # Cria o objeto Produto usando a classe dataclass e os dados do formulário
    produto = Produto(nome=nome, descricao=descricao, estoque=estoque, preco=preco_float, categoria=categoria)
    
    # Chama o método inserir do repositório para salvar o produto
    inserir(produto)
    
    # Redireciona para a página de confirmação de cadastro recebido
    return RedirectResponse("/cadastro_recebido", 303)

@app.get("/cadastro_recebido")
async def cadastro_recebido(request: Request):
    return templates.TemplateResponse("cadastro_recebido.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
