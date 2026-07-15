from funcionarios import faz_cadastro, mostra_cadastro_prévio
import script_sql

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
        else:
            print("obrigado")
            break

if __name__ == "__main__":
    main()
