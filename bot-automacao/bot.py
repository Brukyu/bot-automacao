from botcity.core import DesktopBot

class Bot(DesktopBot):

    # Nomes descritivos para valores literais
    PASSWORD_FIELD = "senha"
    STOCK_OPTION = "estoque"
    ICMS_OPTION = "icms"
    MERCADORIA_OPTION = "mercadoria"
    CFOP_OPTION = "cfop"
    OK_BUTTON = "ok"
    MAX_MATCHING = 0.97
    WAITING_TIME = 10000
    CFOP_RELATIVE_POSITION = (121, 13)

    def action(self, execution=None):
        self.open_small_start()
        self.fill_password()
        self.go_to_stock_screen()
        self.select_icms_option()
        self.select_mercadoria_option()
        self.select_mercadoria()
        self.select_origem()
        self.select_cscson()
        self.select_cfop()
        self.click_ok_button()

    def open_small_start(self):
        """Executa a aplicação Small Start."""
        self.execute(r"C:\Users\Public\Desktop\Small Start.lnk")

    def fill_password(self):
        """Preenche a senha."""
        if not self.find(self.PASSWORD_FIELD, matching=self.MAX_MATCHING, waiting_time=self.WAITING_TIME):
            self.not_found(self.PASSWORD_FIELD)
        self.paste("1234")
        self.enter()

    def go_to_stock_screen(self):
        """Navega para a tela de estoque."""
        if not self.find(self.STOCK_OPTION, matching=self.MAX_MATCHING, waiting_time=self.WAITING_TIME):
            self.not_found(self.STOCK_OPTION)
        self.click()

    def select_icms_option(self):
        """Seleciona o ICMS."""
        if not self.find(self.ICMS_OPTION, matching=self.MAX_MATCHING, waiting_time=self.WAITING_TIME):
            self.not_found(self.ICMS_OPTION)
        self.click()

    def select_mercadoria_option(self):
        """Seleciona a opção Mercadoria."""
        if not self.find(self.MERCADORIA_OPTION, matching=self.MAX_MATCHING, waiting_time=self.WAITING_TIME):
            self.not_found(self.MERCADORIA_OPTION)
        self.click()

    def select_mercadoria(self):
        """Seleciona Mercadoria."""
        self.type_down()
        self.type_down()
        self.enter()

    def select_origem(self):
        """Seleciona Origem."""
        self.tab()  
        self.tab()
        self.tab()
        self.tab()
        self.type_down()
        self.type_down()

    def select_cscson(self):
        """Seleciona CSCSON."""
        self.tab()
        self.type_down()
        self.type_down()
        self.type_down()

    def select_cfop(self):
        """Seleciona CFOP."""
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

        #Seleciona CSCSON para NFC-e."""
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
        self.type_down()
    
    def click_ok_button(self):
        """Clica no botão OK após preencher os dados."""
        if not self.find("ok", matching=0.97, waiting_time=10000):
            self.not_found("ok")
        self.click()



def not_found(self, label):
    print(f"Element not found: {label}")

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()
    input("Pressione Enter para sair...")
