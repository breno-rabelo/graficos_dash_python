import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('ecommerce_estatistica.csv')

def graficos(df):
    # Histograma
    figure1 = px.histogram(df['Nota'])
    figure1.update_layout(
        title='Histograma das Notas',
        xaxis_title='Notas',
        yaxis_title='Frequencia'
    )

    # Dispersao
    figure2 = px.scatter(df['Desconto'], df['Qtd_Vendidos_Cod'])
    figure2.update_layout(
        title='Relacao da quantidade de descontos com a quantidade vendida',
        xaxis_title='Desconto',
        yaxis_title='Quantidade de vendas'
    )

    # Barras
    figure3 = px.bar(df, x='Marca', y='Qtd_Vendidos_Cod', color='Marca', barmode='group',
                     color_discrete_sequence=px.colors.qualitative.Set1)

    # Densidade
    figure4 = sns.kdeplot(df['Desconto_MinMax'], fill=True, color='Blue')
    plt.title('Quantidade de descontos')

    # Pizza
    figure5 = px.pie(df, names='Genero', title='Quantidade de vendas por genero', hole=0.3,
                     color_discrete_sequence=px.colors.qualitative.Set1)
    figure5.update_layout(
        title='Quantidade de vendas por genero',
    )

    # Regressao
    figure6 = sns.regplot(x='Desconto', y='Qtd_Vendidos_Cod', data=df, color='#278f65',
                          scatter_kws={'alpha': 0.5, 'color': '#34c289'})
    figure6.set(xlabel='Desconto', ylabel='Quantidade de vendas')

    # Mapa Calor
    corr = df[['Temporada_Cod', 'Marca_Cod', 'N_Avaliacoes_MinMax', 'Qtd_Vendidos_Cod']].corr()
    figure7 = px.imshow(corr, x=corr.columns, y=corr.columns, title='Mapa de calor')

    return figure1, figure2, figure3, figure4, figure5, figure6, figure7

# Criar um app Dash
def cria_app(df):
    app = Dash(__name__)

    figure1, figure2, figure3, figure4, figure5, figure6, figure7 = graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=figure1),
        dcc.Graph(figure=figure2),
        dcc.Graph(figure=figure3),
        dcc.Graph(figure=figure4),
        dcc.Graph(figure=figure5),
        dcc.Graph(figure=figure6),
        dcc.Graph(figure=figure7)
    ])
    return app

if __name__ == '__main__':
    app = cria_app(df)
    app.run_server(debug=True, port=8050)