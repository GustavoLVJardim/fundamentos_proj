from funcionarios import faz_cadastro, mostra_cadastro_prévio
from script_sql import *
import time

def main():
    print("===================================================")
    print("--------- Funcionários - Banco de Dados -----------")
    print("===================================================")
    print()
    escolha = input("""
Digite 1 para realizar algum cadastro de funcinário: 
Digite 2 para realizar a remoção de cadastro de funcionário: 
Digite 3 para sair: """).strip()[0]
    match escolha:
        case "1":
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
        
        case "2":
            esquecer()
        
        case "3":
            exit()
        
        case _:
            print("opção inválida")

if __name__ == "__main__":
    main()
