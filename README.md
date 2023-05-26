# Documentação do Código para Interface de Login Personalizada usando CustomTkinter

A seguir, está a documentação para o código Python que cria uma interface de login personalizada usando a biblioteca `customtkinter`.

## Introdução

O código fornecido demonstra a criação de uma janela de login personalizada usando a biblioteca `customtkinter`. Ele configura a aparência da janela, define um tema, cria widgets como rótulos, campos de entrada e botões, e implementa funcionalidades como a abertura de uma nova janela e a impressão de uma mensagem quando o botão de login é clicado.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos antes de executar o código:

- Python (versão 3.x recomendada) instalado no seu sistema.
- A biblioteca `customtkinter` instalada. Caso não esteja instalada, você pode instalá-la usando o comando `pip install customtkinter`.

## Código

Aqui está o código completo para criar uma interface de login personalizada:

```python
import customtkinter as ctk

# Criando a janela principal
janela = ctk.CTk()

# Configurando a janela principal
janela.title("Login")
janela.geometry("500x300")

# Customizando o tema da aplicação
janela._set_appearance_mode("dark")
# janela._set_appearance_mode("light")
# janela._set_appearance_mode("system")

# Criando uma nova janela
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="blue")
    nova_janela.geometry("500x350")

# Criando função para clique no botão de login
def Clique():
    print("Fazer Login")

# Criando os widgets
texto = ctk.CTkLabel(janela, text="Fazer Login")
email = ctk.CTkEntry(janela, placeholder_text="E-mail")
senha = ctk.CTkEntry(janela, placeholder_text="Senha", show="*")
botao = ctk.CTkButton(janela, text="Login", command=Clique)
btn_novatela = ctk.CTkButton(janela, text="Abrir nova Janela", command=nova_tela).place(x=180, y=200)

# Posicionando os widgets na janela
texto.pack(padx=10, pady=10)
email.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

# Executando a janela
janela.mainloop()
```

## Explicação do Código

1. O código começa importando a biblioteca `customtkinter` usando o alias `ctk`.

2. Em seguida, uma instância da janela principal é criada usando `ctk.CTk()` e atribuída à variável `janela`.

3. A configuração da janela principal é realizada, incluindo a definição do título da janela como "Login" e a configuração das dimensões iniciais para "500x300" pixels.

4. A aparência da aplicação é customizada usando o método `_set_appearance_mode()`. No exemplo fornecido, o modo escuro é utilizado, mas você também pode escolher entre os modos "light" ou "system" (que segue as configurações do sistema operacional).

5. A função `nova_tela()` é definida para criar uma nova janela

 quando o botão "Abrir nova Janela" for clicado. A nova janela é uma instância de `CTkToplevel` e é definida com uma cor de primeiro plano (foreground) azul.

6. Em seguida, a função `Clique()` é definida para ser chamada quando o botão de login for clicado. Neste exemplo, ela imprime a mensagem "Fazer Login" no console.

7. Diversos widgets são criados usando as classes fornecidas pela biblioteca `customtkinter`. Um rótulo `CTkLabel` com o texto "Fazer Login" é criado e armazenado na variável `texto`. Campos de entrada `CTkEntry` são criados para o email e senha, com texto de espaços reservados (placeholders) definidos. Um botão `CTkButton` com o texto "Login" é criado e associado à função `Clique()`. Um segundo botão "Abrir nova Janela" também é criado e associado à função `nova_tela()`.

8. Os widgets são posicionados na janela principal usando o método `pack()`. O método `place()` também é usado para posicionar o botão "Abrir nova Janela" em coordenadas específicas.

9. Por fim, o loop principal `janela.mainloop()` é iniciado para exibir a janela e aguardar as interações do usuário.

## Execução

Para executar o código, siga estas etapas:

1. Certifique-se de ter cumprido todos os requisitos mencionados anteriormente.

2. Crie um novo arquivo Python e copie o código fornecido para o arquivo.

3. Salve o arquivo com um nome adequado, como "login.py".

4. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo Python foi salvo.

5. Execute o arquivo Python digitando o seguinte comando:

   ```
   python login.py
   ```

6. Após a execução do código, a janela de login será exibida com os campos de entrada, botões e funcionalidades associadas.

## Conclusão

A documentação acima fornece informações sobre como utilizar o código Python para criar uma interface de login personalizada usando a biblioteca `customtkinter`. Certifique-se de seguir os requisitos e as etapas de execução mencionadas para obter os resultados desejados.
