# ================================================================
#  📋 MEUS LEMBRETES
#  Um app pra quem esquece as coisas fácil (TDAH, dificuldade de
#  memória, avós, ou você mesmo no meio da correria da escola).
#  Você escreve o lembrete, ele aparece grandão na lista, e quando
#  fizer é só clicar em "Feito" que ele some. Satisfação garantida!
#
#  Esse é o projeto mais desafiador dos três. Vai com calma!
#  Procura os comentários "👉 TROQUE AQUI" pra saber por onde começar.
# ================================================================

import customtkinter

# Tema do app: "dark" é o modo escuro e "light" é o claro
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Criando a janela, que é a "estante" onde as caixas vão ficar
janela = customtkinter.CTk()
janela.title("Quadro de Memória")
janela.geometry("1000x1000")

# Tamanho da letra dos lembretes
tamanho_letra = 50  # 👉 TROQUE AQUI se quiser começar maior ou menor

# Quantos lembretes cabem na lista. Poucos lembretes = menos bagunça na cabeça!
limite = 50 # 👉 TROQUE AQUI

# Uma lista (tipo uma mochila) que guarda os textos de todos os lembretes.
# A gente precisa dela pra conseguir mudar o tamanho da letra de todos de uma vez.
textos_dos_lembretes = []


# ================================================================
#  FUNÇÕES DOS LEMBRETES
# ================================================================

def atualizar_contador():
    # len() conta quantas coisas tem dentro da lista
    quantidade = len(textos_dos_lembretes)

    if quantidade == 0:
        contador.configure(text="Nenhum lembrete. Aproveita o descanso!")
    elif quantidade == 1:
        contador.configure(text="Você tem 1 lembrete")
    else:
        contador.configure(text="Você tem " + str(quantidade) + " lembretes")


def adicionar():
    texto = entrada.get()

    # Se não escreveu nada, avisa
    if texto == "":
        contador.configure(text="Escreve um lembrete primeiro!")
        return  # "return" aqui faz a função parar na hora

    # Se a lista já tá cheia, avisa também
    if len(textos_dos_lembretes) >= limite:
        contador.configure(text="Lista cheia! Conclui um lembrete antes.")
        return

    # ------------------------------------------------------------
    #  📦 CAIXINHA DO LEMBRETE
    #  Olha que massa: cada lembrete ganha a SUA PRÓPRIA caixinha,
    #  e ela mora DENTRO da caixa da lista (master=frame_lista).
    #  Uma caixa dentro da outra, tipo boneca russa!
    # ------------------------------------------------------------
    caixinha = customtkinter.CTkFrame(master=frame_lista)
    caixinha.pack(padx=10, pady=5, fill="x")

    texto_lembrete = customtkinter.CTkLabel(master=caixinha, text=texto,
                                            font=("Arial", tamanho_letra), wraplength=550)
    texto_lembrete.pack(side="left", padx=15, pady=10)

    # Guarda o texto na mochila (a lista lá de cima)
    textos_dos_lembretes.append(texto_lembrete)

    # ------------------------------------------------------------
    #  Aqui tem uma função DENTRO da função!
    #  Parece estranho, mas é o truque pra cada botão "Feito"
    #  saber exatamente qual caixinha ele tem que apagar.
    # ------------------------------------------------------------
    def concluir():
        textos_dos_lembretes.remove(texto_lembrete)  # Tira da mochila
        caixinha.destroy()  # destroy() apaga a caixinha e tudo que tá dentro dela
        atualizar_contador()

    btn_feito = customtkinter.CTkButton(master=caixinha, text="Feito ✓", width=120, height=50,
                                        font=("Arial", 22), fg_color="#2E7D32",  # 👉 TROQUE AQUI
                                        command=concluir)
    btn_feito.pack(side="right", padx=10, pady=10)

    # Limpa a entrada e atualiza o contador
    entrada.delete(0, "end")
    atualizar_contador()


# ================================================================
#  FUNÇÕES DE ACESSIBILIDADE
#  Quase iguais às dos outros apps, mas aqui tem um "for".
#  O "for" passa por cada lembrete da lista, um por um,
#  e muda a letra de todos. Tipo dar um "aumentar" em cada um.
# ================================================================

def aumentar():
    global tamanho_letra

    if tamanho_letra < 60:
        tamanho_letra = tamanho_letra + 4
        for texto_lembrete in textos_dos_lembretes:
            texto_lembrete.configure(font=("Arial", tamanho_letra))
        info_tamanho.configure(text="Letra: " + str(tamanho_letra))


def diminuir():
    global tamanho_letra

    if tamanho_letra > 16:
        tamanho_letra = tamanho_letra - 4
        for texto_lembrete in textos_dos_lembretes:
            texto_lembrete.configure(font=("Arial", tamanho_letra))
        info_tamanho.configure(text="Letra: " + str(tamanho_letra))


def trocar_tema():
    tema_atual = customtkinter.get_appearance_mode()

    if tema_atual == "Dark":
        customtkinter.set_appearance_mode("light")
        btn_tema.configure(text="Modo escuro")
    else:
        customtkinter.set_appearance_mode("dark")
        btn_tema.configure(text="Modo claro")


# ================================================================
#  📦 CAIXA 1: BARRA DE ACESSIBILIDADE (lá no topo)
#  A mesma dos outros dois apps. Você já é especialista nela!
# ================================================================

frame_barra = customtkinter.CTkFrame(master=janela)
frame_barra.pack(padx=10, pady=10, fill="x")

btn_diminuir = customtkinter.CTkButton(master=frame_barra, text="A-", width=60, height=50,
                                       font=("Arial", 22), command=diminuir)
btn_diminuir.pack(side="left", padx=5, pady=10)

btn_aumentar = customtkinter.CTkButton(master=frame_barra, text="A+", width=60, height=50,
                                       font=("Arial", 22), command=aumentar)
btn_aumentar.pack(side="left", padx=5, pady=10)

info_tamanho = customtkinter.CTkLabel(master=frame_barra, text="Letra: 26", font=("Arial", 20))
info_tamanho.pack(side="left", padx=15)

btn_tema = customtkinter.CTkButton(master=frame_barra, text="Modo claro", height=50,
                                   font=("Arial", 20), command=trocar_tema)
btn_tema.pack(side="right", padx=10, pady=10)


# ================================================================
#  📦 CAIXA 2: NOVO LEMBRETE (onde você escreve)
# ================================================================

frame_entrada = customtkinter.CTkFrame(master=janela)
frame_entrada.pack(padx=10, pady=10, fill="x")

entrada = customtkinter.CTkEntry(master=frame_entrada, height=50, font=("Arial", 24),
                                 placeholder_text="Ex.: Tomar remédio às 8h")
entrada.pack(side="left", padx=10, pady=10, fill="x", expand=True)

btn_adicionar = customtkinter.CTkButton(master=frame_entrada, text="Adicionar um lembrete", height=50,
                                        font=("Arial", 22), command=adicionar)
btn_adicionar.pack(side="right", padx=10, pady=10)


# ================================================================
#  📦 CAIXA 3: LISTA DE LEMBRETES
#  Começa vazia! As caixinhas dos lembretes vão nascendo aqui
#  dentro toda vez que você clica em "Adicionar".
#  O fg_color com DUAS cores funciona nos dois temas (lembra do segredo?)
# ================================================================

frame_lista = customtkinter.CTkFrame(master=janela,
                                     fg_color=("gray90", "gray10"))  # 👉 TROQUE AQUI as duas cores
frame_lista.pack(padx=10, pady=10, fill="both", expand=True)


# ================================================================
#  📦 CAIXA 4: RODAPÉ COM O CONTADOR (lá embaixo)
# ================================================================

frame_rodape = customtkinter.CTkFrame(master=janela, fg_color="transparent")
frame_rodape.pack(padx=10, pady=10, fill="x")

contador = customtkinter.CTkLabel(master=frame_rodape, text="Nenhum lembrete. Aproveita o descanso!",
                                  font=("Arial", 22))
contador.pack(pady=5)


# ================================================================
#  💡 IDEIAS PRA VOCÊ TURBINAR O SEU APP
#  1. Muda a mensagem de "lista vazia" pra uma frase motivacional sua
#  2. Coloca uma segunda entrada só pro horário (ex.: "08:00") e junta
#     os dois: texto = horario + " - " + lembrete
#  3. Quer mais lembretes? Aumenta o "limite" lá em cima e troca
#     CTkFrame por CTkScrollableFrame na CAIXA 3 (aí a lista ganha
#     uma barrinha de rolar!)
#  4. Um botão "Importante" que adiciona o lembrete com texto vermelho:
#     text_color="red" no CTkLabel do lembrete
# ================================================================

# Essa linha mantém a janela aberta. Ela sempre fica por último!
janela.mainloop()
