class Livro:
    def __init__(self, codigo, titulo, autor, editora, ano, disponivel = 'SIM'):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.disponivel = disponivel

    def mostrarLivro(self):
        print(f'\nCódigo: {self.codigo:03.0f}')
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Editora: {self.editora}')
        print(f'Ano: {self.ano}')
        print(f'Disponibilidade: {self.disponivel}')
    
    def alugarLivro(self):
        if self.disponivel == 'SIM':
            self.disponivel = 'ALUGADO'
            print('Livro alugado com sucesso!')
            a = input('')
        else:
            print('Livro não disponível para aluguel!')
            a = input('')

    def devolverLivro(self):
        if self.disponivel == 'ALUGADO':
            self.disponivel = 'SIM'
            print('Operação realizada com sucesso!')
            a = input('')
        else:
            print('Livro não consta como alugado. Favor verificar o código.')
            a = input('')

    def alterarLivro(self, alteracao, alteracaov):
        if alteracao == 't':
            self.titulo = alteracaov
            print('Alteração feita com sucesso!')
        elif alteracao == 'a':
            self.autor = alteracaov
            print('Alteração feita com sucesso!')
        elif alteracao == 'e':
            self.editora = alteracaov
            print('Alteração feita com sucesso!')
        elif alteracao == 'an':
            self.ano = alteracaov
            print('Alteração feita com sucesso!')
        else:
            print('Alteração inválida')