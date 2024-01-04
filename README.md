# Calculadora com Flask

Este é um projeto simples que demonstra o uso do Flask como backend para uma calculadora web, e Js para a interatividade na página da calculadora.

## **Pré-requisitos**

Certifique-se de ter o Python instalado. Este projeto utiliza o Flask para o backend para interatividade na página web.

## **Instalação**

1. Clone este repositório:
    
    ```bash
    bashCopy code
    git clone https://github.com/seu_usuario/seu_projeto.git
    
    ```
    
2. Navegue até o diretório do projeto:
    
    ```bash
    bashCopy code
    cd seu_projeto
    
    ```
    
3. Crie um ambiente virtual (opcional, mas recomendado):
    
    ```bash
    bashCopy code
    python -m venv venv
    
    ```
    
4. Ative o ambiente virtual (no Windows):
    
    ```bash
    bashCopy code
    venv\Scripts\activate
    
    ```
    
5. Instale as dependências:
    
    ```bash
    bashCopy code
    pip install -r requirements.txt
    
    ```
    

## **Executando o projeto**

1. Execute o arquivo **`run.py`** para iniciar o servidor Flask:
    
    ```bash
    bashCopy code
    python run.py
    
    ```
    
2. Abra o navegador e acesse **`http://127.0.0.1:5000/calculadora`** para usar a calculadora.

## **Funcionalidades**

- Calculadora simples com operações de adição, subtração, multiplicação e divisão.
- Interação em tempo real utilizando Vue.js para realizar os cálculos na página sem recarregar.

## **Estrutura do Projeto**

```python

meu_projeto/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── calculadora.html
│   │   └── index.html
│   └── assets/
│       └── style.css
│
└── run.py

```

## **Contribuição**

Contribuições são bem-vindas! Se você encontrar algum problema ou quiser adicionar novos recursos, sinta-se à vontade para abrir uma issue ou enviar um pull request.
