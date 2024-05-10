class Livro:
    def __init__(self, titulo, autor, genero, estoque):
        self.nome = titulo
        self.autor = autor
        self.ano = genero
        self.estoque = estoque

    def ver_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Gênero: {self.genero}")
        print(f"Estoque: {self.estoque}")

    def emprestar_livro(self):
        if self.estoque > 0:
            self.estoque -= 1
            print("O empréstimo foi efetuado!")
        else:
            print("Não há o livro selecionado no estoque! T-T")
        
    def devolver_livro(self):
        self.estoque += 1
        print("O livro foi devolvido!")