import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados tratados do Rio de Janeiro
df = pd.read_csv("dados.csv")

# Delitos de interesse
delito_interesse = [
    'Homicídio Doloso',
    'Letalidade Violenta',
    'Morte por Intervencao do Agente do Estado'
]

# Filtrar para os principais delitos
df = df[df['delito'].isin(delito_interesse)]

# Agrupar por ano e tipo de delito e somar as contagens
df_grouped = df.groupby(['ano', 'delito'])['populacao'].sum().reset_index()

# Pivotar os dados para o gráfico
df_pivot = df_grouped.pivot(index='ano', columns='delito', values='populacao')

# Plotar gráfico de linhas
plt.figure(figsize=(14, 7))
for delito in df_pivot.columns:
    plt.plot(df_pivot.index, df_pivot[delito], marker='o', label=delito)

plt.title("Evolução dos principais delitos no Estado do Rio de Janeiro")
plt.xlabel("Ano")
plt.ylabel("Número de Ocorrências")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()
