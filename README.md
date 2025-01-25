# Automação: Conversão de Excel para JSON

Este script automatiza a conversão de uma planilha Excel para um arquivo JSON, formatando os dados e gerando identificadores incrementais automaticamente.

---

## ⚙️ Tecnologias Utilizadas

- **Python**  
- **Pandas** (para manipulação de dados)  
- **JSON** (para exportação de dados)  

---

## 🚀 Como executar o script?

### 1. Instale as dependências
Certifique-se de que o Python está instalado e instale as bibliotecas necessárias com:

```bash
pip install pandas openpyxl
```

### 2. Configure o arquivo de entrada
Substitua o caminho do arquivo Excel na variável `file_path` dentro do script:

```python
file_path = 'planilha.xlsx'
```

### 3. Execute o script
Para rodar a conversão, execute o seguinte comando:

```bash
python converter.py
```

O arquivo JSON será gerado no diretório atual com o nome `output.json`.

---

## 📊 Explicação do Código

1. **Leitura da planilha Excel:**  
   O script lê os dados da planilha especificada usando `pandas`.

2. **Padronização dos nomes das colunas:**  
   - Remove espaços e caracteres especiais.
   - Converte letras maiúsculas para minúsculas.
   - Substitui caracteres como `ç` por `c` e `ã` por `a`.

3. **Geração de IDs incrementais:**  
   - A coluna `id` é criada automaticamente para cada linha.

4. **Formatação dos dados para JSON:**  
   - Campos extraídos da planilha: `descricao`, `referencia` e `preco_ven`.
   - Geração automática de caminhos de imagens.

5. **Exportação para JSON:**  
   - O arquivo JSON é salvo com indentação para melhor legibilidade.

---

## 📅 Exemplo de saída JSON

```json
[
  {
    "id": 1,
    "name": "Produto A",
    "ref": "12345",
    "price": 99.90,
    "image": "/assets/produto-a.jpg"
  },
  {
    "id": 2,
    "name": "Produto B",
    "ref": "67890",
    "price": 149.50,
    "image": "/assets/produto-b.jpg"
  }
]
```

---

## 💪 Contribuição

Sinta-se à vontade para contribuir com o projeto! Para isso:

1. Faça um fork do repositório
2. Crie uma branch: `git checkout -b feature/minha-feature`
3. Commit suas mudanças: `git commit -m 'Adicionando nova feature'`
4. Faça um push para a branch: `git push origin feature/minha-feature`
5. Abra um Pull Request

---
