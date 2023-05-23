
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
"""
Contagem de Letras Nome do Usuário:
"""







entrada = input('Digite seu primeiro nome: ')

if (len(entrada)) <= 4 :
    print('Seu nome é muito curto.')
elif(len(entrada)) == 6 :
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')    

nome = input('Digite seu nome:')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4 :
        print('Seu nome é muito curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6 :
        print('Seu nome é normal')
    else :
        print('Seu nome é muito grande.')
else:
    print('Digite ao menos uma letra do seu nome.')    

nome = input('Digite seu nome: ')
tamanho_nome = (len(nome))

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é muito curto')
    elif tamanho_nome >=5 and tamanho_nome <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')        
else:
    print('Por faovr, digite mais que uma letra.')    

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)


if tamanho_nome > 1:
    if tamanho_nome <= 4 :
        print('Seu nome é muito pequeno')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande.')      
else:
    print('Por favor, digite mais de uma letra.')