from funcionarios import faz_cadastro, mostra_cadastro_prévio
from script_sql import *
import time

def main():
    print("===================================================")
    print("--------- Funcionários - Banco de Dados -----------")
    print("===================================================")
    print()
    escolha = input("Deseja realizar algum cadastro de funcinário?[s/n]: ").strip().lower()[0]
    while True:
        if escolha == "s":
            funcionario = faz_cadastro()
            mostra_cadastro_prévio(funcionario)
            print()
            print("Vamos fazer a inserção em nosso banco de dados...")
            insere_dados_funcionario_na_tabela(funcionario)
            print("Aguarde um instante...")
            time.sleep(2)
            print("Dados salvos com sucesso. Muito Obrigado!")
            break
        else:
            print("obrigado")
            break

if __name__ == "__main__":
    main()
