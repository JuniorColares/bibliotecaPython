import os
from livro import Livro

livros = []
cod = 0

def inicioPrograma():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n*******************************************')
    print('*********Escolha a opção desejada!*********')
    print('*******************************************')
    print('(1) Cadastrar livro\n(2) Consultar livros cadastrados\n(3) Pesquisar livro\n(4) Alugar livro\n(5) Devolver livro\n(6) Editar livro\n(7) Excluir livro\n(8) Encerrar sistema')

def formaLivro(cod):
    os.system('cls' if os.name == 'nt' else 'clear')
    titulo = input('Título: ')
    autor = input('Autor: ')
    editora = input('Editora: ')
    ano = input('Ano: ')
    livro = Livro(cod, titulo, autor, editora, ano)
    return livro


while True:
    lpesquisa = []
    inicioPrograma()
    op = input('Opção: ')
    
    if op == '8':
        break
    elif op == '1':
        cod += 1
        livro = formaLivro(cod)
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
    elif op == '5':
        codigo = int(input('Informe o código do livro que deseja devolver: '))
        for i in range(0, len(livros)):
            if codigo == livros[i].codigo:
                livros[i].devolverLivro()
    elif op == '6':
        codigo = int(input('Informe o código do livro que deseja alterar: '))
        for i in range(0, len(livros)):
            if codigo == livros[i].codigo:
                alteracao = input('(t) Título / (a) Autor / (e) Editora / (an) Ano\nO que deseja alterar: ').lower().strip()
                alteracaov = input('Qual o novo valor: ')
                livros[i].alterarLivro(alteracao, alteracaov)
    elif op == '7':
        codigo = int(input('Informe o código do livro que deseja excluir: '))
        for i in range(0, len(livros)):
            if codigo == livros[i].codigo:
                conf = input(f'Tem certeza que deseja excluir o livro {livros[i].titulo} de {livros[i].autor}? (s/n) ').lower().strip()
                if conf == 's':
                    del(livros[i])
                    print('Livro excluído')
                    a = input('')
    else:
        print('Opção inválida!')


print('\nSISTEMA ENCERRADO!')

