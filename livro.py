class Livro:
    def __init__(self, codigo, titulo, autor, editora, ano, disponivel = 'SIM'):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.disponivel = disponivel