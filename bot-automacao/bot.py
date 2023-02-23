from typing import KeysView
from botcity.core import DesktopBot

class Bot(DesktopBot):
    def action(self, execution=None):
        # Executando a aplicação Small Start
        self.execute(r'C:\Users\Public\Desktop\Small Start.lnk')

        # Preenchendo a senha
        if not self.find("senha", matching=0.97, waiting_time=10000):
            self.not_found("senha")
        self.paste("1234")
        self.enter()

        # Navegando para a tela de estoque
        if not self.find("estoque", matching=0.97, waiting_time=10000):
            self.not_found("estoque")
        self.click()

        # Selecionando o ICMS
        if not self.find("icms", matching=0.97, waiting_time=10000):
            self.not_found("icms")
        self.click()

        # Selecionando a Mercadoria
        if not self.find("mercadoria", matching=0.97, waiting_time=10000):
            self.not_found("mercadoria")
        self.click(),

        # Selecionando Mercadoria
        self.type_down()
        self.type_down()
        self.enter()

        # Selecionando Origem
        self.tab()
        self.tab()
        self.tab()
        self.tab()
        self.type_down()
        self.type_down()

        # Selecionando CSCSON
        self.tab()
        self.type_down()
        self.type_down()
        self.type_down()

        # Selecionando CFOP
        if not self.find("cfop", matching=0.97, waiting_time=10000):
            self.not_found("cfop")
        self.click_relative(121, 13)
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.enter()

        # Selecionando CSCSON NFC-e
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        if not self.find("ok", matching=0.97, waiting_time=10000):
            self.not_found("ok")
        self.click()

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()
    input("Pressione Enter para sair...")
