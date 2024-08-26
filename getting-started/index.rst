===============
Getting started
===============

.. toctree::
   :maxdepth: 5

   setup-building
   fixing-issues
   git-boot-camp
   pull-request-lifecycle
   getting-help
import tkinter as tk
import json
import requests

class Equipamento:
    def __init__(self, nome, tipo, localizacao):
        self.nome = nome
        self.tipo = tipo
        self.localizacao = localizacao

class PMOC:
    def __init__(self):
        self.equipamentos = []

    def adicionar_equipamento(self, equipamento):
        self.equipamentos.append(equipamento)

    def listar_equipamentos(self):
        for equipamento in self.equipamentos:
            print(f"Nome: {equipamento.nome}, Tipo: {equipamento.tipo}, Localização: {equipamento.localizacao}")

    def salvar_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "w") as arquivo:
            dados = []
            for equipamento in self.equipamentos:
                dados.append({
                    "nome": equipamento.nome,
                    "tipo": equipamento.tipo,
                    "localizacao": equipamento.localizacao
                })
            json.dump(dados, arquivo)

    def carregar_de_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
            for item in dados:
                equipamento = Equipamento(item["nome"], item["tipo"], item["localizacao"])
                self.adicionar_equipamento(equipamento)

    def enviar_dados_via_api(self, equipamento):
        url = "https://api.example.com/pmoc/equipamentos"
        payload = {
            "nome": equipamento.nome,
            "tipo": equipamento.tipo,
            "localizacao": equipamento.localizacao
        }
        response = requests.post(url, json=payload)

        if response.status_code == 201:
            print("Dados enviados com sucesso!")
        else:
            print(f"Erro ao enviar dados (status code {response.status_code}): {response.text}")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PMOC - Gestão de Equipamentos")

        self.label_nome = tk.Label(root, text="Nome:")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_tipo = tk.Label(root, text="Tipo:")
        self.label_tipo.pack()
        self.entry_tipo = tk.Entry(root)
        self.entry_tipo.pack()

        self.label_localizacao = tk.Label(root, text="Localização:")
        self.label_localizacao.pack()
        self.entry_localizacao = tk.Entry(root)
        self.entry_localizacao.pack()

        self.button_adicionar = tk.Button(root, text="Adicionar Equipamento", command=self.adicionar_equipamento)
        self.button_adicionar.pack()

        self.pmoc = PMOC()

    def adicionar_equipamento(self):
        nome = self.entry_nome.get()
        tipo = self.entry_tipo.get()
        localizacao = self.entry_localizacao.get()

        equipamento = Equipamento(nome, tipo, localizacao)
        self.pmoc.adicionar_equipamento(equipamento)
        self.pmoc.enviar_dados_via_api(equipamento)

        print(f"Equipamento adicionado: {nome}, {tipo}, {localizacao}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
