import os
def processarResposta(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep} Claro, {nome}. {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep} Depende do seu empenho, {nome}. {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep} Quando você souber os 5 pilares de Python pode ser que esteja bom, porém e legal aplicar para uma vaga e testar seus conhecimentos, {nome}. {os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep} Voce pode estudar de varias maneiras, YouTube, livros e comunidades, {nome}. {os.linesep}')
    else:
        print(f'{os.linesep}{nome} somente 1, 2,3 e 4 são respostas válidas {os.linesep}')

def start():
    #apresentacao
    print('Ola, eu sou o Wall-E, assistente virtual!')
    #pegar o nome
    nome = input('Qual é o seu nome? ')
    #pedir o e-mail
    email = input('Qual é o seu e-mail? ')
    while True:  
    #oferecer menu
        resposta = input(f'O que gostaria de saber hoje?{os.linesep}[1] - Vale apena aprender Python?{os.linesep}[2] - Quanto tempo leva para aprender Python?{os.linesep}[3] - Quando vou saber que estou BOM o sulficiente para conseguir um emprego?{os.linesep}[4] - Onde me recomenda estudar Python para conseguir emprego?{os.linesep}')
        #processar a resposta
        processarResposta(resposta,nome)

if __name__ == '__main__':
    start()