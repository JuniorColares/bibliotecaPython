import os
from livro import Livro

livros = []
cod = 0

while True:
    lpesquisa = []
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n*******************************************')
    print('*********Escolha a opção desejada!*********')
    print('*******************************************')
    print('(1) Cadastrar livro\n(2) Consultar livros cadastrados\n(3) Pesquisar livro\n(4) Alugar livro\n(5) Devolver livro\n(6) Editar livro\n(7) Excluir livro\n(8) Encerrar sistema')
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
            livros[i].mostrarLivro()
        c = input('')
    elif op == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        pesquisa = input('Qual livro está procurando: ')
        for i in range(0, len(livros)):
            if pesquisa in livros[i].titulo:
                lpesquisa.append(livros[i])
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(0, len(lpesquisa)):
            lpesquisa[i].mostrarLivro()
        c = input('')
    elif op == '4':
        codigo = int(input('Informe o código do livro que deseja alugar: '))
        for i in range(0, len(livros)):
            if codigo == livros[i].codigo:
                livros[i].alugarLivro()