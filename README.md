# 🏡 **Cálculo de Aluguel de Apartamentos** | Projeto da Faculdade

## 💡 **Descrição**
Este projeto foi desenvolvido como parte do meu curso na faculdade e tem como objetivo calcular o custo do aluguel de apartamentos de dois tipos (Tipo 1 e Tipo 2) com base no número de pessoas hospedadas e na quantidade de dias de estadia. A lógica do projeto é:

- **Entrada de Dados**: O usuário insere o nome, a quantidade de pessoas, o tipo de apartamento e o número de diárias.
- **Validação**: Verificação das entradas para garantir que sejam válidas.
- **Cálculo do Custo Total**: O custo do aluguel é calculado de acordo com a quantidade de pessoas e o tipo de apartamento.
- **Divisão do Valor**: O valor total é dividido entre as pessoas hospedadas, calculando o valor a ser pago por cada uma.

## 🚀 **Tecnologias Utilizadas**
- **Python**: Linguagem de programação utilizada.
- **Biblioteca `os`**: Usada para limpar a tela do terminal e melhorar a interação com o usuário.

## 🔧 **Funcionalidades**
- **Verificação de Entrada de Dados**: Garantia de que o número de pessoas e o tipo de apartamento sejam válidos, com mensagens de erro caso o usuário insira dados incorretos.
- **Cálculo do Aluguel**: Dependendo do tipo do apartamento (1 ou 2) e da quantidade de pessoas, o sistema calcula o custo total e o valor individual.
- **Saída de Resultados**: Exibe um resumo com as informações da reserva e o valor a ser pago por pessoa.

## 💻 **Como Rodar o Projeto**

1. Clone o repositório:
    ```bash
    git clone https://github.com/omarceloz/apt-calculator.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd apt-calculator
    ```

3. Execute o script Python:
    ```bash
    python index.py
    ```

4. Insira as informações solicitadas, como o tipo de apartamento (1 ou 2), número de pessoas e dias de estadia.

## 📈 **Exemplo de Execução**
Ao rodar o programa, o sistema pedirá as seguintes informações:

- Nome do cliente.
- Tipo de apartamento (1 ou 2).
- Quantidade de pessoas (1 a 6).
- Quantidade de diárias.

Exemplo de execução:

```bash
Digite seu nome: João
Digite o tipo de apartamento (1 ou 2): 1
Você gostaria de fazer o orçamento para quantas pessoas? (1 a 6): 4
Digite a quantidade de diárias que você gostaria de alugar: 5

Olá João, Muito obrigado por fazer seu orçamento conosco.
Reserva para: 4 pessoa(s)
Tipo de reserva: TIPO 1 R$ 42
Orçamento para: 5 dia(s)

Valor total da reserva: R$ 210,00
Para cada pessoa: R$ 52,50
