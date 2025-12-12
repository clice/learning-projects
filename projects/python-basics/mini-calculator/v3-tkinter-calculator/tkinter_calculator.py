import tkinter as tk
from tkinter import messagebox


# Classe que cria uma interface gráfica de calculadora usando Tkinter
class CalculadoraGUI:
    
    # Cria a janela principal e os componentes da calculadora
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Calculadora Simples")
        
        # Cria um campo de texto para exibir a expressão e o resultado
        self.display = tk.Entry(self.janela, width=20, font=("Arial", 18), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Define os botões da calculadora
        botoes = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
        ]
        
        # Cria e posiciona os botões na janela
        linha = 1
        coluna = 0
        
        for texto in botoes:
            # Cria um botão e associa a função de clique
            botao = tk.Button(
                self.janela, 
                text=texto, 
                width=5, 
                height=2, 
                font=("Arial", 14),
                command=lambda t=texto: self.clique_botao(t)  # Usa lambda para passar o texto do botão
            )
            botao.grid(row=linha, column=coluna, padx=5, pady=5)
            
            # Atualiza a posição para o próximo botão
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1
                
        # Cria o botão de igual em uma linha separada
        botao_igual = tk.Button(
            self.janela, 
            text="=", 
            width=22, 
            height=2, 
            font=("Arial", 14),
            command=self.calcular  # Chama a função calcular ao clicar
        )
        botao_igual.grid(row=linha, column=0, columnspan=4, padx=5, pady=5)
        

    # Função chamada quando um botão é clicado
    def clique_botao(self, texto):
        # Limpa o display se o botão "C" for clicado
        if texto == "C":            
            self.display.delete(0, tk.END)
        # Adiciona o texto do botão ao display
        else:
            self.display.insert(tk.END, texto)
            
            
    # Função para calcular a expressão no display
    def calcular(self):
        expressao = self.display.get()
        try:
            # Avalia a expressão e exibe o resultado
            resultado = eval(expressao)
            # Limpa o display e insere o resultado
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(resultado))
        except Exception as e:
            # Mostra uma mensagem de erro em caso de exceção
            messagebox.showerror("Erro", "Expressão inválida")  
            
            
    # Inicia o loop principal da interface gráfica
    def iniciar(self):
        self.janela.mainloop()
        
        
if __name__ == "__main__":
    calculadora = CalculadoraGUI()
    calculadora.iniciar()