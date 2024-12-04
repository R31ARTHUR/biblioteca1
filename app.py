from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Dados em memória
usuarios = []
livros = []
locacoes = []

@app.route('/')
def index():
    """Página inicial"""
    for locacao in locacoes:
        if locacao['data_devolucao']:
            locacao['atrasado'] = False
        else:
            data_prevista = datetime.strptime(locacao['data_prevista'], '%Y-%m-%d')
            hoje = datetime.now()
            locacao['atrasado'] = hoje > data_prevista
    return render_template('index.html', locacoes=locacoes)

# Páginas de gerenciamento
@app.route('/usuarios')
def gerenciar_usuarios():
    """Página para gerenciar usuários"""
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/livros')
def gerenciar_livros():
    """Página para gerenciar livros"""
    return render_template('livros.html', livros=livros)

# Cadastro de usuários
@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    id_usuario = len(usuarios) + 1
    nome = request.form['nome']
    turma = request.form['turma']
    nome_turma = request.form['nome_turma']
    usuarios.append({'id': id_usuario, 'nome': nome, 'turma': turma, 'nome_turma': nome_turma})
    return redirect(url_for('gerenciar_usuarios'))

# Cadastro de livros
@app.route('/cadastrar_livro', methods=['POST'])
def cadastrar_livro():
    id_livro = len(livros) + 1
    titulo = request.form['titulo']
    autor = request.form['autor']
    ano = request.form['ano']
    livros.append({'id': id_livro, 'titulo': titulo, 'autor': autor, 'ano': ano})
    return redirect(url_for('gerenciar_livros'))

# Registro de locações
@app.route('/registrar_locacao', methods=['POST'])
def registrar_locacao():
    id_usuario = int(request.form['id_usuario'])
    id_livro = int(request.form['id_livro'])
    data_retirada = request.form['data_retirada']
    data_prevista = request.form['data_prevista']
    locacoes.append({
        'id': len(locacoes) + 1,
        'id_usuario': id_usuario,
        'id_livro': id_livro,
        'data_retirada': data_retirada,
        'data_prevista': data_prevista,
        'data_devolucao': None,
        'atrasado': False
    })
    return redirect(url_for('index'))

# Registro de devolução
@app.route('/registrar_devolucao/<int:locacao_id>', methods=['POST'])
def registrar_devolucao(locacao_id):
    data_devolucao = request.form['data_devolucao']
    for locacao in locacoes:
        if locacao['id'] == locacao_id:
            locacao['data_devolucao'] = data_devolucao
            locacao['atrasado'] = False
            break
    return redirect(url_for('index'))

# Busca por usuários e livros
@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '').lower()
    resultados_usuarios = [usuario for usuario in usuarios if termo in usuario['nome'].lower()]
    resultados_livros = [livro for livro in livros if termo in livro['titulo'].lower()]
    return render_template('busca.html', termo=termo, usuarios=resultados_usuarios, livros=resultados_livros)

if __name__ == '__main__':
    app.run(debug=True)
