import tkinter as tk
from tkinter import messagebox, ttk
import requests

def buscar_informacoes():
    query = ip_entry.get().strip()
    search_type = search_option.get()

    if not query:
        messagebox.showwarning("Aviso", "Por favor, insira um endereço IP ou hostname.")
        return

    try:
        response = requests.get(f"http://ip-api.com/json/{query}")
        data = response.json()

        if data['status'] == "fail":
            messagebox.showinfo("Resultado", f"O {search_type.lower()} {query} não foi encontrado.")
            return

        # Exibir as informações obtidas
        info_text = (
            f"{search_type}: {data.get('query', 'N/A')}\n"
            f"Cidade: {data.get('city', 'N/A')}\n"
            f"Região: {data.get('regionName', 'N/A')}\n"
            f"País: {data.get('country', 'N/A')}\n"
            f"Localização: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}\n"
            f"Organização: {data.get('isp', 'N/A')}\n"
        )

        result_label.config(text=info_text)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao buscar as informações: {e}")

def colar_texto():
    ip_entry.delete(0, tk.END)  # Limpa o campo de entrada
    ip_entry.insert(0, root.clipboard_get())  # Cola o conteúdo da área de transferência

# Configuração da interface gráfica
root = tk.Tk()
root.title("Informações do IP")
root.geometry("450x350")
root.configure(bg="#f0f0f5")

# Carregar o ícone (formato .ico)
icon_path = "icon.ico"  # Caminho para o seu ícone
root.iconbitmap(icon_path)

# Estilo do botão
style = ttk.Style()
style.configure("TButton", background="#007aff", foreground="white", font=("Helvetica", 12))
style.map("TButton", background=[("active", "#0051a8")])

# Adicionando um título
title_label = tk.Label(root, text="Consulta de IP/Hostname", bg="#f0f0f5", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Opções de pesquisa
search_option = tk.StringVar(value="IP")  # Opção padrão
option_menu = ttk.OptionMenu(root, search_option, "IP", "IP", "Hostname")
option_menu.pack(pady=5)

# Campo de entrada
tk.Label(root, text="Insira o endereço IP ou hostname:", bg="#f0f0f5").pack(pady=5)
entry_frame = tk.Frame(root, bg="#f0f0f5")
entry_frame.pack(pady=5)

ip_entry = tk.Entry(entry_frame, font=("Helvetica", 12))
ip_entry.pack(side=tk.LEFT, padx=5)

# Botão de colar
paste_button = ttk.Button(entry_frame, text="Colar", command=colar_texto)
paste_button.pack(side=tk.LEFT, padx=5)
paste_button.config(width=6)  # Ajusta a largura do botão para um tamanho menor

# Botão de busca
buscar_button = ttk.Button(root, text="Buscar", command=buscar_informacoes)
buscar_button.pack(pady=10)

result_label = tk.Label(root, text="", bg="#f0f0f5", justify=tk.LEFT, font=("Helvetica", 12))
result_label.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
