from pandas import DataFrame, read_html
from selenium.webdriver import Chrome



link = 'https://pt.wikipedia.org/wiki/Lista_de_jogos_eletr%C3%B4nicos_mais_vendidos'


def get_data():
    """
    Retrieves data from link using a Chrome browser instance.

    Returns:
        DataFrame: A pandas DataFrame containing the data extracted from the wikipedia.
    """
    drive = Chrome()
    drive.get(link)
    df = read_html(link)[1]

    return df

# tratou os dados
def data_processing(df: DataFrame):
    # Renomear coluna 'Desenvolvedora(s)[n 1]' para 'Desenvolvedora(s)'
    df = df.rename(columns={'Desenvolvedora(s)[n 1]': 'Desenvolvedora(s)'})

    df['Desenvolvedora(s)'] = df['Desenvolvedora(s)'].str.split(' / ')
    df = df.explode('Desenvolvedora(s)')
    
    # Remover pontos das vendas e converter para int
    df['Vendas'] = df['Vendas'].str.replace('.', '').astype('Int64')    
    # Remover colunas indesejadas
    df = df.drop(['Lançamento inicial', 'Publicadora(s)[n 1]', 'Ref.'], axis=1)

    return df

def sales_info(df: DataFrame):
    # agrupando por loja
    df = df.groupby('Desenvolvedora(s)').sum()
    df = df[['Vendas']]
    df = df.sort_values('Vendas', ascending=False)
    return df[:10]
  
