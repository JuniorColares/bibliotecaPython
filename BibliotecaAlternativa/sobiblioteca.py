import os
from livro import Livro

titulol = open('titulo.txt', 'r')
titulos = []
for l in titulol:
    titulos.append(l.strip())
print(titulos)
titulol.close()

autorl = open('autor.txt', 'r')
autores = []
for l in autorl:
    autores.append(l.strip())
print(autores)
autorl.close()

editoral = open('editora.txt', 'r')
editoras = []
for l in editoral:
    editoras.append(l.strip())
print(editoras)
editoral.close()

anol = open('ano.txt', 'r')
anos = []
for l in anol:
    anos.append(l.strip())
print(anos)
anol.close()

codigol = open('codigo.txt', 'r')
codigos = []
for l in codigol:
    codigos.append(l.strip())
print(codigos)
codigol.close()

disponivell = open('disponivel.txt', 'r')
disponiveis = []
for l in disponivell:
    disponiveis.append(l.strip())
print(disponiveis)
disponivell.close()

cod = 0
while cod < len(codigos):
    cod += 1
print(cod)

titulol = open('titulo.txt', 'a')
autorl = open('autor.txt', 'a')
editoral = open('editora.txt', 'a')
anol = open('ano.txt', 'a')
codigol = open('codigo.txt', 'a')
disponivell = open('disponivel.txt', 'a')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n*******************************************')
    print('*********Escolha a opção desejada!*********')
    print('*******************************************')
    print('(1) Cadastrar livro\n(2) Consultar livros cadastrados\n(3) Pesquisar livro\n(4) Alugar livro\n(5) Devolver livro\n(6) Editar livro\n(7) Excluir livro\n(8) Encerrar sistema')
    op = input('Opção: ')

    if op == '8':
        break
    elif op == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        cod += 1
        titulo = input('Título: ')
        autor = input('Autor: ')
        editora = input('Editora: ')
        ano = input('Ano: ')
        livro = Livro(cod, titulo, autor, editora, ano)
        titulol.write(f"{livro.titulo}\n")
        titulos.append(livro.titulo)
        autorl.write(f"{livro.autor}\n")
        autores.append(livro.autor)
        editoral.write(f"{livro.editora}\n")
        editoras.append(livro.editora)
        anol.write(f"{livro.ano}\n")
        anos.append(livro.ano)
        codigol.write(f"{livro.codigo}\n")
        codigos.append(livro.codigo)
        disponivell.write(f"{livro.disponivel}\n")
        disponiveis.append(livro.disponivel)
    elif op == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(0, len(titulos)):
            print(f'\nCódigo: {int(codigos[i]):03.0f}\nTítulo: {titulos[i]}\nAutor: {autores[i]}\nEditora: {editoras[i]}\nAno: {anos[i]}\nDisponíbilidade: {disponiveis[i]}')
        c = input('')
    elif op == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        pesquisa = input('Qual livro está procurando: ')
        for i in range(0, len(titulos)):
            if pesquisa in titulos[i]:
                print(f'\nCódigo: {int(codigos[i]):03.0f}')
                print(f'Título: {titulos[i]}')
                print(f'Autor: {autores[i]}')
                print(f'Editora: {editoras[i]}')
                print(f'Ano: {anos[i]}')
                print(f'Disponibilidade: {disponiveis[i]}')
        os.system('cls' if os.name == 'nt' else 'clear')
        c = input('')
    elif op == '4':
        codigo = int(input('Informe o código do livro que deseja alugar: '))
        for i in range(0, len(titulos)):
            if codigo == int(codigos[i]):
                if disponiveis[i] == 'SIM':
                    disponiveis[i] = 'ALUGADO'
                    print('Livro alugado com sucesso!')
                    a = input('')
                else:
                    print('Livro não disponível para aluguel!')
                    a = input('')
    elif op == '5':
        codigo = int(input('Informe o código do livro que deseja devolver: '))
        for i in range(0, len(titulos)):
            if codigo == int(codigos[i]):
                if disponiveis[i] == 'SIM':
                    print('O livro não está alugado. Verifique o código!')
                    input('')
                else:
                    disponiveis[i] = 'SIM'
                    print('Livro devolvido com sucesso!')
                    a = input('')
    elif op == '6':
        codigo = int(input('Informe o código do livro que deseja alterar: '))
        for i in range(0, len(titulos)):
            if codigo == int(codigos[i]):
                alteracao = input('(t) Título / (a) Autor / (e) Editora / (an) Ano\nO que deseja alterar: ')
                alteracaov = input('Qual o novo valor: ')
                if alteracao == 't':
                    titulos[i] = alteracaov
                elif alteracao == 'a':
                    autores[i] = alteracaov
                elif alteracao == 'e':
                    editoras[i] = alteracaov
                elif alteracao == 'an':
                    anos[i] = alteracaov
    elif op == '7':
        codigo = int(input('Informe o código do livro que deseja excluir: '))
        for i in range(0, len(titulos)):
            if codigo == int(codigos[i]):
                conf = input(f'Tem certeza que deseja excluir o livro {titulos[i]} de {autores[i]}? (s/n) ')
                if conf == 's':
                    del(titulos[i])
                    del(autores[i])
                    del(editoras[i])
                    del(anos[i])
                    del(codigos[i])
                    del(disponiveis[i])
                    print('Livro excluído')
                    a = input('')
            continue
    else:
        print('Opção inválida!')

titulol.close()
editoral.close()
anol.close()
autorl.close()
disponivell.close()
codigol.close()

print('\nSISTEMA ENCERRADO!')