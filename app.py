from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta

app = Flask(__name__)

# Dados simulados em memória
alunos = []  # Lista para armazenar alunos
livros = []  # Lista para armazenar livros
emprestimos = []  # Lista para armazenar empréstimos

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Cadastro de alunos
@app.route('/cadastrar_aluno', methods=['GET', 'POST'])
def cadastrar_aluno():
    if request.method == 'POST':
        aluno = {
            'id': int(request.form['id']),
            'nome': request.form['nome'],
            'turma': request.form['turma'],
            'serie': request.form['serie'],
            'turno': request.form['turno']
        }
        alunos.append(aluno)
        return redirect(url_for('cadastrar_aluno'))
    return render_template('cadastrar_aluno.html', alunos=alunos)

# Cadastro de livros
@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        livro = {
            'id': int(request.form['id']),
            'titulo': request.form['titulo'],
            'autor': request.form['autor'],
            'ano': int(request.form['ano'])
        }
        livros.append(livro)
        return redirect(url_for('cadastrar_livro'))
    return render_template('cadastrar_livro.html', livros=livros)

# Registro de empréstimos
@app.route('/registrar_emprestimo', methods=['GET', 'POST'])
def registrar_emprestimo():
    if request.method == 'POST':
        emprestimo = {
            'aluno_id': int(request.form['aluno_id']),
            'livro_id': int(request.form['livro_id']),
            'data_retirada': datetime.now().strftime('%Y-%m-%d'),
            'data_prevista': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
            'devolvido': False
        }
        emprestimos.append(emprestimo)
        return redirect(url_for('registrar_emprestimo'))
    return render_template('registrar_emprestimo.html', alunos=alunos, livros=livros, emprestimos=emprestimos)

# Registro de devoluções
@app.route('/registrar_devolucao', methods=['GET', 'POST'])
def registrar_devolucao():
    if request.method == 'POST':
        aluno_id = int(request.form['aluno_id'])
        livro_id = int(request.form['livro_id'])
        for emprestimo in emprestimos:
            if emprestimo['aluno_id'] == aluno_id and emprestimo['livro_id'] == livro_id:
                emprestimo['devolvido'] = True
                emprestimo['data_devolucao'] = datetime.now().strftime('%Y-%m-%d')
                break
        return redirect(url_for('registrar_devolucao'))
    return render_template('registrar_devolucao.html', emprestimos=emprestimos, alunos=alunos, livros=livros)

# Lista de atrasados
@app.route('/atrasados')
def atrasados():
    atrasados_list = []
    for emprestimo in emprestimos:
        if not emprestimo['devolvido'] and datetime.strptime(emprestimo['data_prevista'], '%Y-%m-%d') < datetime.now():
            aluno = next((al for al in alunos if al['id'] == emprestimo['aluno_id']), None)
            livro = next((lv for lv in livros if lv['id'] == emprestimo['livro_id']), None)
            atrasados_list.append({
                'aluno': aluno,
                'livro': livro,
                'data_prevista': emprestimo['data_prevista']
            })
    return render_template('atrasados.html', atrasados=atrasados_list)

# Histórico de devoluções
@app.route('/historico')
def historico():
    historico_list = [
        {
            'aluno': next((al for al in alunos if al['id'] == emp['aluno_id']), None),
            'livro': next((lv for lv in livros if lv['id'] == emp['livro_id']), None),
            'data_devolucao': emp.get('data_devolucao')
        }
        for emp in emprestimos if emp['devolvido']
    ]
    return render_template('historico.html', historico=historico_list)

if __name__ == '__main__':
    app.run(debug=True)
