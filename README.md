Ecommerce Estatística Dashboard
Este projeto cria uma aplicação interativa de visualização de dados de um dataset de ecommerce, utilizando Dash, Plotly e Seaborn. A aplicação exibe gráficos interativos para explorar métricas de vendas, como notas de produtos, descontos aplicados, quantidade de produtos vendidos e muito mais.

Tecnologias Utilizadas
Python 3.x
Dash - Framework para construção de aplicações web interativas.
Plotly - Biblioteca para criação de gráficos interativos.
Seaborn - Biblioteca para visualização de dados estatísticos.
Pandas - Biblioteca para manipulação de dados.
Matplotlib - Biblioteca para criação de gráficos estáticos.
Funcionalidades
A aplicação inclui os seguintes gráficos interativos:

Histograma: Mostra a distribuição das notas dos produtos.
Gráfico de Dispersão: Relação entre o desconto e a quantidade de produtos vendidos.
Gráfico de Barras: Comparação da quantidade de produtos vendidos por marca.
Gráfico de Densidade: Visualiza a distribuição dos descontos aplicados.
Gráfico de Pizza: Mostra a distribuição das vendas por gênero.
Gráfico de Regressão: Exibe a relação entre o desconto e a quantidade de vendas.
Mapa de Calor: Exibe a correlação entre algumas variáveis importantes.
Pré-requisitos
Antes de executar a aplicação, você precisa instalar as bibliotecas necessárias. Você pode fazer isso utilizando o pip:

bash
Copiar
Editar
pip install pandas dash plotly seaborn matplotlib
Como Usar
Clone este repositório para sua máquina local:

bash
Copiar
Editar
git clone https://github.com/seu_usuario/ecommerce_dashboard.git
Navegue até o diretório do projeto:

bash
Copiar
Editar
cd ecommerce_dashboard
Garanta que o arquivo ecommerce_estatistica.csv esteja no mesmo diretório ou forneça o caminho correto para o arquivo CSV.

Execute o arquivo Python:

bash
Copiar
Editar
python app.py
Acesse a aplicação no seu navegador:

cpp
Copiar
Editar
http://127.0.0.1:8050/
Estrutura do Projeto
bash
Copiar
Editar
ecommerce_dashboard/
│
├── app.py                  # Arquivo principal da aplicação Dash
├── ecommerce_estatistica.csv # Dataset utilizado para gerar os gráficos
├── README.md               # Este arquivo

Observações

Certifique-se de que o arquivo ecommerce_estatistica.csv tenha o formato correto e que as colunas mencionadas no código existam. Caso contrário, será necessário ajustar o código de acordo com o seu dataset.
A aplicação pode ser estendida com mais gráficos interativos ou análise de dados.

Contribuições
Se você quiser contribuir com melhorias ou novas funcionalidades, sinta-se à vontade para fazer um fork deste repositório e enviar um pull request.
