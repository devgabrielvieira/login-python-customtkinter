import customtkinter as ctk

# Criando janela
janela = ctk.CTk()

# Configurando a nossa janela principal
# Colocando titulo
janela.title("Login")
# Dimensão inicial da janela
janela.geometry("500x300")

# Customizando tema da nossa aplicacao
janela._set_appearance_mode("dark")
# janela._set_appearance_mode("ligth")
# janela._set_appearance_mode("system")

# ctk.set_default_color_theme("dark-blue")

# Criando nova janela
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="blue")
    nova_janela.geometry("500x350")

btn_novatela = ctk.CTkButton(master=janela, text="Abrir nova Janela", command=nova_tela).place(x=180, y=200)

# Criando função Clique
def Clique():
    print("Fazer Login")

texto = ctk.CTkLabel(janela, text="Fazer Login")

email = ctk.CTkEntry(janela, 
                               placeholder_text="E-mail")

senha = ctk.CTkEntry(janela, 
                               placeholder_text="Senha", 
                               show="*")

botao = ctk.CTkButton(janela, text="Login", 
                                command=Clique)

texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

# Rodando a janela
janela.mainloop()
