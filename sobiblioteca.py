import os
from livro import Livro

livros = []
cod = 0

while True:
    print('\n*******************************************')
    print('*********Escolha a opção desejada!*********')
    print('*******************************************')
    print('(1) Cadastrar livro\n(2) Consultar livros cadastrados\n(3) Alugar livro\n(4) Devolver livro\n(5) Excluir livro\n(6) Encerrar sistema')
    op = input('Opção: ')

    if op == '6':
        break
    elif op == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        cod += 1
        titulo = input('Título: ')
        autor = input('Autor: ')
        editora = input('Editora: ')
        ano = input('Ano: ')
        livro = Livro(cod, titulo, autor, editora, ano)
        livros.append(livro)
    elif op == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(0, len(livros)):
            print(f'\nCódigo: {livros[i].codigo:03.0f}')
            print(f'Título: {livros[i].titulo}')
            print(f'Autor: {livros[i].autor}')
            print(f'Editora: {livros[i].editora}')
            print(f'Ano: {livros[i].ano}')
            print(f'Disponibilidade: {livros[i].disponivel}')

