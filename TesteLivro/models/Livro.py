class Livro:
    def __init__(self, titulo, autor, ano_publicacao, numero_pag, pag_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_pag = numero_pag
        self.pag_atual = pag_atual

    def tt_titulo(self):
        print(f"O nome do livro é {self.titulo}")

    def escritor(self):
        print(f"O nome do autor deste livro é {self.autor}")

    def get_ano_publicacao(self):
        self.ano_publicacao = self.ano_publicacao

    def numero_pag(self):
        self.numero_pag = self.numero_pag

    def pag_atual(self):
        self.pag_atual = self.pag_atual

    def avancar_pag(self):
        if self.pag_atual < self.numero_pag:
            self.pag_atual +=1
        print(f"Página  {self.pag_atual} / {self.numero_pag} ")

    def voltar_pag(self):
            if self.pag_atual > self.numero_pag:
                self.pag_atual-=1
            print(f"Página {self.pag_atual}/{self.numero_pag}")

    def infos(self):
        print(f"O livro {self.titulo} foi publicado em {self.ano_publicacao} por {self.autor}")
        print(f"Contém {self.numero_pag} atualmente está na página {self.pag_atual}")
    

    
