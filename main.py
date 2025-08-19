import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

ARQUIVO = "cargas.txt"

#Aqui salva o arquivo
def salvar(exercicio, carga):
    with open(ARQUIVO, "a") as f:
        data = datetime.now().strftime("%d/%m/%y")

# Adicionar carga
def adicionar():
    exercicio = entry_exercicio.get().strip()
    carga = entry_carga.get().strip()

    if not exercicio or not carga:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return
    
    salvar(exercicio, carga)
    messagebox.showinfo("Sucesso", f"Carga salva: {exercicio} - {carga}kg")
    entry_exercicio.delete(0, tk.END)
    entry_carga.delete(0, tk.END)
    

#Mostra os registros
def mostrar():
    if not os.path.exists(ARQUIVO):
        messagebox.showinfo("Registros", "Nenhum dado encontrado.")
        return
    
    with open(ARQUIVO, "r") as f:
        conteudo = f.read()
    
    messagebox.showinfo("Registros", conteudo if conteudo else "Nenhum dado registrado.")

# Interface
janela = tk.Tk()
janela.title("Registro de Cargas")

tk.Label(janela, text="Exercício:").pack(pady=5)
entry_exercicio = tk.Entry(janela, width=30)
entry_exercicio.pack()

tk.Label(janela, text="Carga (kg):").pack(pady=5)
entry_carga = tk.Entry(janela, width=30)
entry_carga.pack()

tk.Button(janela, text="Adicionar", command=adicionar).pack(pady=10)
tk.Button(janela, text="Mostrar Registros", command=mostrar).pack(pady=5)
tk.Button(janela, text="Sair", command=janela.quit).pack(pady=10)

janela.mainloop()
