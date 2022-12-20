try:
    novo_texto = str()
    escolhaUsuario = str(input('Informe o diretório do arquivo que você quer ler: '))
    print('Opções:\n1 - Remover maiúsculas\n2 - Trocar caracteres\n3 - Retirar acentos e caracteres especiais')
    escolhaDoisUsuario = int(input('\nO que você deseja fazer no texto? '))
    arquivo = open(f'{escolhaUsuario}.txt', encoding='utf-8', mode='r')
    texto = arquivo.read()
    if escolhaDoisUsuario == 1:
        novo_texto = texto.lower()
    elif escolhaDoisUsuario == 2:
        escolhaCaracteres = str(input('Escolha um caractere para trocar e outro para substituir (Informe um caractere, aperte espaço, e informe outro caractere): '))
        novosCaracteres = escolhaCaracteres.split()
        novo_texto = texto.replace(novosCaracteres[0], novosCaracteres[1])
    elif escolhaDoisUsuario == 3:
        novo_texto = texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ç', 'c').replace('ã', 'a').replace('õ', 'o').replace('â', 'â').replace('ê', 'e').replace('ô', 'o')
    else:
        print('Escolha uma opção válida.')
    arquivo.close()
    escolhaTresUsuario = int(input('Você deseja criar um novo arquivo ou substituir o existente?\n1 - Criar novo arquivo\n2 - Substituir arquivo existente\nEscolha digitando o número da opção desejada: '))
    if escolhaTresUsuario == 2:
        arquivo = open(escolhaUsuario, encoding='utf-8', mode='w')
        arquivo.write(novo_texto)
        arquivo.close()
    elif escolhaTresUsuario == 1:
        escolhaQuatroUsuario = str(input('Escolha o nome do novo arquivo: '))
        if escolhaQuatroUsuario == escolhaUsuario:
            print('Um arquivo com esse nome já existe. Informe outro nome para o novo arquivo.')
            exit()
        else:
            arquivo_novo = open(f'{escolhaQuatroUsuario}.txt', encoding='utf-8', mode='w')
            arquivo_novo.write(novo_texto)
            arquivo_novo.close()
    else:
        print('Escolha uma opção válida.')
    print(novo_texto)
except FileNotFoundError:
    print('Arquivo não encontrado.')
except KeyboardInterrupt:
    print('\nVocê encerrou o programa.')
