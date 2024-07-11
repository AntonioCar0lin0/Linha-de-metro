import tkinter as tk
from tkinter.ttk import Combobox
import matplotlib.pyplot as plt
import networkx as nx
from data_loader import data_nodes
from dijkstra_algorithm import organize_path, organize_itinerary

# Função para visualizar o grafo


def visualize_graph(dataset, itinerary):
    G = nx.Graph()

    for node, neighbors in dataset.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=400, font_size=5, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    path_edges = list(zip(itinerary, itinerary[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges,
                           edge_color='r', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=itinerary,
                           node_color='r', node_size=500)

    plt.title('Visualização das linhas de metrô', size=15, color='darkblue')
    plt.gcf().canvas.manager.set_window_title("Visualização das linhas de metrô")
    plt.show()

# Função para quando o botão for pressionado


def on_button_click():
    starting_node = combo.get()  # Resgata o valor do destino inicial
    final_node = combo1.get()  # Resgata o valor do destino final
    organized_dict = organize_path(starting_node, data_nodes)
    itinerary = organize_itinerary(organized_dict, starting_node, final_node)
    visualize_graph(data_nodes, itinerary)


# Cria a janela
janela = tk.Tk()
janela.title("Visualização das linhas de metrô")

# Mensagem principal, com background preto
mensagem = tk.Label(janela, text='Sistema de visualização das linhas de metrô',
                    fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')

# Selecionar o ponto de partida
mensagem1 = tk.Label(janela, text='Selecione o local de partida:')
mensagem1.grid(row=2, column=0)
combo = Combobox(janela)
combo['values'] = list(data_nodes.keys())
combo.current(0)  # Define o item selecionado
combo.grid(row=2, column=1, columnspan=2)

# Selecionar o destino
mensagem2 = tk.Label(janela, text='Selecione o destino desejado:')
mensagem2.grid(row=5, column=0)
combo1 = Combobox(janela)
combo1['values'] = list(data_nodes.keys())
combo1.current(0)  # Define o item selecionado
combo1.grid(row=5, column=1)

# Criar o botão para pressionar OK
botao = tk.Button(janela, text='OK', command=on_button_click)
botao.grid(row=6, column=1)


janela.mainloop()
