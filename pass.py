import random
import string

def gerar_senha(tamanho=12):
    # Definindo os componentes da senha
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    
    # Combinar todos os componentes
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
    
    # Garantir que a senha contenha pelo menos um de cada tipo
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Preencher o restante da senha com caracteres aleatórios
    senha += random.choices(todos_caracteres, k=tamanho-4)
    
    # Embaralhar os caracteres para torná-la mais imprevisível
    random.shuffle(senha)
    
    # Retornar a senha como uma string
    return ''.join(senha)

# Testando o gerador de senhas
tamanho_senha = int(input("Digite o tamanho da senha que deseja (mínimo 6): "))
if tamanho_senha < 6:
    print("O tamanho mínimo da senha é 6.")
else:
    senha = gerar_senha(tamanho_senha)
    print("Senha gerada:", senha)
