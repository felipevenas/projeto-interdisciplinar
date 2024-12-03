import sys
import os
from entities.User import User
from entities.Materials import Materials
from entities.Wallet import Wallet

def main():

    material = Materials()
    wallet = Wallet()
    i = 1
    
    while (i != 0):

        print("======== Bem-vindo a EcoTroca ========")
        print()
        print("1: Login")
        print("2: Registre-se")
        print("3: Informações")
        print("0: Sair")
        i = int(input("Escolha uma opção: "))

        print()

        if i == 1:

            username = input("Usuário: ")
            password = int(input("Senha: "))
            print()

        elif i == 2:

            cpf = input("CPF: ")
            full_name = input("Nome completo: ")
            username = input("Nome de usuário: ")
            password = int(input("Senha numérica: "))
            user = User(full_name, username, password, cpf)
            print()

        elif i == 3:

            print("1. Toque na tela - ")
            print("2. Faça seu Login ou Registre-se - ")
            print("3. Selecione (Depositar Materiais) - ")
            print("4. Escolha o tipo de material que será depositado - ")
            print("5. Aguarde a luz verde ascender - ")
            print("6. Despeje seus materiais no local informado - ")
            print("7. A máquina irá pesar, calcular e adicionar suas moedas na sua carteira virtual - ")
            print("8. Troque suas moedas por itens na nossa loja.")
            print()
            continue
        
        elif i == 0:

            print("Sistema encerrado.")
            break

        else:

            print("Opção inválida.")
            continue

        while (i != 0):
            print("O que irá fazer agora?")
            print("1: Depositar material")
            print("2: Carteira")
            print("3: Loja")
            print("0: Sair")
            i = int(input("Escolha uma opção: "))

            print()

            if i == 1:
                print("LED_VERMELHO")
                print("-")
                print("Tipo do material que será depositado:")
                print("1: Garrafa Plástica")
                print("2: Lata de Alumínio")
                print("3: Jornal e Revistas")
                tipo_material = int(input("Escolha o tipo do material: "))

                qntd_material = int(input("Quantidade que será depositada: "))

                if tipo_material == 1:
                    earn = material.get_plastic() * qntd_material
                elif tipo_material == 2:
                    earn = material.get_aluminium() * qntd_material
                else:
                    earn = material.get_paper() * qntd_material

                wallet.add_wallet(earn)

                print()
                print("LED_VERDE")
                print("-")
                print("Despeje seu(s) material(s) no local indicado...")
                print("---")
                print("---")
                print("---")
                print("EcoTroca realizada com sucesso!")
                print(f"+R$ {earn:.2f} foram adicionados em sua carteira.")
                print()

            elif i == 2:

                print(f"Saldo disponível: R${wallet.get_balance():.2f}")
                print()

            elif i == 3:

                print("Itens disponíveis:")
                print("1: Gift Card - R$20.00")
                print("2: Vale Ingresso no Cinema - R$15.00")
                print("3: Vale Passagem de Metrô - R$2.50")
                print()

            elif i == 0:

                print("Sistema encerrado.")
                return
            
            else:

                print("Opção inválida.")


if __name__ == "__main__":
    main()