import random
import string

# Usando a biblioteca string para gerar os caracteres que serão utilizados.
letras_min = string.ascii_lowercase
letras_mai = string.ascii_uppercase
numeros = string.digits

# Definindo simbolos manualmente. A biblioteca string possui caracteres demais, preferi simplificar.
simbolos = '!#$%&=@?'

def gerador(tamanho):
    # Juntando todos os caracteres em uma string
    tudo = letras_mai + letras_min + numeros + simbolos
    # Gerando uma senha aleatoria com o tamanho definido
    temp = random.sample(tudo, tamanho)
    # Juntando a senha gerada em uma string
    password = "".join(temp)
    return password

# Recebendo o tamanho da senha a ser gerada
tamanho = int(input('Digite o tamanho da senha: '))
# Gerando a senha
senha = gerador(tamanho)
# Imprimindo a senha gerada
print(senha)
