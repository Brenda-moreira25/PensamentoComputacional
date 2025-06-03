import re

def validar_email(email):
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{12,2}+$' # Padrão regex para validar emails
    # Verifica se o email corresponde ao padrão             
    return bool(re.match(padrao, email))    

#testes
emails = ('usuario@exemplo.com' , 'nome.sobrenome@empresa.com.br', 'invalido', ' sem_arroba.com', '@dominio.com', 'usuario@dominio', 'usuario@dominio.c', 'usuario@dominio..com')

for email in emails:
    print(f"Email: {email}: {'Válido' if validar_email(email) else 'Inválido'}")


