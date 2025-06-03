from tkinter import tk

def criar_tela(titulo):
    """
    Cria uma janela com o título 

    Args:
        titulo (str): Título da janela.
        largura (int): Largura da janela.
        altura (int): Altura da janela.
    
    Returns:
        tk.Tk: Instância da janela criada.
    """
    tela = tk.Tk()
    tela.title(titulo, "Veículos")
    tela.style(theme="super hero")
    tela.geometry("600x400", text=Ariel, 20)

    return tela

def exibir_mensagem(tela, mensagem):
    """
    Exibe uma mensagem em uma janela de diálogo.
    
    Args:
        tela (tk.Tk): Instância da janela onde a mensagem será exibida.
        mensagem (str): Mensagem a ser exibida.
    """
    tk.messagebox.showinfo("Informação", mensagem, parent=tela)
def fechar_tela(tela):
    """
    Fecha a janela especificada.
    
    Args:
        tela (tk.Tk): Instância da janela a ser fechada.
    """
    tela.destroy()
def limpar_campos(campos):
    """
    Limpa os campos de entrada especificados.

    Args:
        campos (list): Lista de campos de entrada a serem limpos.
    """
    for campo in campos:
        campo.delete(0, tk.END)

def obter_valor_entrada(campo):
    """
    Obtém o valor de um campo de entrada.

    Args:
        campo (tk.Entry): Campo de entrada do qual o valor será obtido.

    Returns:
        str: Valor do campo de entrada.
    """
    return campo.get().strip()
def definir_valor_entrada(campo, valor):
    """
    Define o valor de um campo de entrada.
    Args:
        campo (tk.Entry): Campo de entrada onde o valor será definido.
        valor (str): Valor a ser definido no campo de entrada.
    """
    campo.delete(0, tk.END)
    campo.insert(0, valor.strip())
def criar_botao(tela, texto, comando):
    """
    Cria um botão na tela com o texto e comando especificados.

    Args:
        tela (tk.Tk): Instância da janela onde o botão será criado.
        texto (str): Texto a ser exibido no botão.
        comando (callable): Função a ser chamada quando o botão for clicado.

    Returns:
        tk.Button: Instância do botão criado.
    """
    botao = tk.Button(tela, text=texto, command=comando)
    botao.pack(pady=10)
    return botao
def criar_label(tela, texto):
    """
    Cria um rótulo na tela com o texto especificado.
    Args:
        tela (tk.Tk): Instância da janela onde o rótulo será criado.
        texto (str): Texto a ser exibido no rótulo.
    Returns:

        tk.Label: Instância do rótulo criado.
    """
    label = tk.Label(tela, text=texto)
    label.pack(pady=5)
    return label
def criar_campo_entrada(tela, texto):
    """
    Cria um campo de entrada na tela com o texto especificado.
    Args:
        tela (tk.Tk): Instância da janela onde o campo de entrada será criado.
        texto (str): Texto a ser exibido como rótulo do campo de entrada.

    Returns:
        tk.Entry: Instância do campo de entrada criado.
    """
    frame = tk.Frame(tela)
    frame.pack(pady=5)

    label = tk.Label(frame, text=texto)
    label.pack(side=tk.LEFT)

    entrada = tk.Entry(frame)
    entrada.pack(side=tk.RIGHT)

    return entrada      
def criar_lista(tela, itens):
    """
    Cria uma lista na tela com os itens especificados.
    Args:
        tela (tk.Tk): Instância da janela onde a lista será criada.
        itens (list): Lista de itens a serem exibidos.
    Returns:

        tk.Listbox: Instância da lista criada.  
    """
    lista = tk.Listbox(tela)
    for item in itens:
        lista.insert(tk.END, item)
    lista.pack(pady=10, fill=tk.BOTH, expand=True)
    return lista
def obter_item_lista(lista):
    """
    Obtém o item selecionado de uma lista.
    Args:
        lista (tk.Listbox): Instância da lista de onde o item será obtido.
    Returns:
        str: Item selecionado da lista, ou None se nenhum item estiver selecionado.
    """
    selecionado = lista.curselection()
    if selecionado:
        return lista.get(selecionado[0])
    return None
def definir_item_lista(lista, itens):
    """
    Define os itens de uma lista.
    Args:
        lista (tk.Listbox): Instância da lista onde os itens serão definidos.
        itens (list): Lista de itens a serem exibidos na lista.
    """
    lista.delete(0, tk.END)
    for item in itens:
        lista.insert(tk.END, item)
    lista.pack(pady=10, fill=tk.BOTH, expand=True)
