import json
import os

ARQUIVO = "cargas.json"

# Carregar dados
def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return {}

# Salvar dados
def salvar(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)

def menu():
    dados = carregar()
    
    while True:
        print("\n--- REGISTRO DE CARGAS ---")
        print("1. Adicionar novo exercício")
        print("2. Registrar carga em exercício existente")
        print("3. Mostrar exercícios")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do exercício: ")
            if nome not in dados:
                dados[nome] = []   # <<< CORRIGIDO AQUI
                print(f"✅ Exercício '{nome}' adicionado.")
            else:
                print("⚠️ Esse exercício já existe.")
            salvar(dados)

        elif opcao == "2":
            nome = input("Nome do exercício: ")
            if nome in dados:
                carga = input("Digite a carga (kg): ")
                dados[nome].append(carga)
                print(f"✅ Carga {carga}kg adicionada em '{nome}'.")
            else:
                print("❌ Exercício não encontrado.")
            salvar(dados)

        elif opcao == "3":
            if not dados:
                print("📂 Nenhum exercício cadastrado.")
            else:
                for ex, cargas in dados.items():
                    print(f"\n{ex}: {', '.join(cargas) if cargas else 'sem cargas ainda'}")

        elif opcao == "4":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida.")
