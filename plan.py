import pandas as pd
import json

# Substitua pelo caminho do seu arquivo Excel
file_path = 'planilha.xlsx'

# Leia a planilha
df = pd.read_excel(file_path)
print(df.columns)


# Padronizar os nomes das colunas (removendo espaços, acentos e ajustando caracteres especiais)
df.columns = df.columns.str.strip().str.lower().str.replace('ç', 'c').str.replace('ã', 'a').str.replace(' ', '_')
df.columns = df.columns.str.normalize('NFD').str.encode('ascii', errors='ignore').str.decode('ascii')

# Gerar ID incremental
df['id'] = range(1, len(df) + 1)

# Criar o JSON
json_data = [
    {
        "id": row['id'],
        "name": row['descricao'],  # Nome extraído da coluna 'Descrição'
        "ref": row['referencia'],  # Nome extraído da coluna 'Referência'
        "price": row['preco_ven'],  # Nome extraído da coluna 'Preço ven'
        "image": f"/assets/{row['descricao'].lower().replace(' ', '-').replace(',', '').replace('.', '')}.jpg"
    }
    for _, row in df.iterrows()
]

# Salvar como JSON
output_file = 'output.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print(f"JSON gerado e salvo em {output_file}")
