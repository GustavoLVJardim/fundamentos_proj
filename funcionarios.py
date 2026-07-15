
def faz_cadastro():
    print("===================================================")
    print("------------- Funcionários - Cadatro --------------")
    print("===================================================")
    while True:
        try:
            nome = input("Digite o seu nome completo: ").strip().title()
            email = input("Digite o email: ").strip().lower()
            depto = input("Digite o departamento: ").strip().capitalize()
            
            return nome, email, depto
        except Exception as e:
            print(f"[ERRO]: alguma informação pode estar incorreta. {e} ")
            continue
    

def mostra_cadastro_prévio(tupla_funcionário):
    print("===================================================")
    print("------------- Funcionários - Cadatro --------------")
    print("===================================================")
    print()
    print(f"O funcionário cadastrado foi:\nnome: {tupla_funcionário[0]}\nemail: {tupla_funcionário[1]}\ndepartamento: {tupla_funcionário[2]}")
    print()
    