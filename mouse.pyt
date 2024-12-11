import tkinter as tk
from pynput.mouse import Listener

# Função que vai atualizar as coordenadas do mouse
def on_move(x, y):
    # Atualiza a posição do mouse no terminal (fora da janela)
    print(f"Posição do mouse: X = {x}, Y = {y}")

# Configura o listener para monitorar o movimento do mouse
listener = Listener(on_move=on_move)
listener.start()

# Criação da interface gráfica com Tkinter
root = tk.Tk()
root.title("Interface Tkinter")
root.geometry("400x200")

# Exibe uma mensagem simples
label = tk.Label(root, text="Movimente o mouse para ver as coordenadas no console.", font=("Arial", 14))
label.pack(pady=50)

# Inicia o loop da interface gráfica
root.mainloop()
