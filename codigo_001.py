import pandas as pd

# Criando um DataFrame com dados fictícios de alunos e notas
data = {
    'Nome': ['Alice', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [15, 16, 14, 17, 16],
    'Nota 1': [8.5, 7.0, 9.0, 6.5, 8.0],
    'Nota 2': [7.5, 8.0, 9.5, 7.0, 7.5]
}

df = pd.DataFrame(data)

# Adicionando uma nova coluna com a média das notas
df['Média'] = df[['Nota 1', 'Nota 2']].mean(axis=1)

# Filtrando alunos com média maior ou igual a 8
aprovados = df[df['Média'] >= 8]

# Exibindo os dados
print("Tabela completa:")
print(df)

print("\nAlunos aprovados:")
print(aprovados)


