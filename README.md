
# Previsão de Vendas com Séries Temporais

Esse é um projeto de estudo aplicando conceitos de estatística e econometria, especialmente **Séries Temporais** para o desenvolvimento do *backend* de um sistema de previsão de vendas. 

# Documentação Teórica
Escrevi uma breve documentação das escolhas que tomei para o desenvolvimento, desde escolha do dataset até a tentativa de não uso de certas tranformações nos dados para cumprir estacionalidades.

[Artigo Completo](https://medium.com/@aquilamazzei/previs%C3%A3o-de-vendas-com-s%C3%A9ries-temporais-4aaf07aa06a5)

### Pastas
- `analysis`: Notebook com os testes estatísticos utilizado como estudo de caso
- `backend`: Contém todos os arquivos para a execução do servidor da API
- `datasets`: Datasets original usado no projeto 




## Documentação da API 


```
  GET /train
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `product_name` | `json` | Efetua o treinamento e exportação do melhor modelo para um produto em específico |

```
  GET /trainall
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `-`      | `-` | Efetua o treinamento e exportação do melhor modelo para todos os produtos |


```
  GET /predict
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `{days, product_name}`      | `json` | Retorna o valor esperado para os próximos `days`   |


```
  GET /sales/insert
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `{product_name, quantity}`      | `json` |Insere a venda de um produto  |





## Stack

 - MySQL
 - Python
 - FastAPI
