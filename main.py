from utils import get_data, data_processing, sales_info



game_df = get_data()
# tabela completa dos games mais vendidos


game_df = data_processing(game_df) # trata os nomes das colunas
print(game_df)

sales = sales_info(game_df) # tabela de vendas por loja
sales.plot(kind='bar', figsize=(15, 5)).get_figure().show()
print(sales)


#input('hello') caso o grafico suma rapidamente
