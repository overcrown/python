contador1 = contador2 = 0
lista = list()
arquivo = open('C:/users/gabri/desktop/debug.txt','r')
for c in arquivo:
    print(c.strip())
    lista.append(c)
arquivo.close()

while True:
    print(len(lista))
    print('--------MENU DE OPÇÕES---------')
    cadastro = str(input('(\033[32m1\033[m) Se você deseja cadastrar alguém.'
                    '\n(\033[32m2\033[m) Se você deseja buscar algum cadastro.'
                    '\n(\033[32m3\033[m) Se você deseja sair.'
                    '\n(\033[32m4\033[m) Se você deseja apagar o registro de algum cliente.'
                    '\n(\033[32m5\033[m) Se você deseja visualizar todos os registros.'
                    '\nDigite: ')).upper()
    if cadastro == '3':
        break
    if cadastro == '1':
        while True:
            lista.clear()
            arquivo = open("C:/users/gabri/desktop/debug.txt", "a")
            print('-='*30)
            nome = str(input('Nome: ')).upper()
            rg = str(input('RG: ')).upper()
            while True:
                print('Digite apenas números!')
                rg = int(input('RG: '))
                if rg.isnumeric():
                    break
            arquivo.write(f'  Nome: {nome}')
            arquivo.write(f'  RG: {rg}')
            arquivo.write('\n')
            arquivo.close()
            arquivo = open('C:/users/gabri/desktop/debug.txt','r')
            for c in arquivo:
                lista.append(c)
            arquivo.close()
            arquivo = open('C:/users/gabri/desktop/debug.txt', 'w')
            for c in lista:
                arquivo.write(c)
            arquivo.close()
            answer_1 = str(input('Você quer continuar[Sim/Não]? ')).upper()[0]
            if answer_1 == 'N':
                break
    if cadastro == '2':
        for c in lista:
            print(c.strip())
        while True:
            contador1 = 0
            print('='*40)
            print('BUSCADOR'.center(40))
            print('='*40)
            arquivo = open('C:/users/gabri/desktop/debug.txt', 'r')
            cliente = str(input('Qual cliente você deseja buscar? ')).upper()
            for c in lista:
                if cliente in c:
                    print(c)
                else:
                    contador1 += 1
            if contador1 == len(lista):
                print('Cliente não encontrado!')
            print('-'*40)
            answer_2 = str(input('Quer continuar a busca[Sim/Nao]? ')).upper()
            if answer_2 == 'NAO':
                break
            arquivo.close()
    if cadastro == '4':
        arquivo = open('C:/users/gabri/desktop/debug.txt', 'r')
        while True:
            contador2 = 0
            option = str(input('Qual cliente você deseja apagar? ')).upper()
            for c in lista:
                contador2 += 1
                if option in c:
                    print(c)
                    answer_3 = str(input('Deseja excluir[Sim/Nao]? ')).upper()
                    if answer_3 == 'SIM':
                        print(contador2)
                        del lista[contador2-1]
                        contador1 -= 1
                        print('Registro excluído!')
                else:
                    contador1 += 1
            if contador1 == len(lista):
                print('Cliente não encontrado!')
            print('-'*40)
            answer_4 = str(input('Deseja apagar mais um registro[Sim/Nao]? ')).upper()
            if answer_4 == 'NAO':
                break
            elif answer_4 == 'SIM':
                print('-'*40)
        arquivo.close()
        arquivo = open('C:/users/gabri/desktop/debug.txt', 'w')
        for c in lista:
            arquivo.write(c)
        arquivo.close()
    if cadastro == '5':
        arquivo = open('C:/users/gabri/desktop/debug.txt', 'r')
        for c in arquivo:
            print(c)
        arquivo.close()
print('\033[35mFIM\033[m')