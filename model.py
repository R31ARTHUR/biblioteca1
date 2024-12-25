from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Livro(db.Model):
    __tablename__ = 'livros'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    categoria = db.Column(db.String(100))
    editora = db.Column(db.String(100))
    edicao = db.Column(db.String(50))
    ano = db.Column(db.Integer)
    indicacao = db.Column(db.String(150))

    def __repr__(self):
        return f"<Livro {self.titulo}>"

class Aluno(db.Model):
    __tablename__ = 'alunos'
    
    matricula = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Aluno {self.nome}>"

class Emprestimo(db.Model):
    __tablename__ = 'emprestimos'
    
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.matricula'), nullable=False)
    livro_id = db.Column(db.Integer, db.ForeignKey('livros.id'), nullable=False)
    data_emprestimo = db.Column(db.Date, nullable=False)
    data_devolucao = db.Column(db.Date)

    aluno = db.relationship('Aluno', backref='emprestimos')
    livro = db.relationship('Livro', backref='emprestimos')

    def __repr__(self):
        return f"<Emprestimo Aluno: {self.aluno.nome}, Livro: {self.livro.titulo}>"
