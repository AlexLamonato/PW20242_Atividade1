from util import obter_conexao
from sql.produto_sql import SQL_CRIAR_TABELA, SQL_OBTER_TODOS, SQL_INSERIR
# from produto_model import Produto
def criar_tabela():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(SQL_CRIAR_TABELA)
    conexao.commit()
    conexao.close()



def inserir(produto):
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(SQL_INSERIR, (produto.nome, produto.descricao, produto.estoque, produto.preco, produto.categoria))
    conexao.commit()
    conexao.close()

def obter_todos():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(SQL_OBTER_TODOS)
    rows = cursor.fetchall()
    conexao.close()
    
    produtos = []
    for row in rows:
        produto = Produto(id=row[0], nome=row[1], descricao=row[2], estoque=row[3], preco=row[4], categoria=row[5])
        produtos.append(produto)
    
    return produtos