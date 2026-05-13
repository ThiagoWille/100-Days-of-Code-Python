# 🔐 Day 8: Funções com Parâmetros e a Cifra de César

O foco de hoje foi aprofundar o uso de funções, movendo de execuções simples para blocos de código dinâmicos que aceitam múltiplos inputs, culminando no projeto da Cifra de César.

## 🧠 Conceitos Aprendidos

* **Parâmetros vs. Argumentos**: Entendimento de que parâmetros são os nomes definidos na função e argumentos são os valores reais passados na chamada.
* **Argumentos Posicionais**: A importância da ordem em que os dados são inseridos.
* **Keyword Arguments**: Técnica para vincular argumentos diretamente aos parâmetros (`parametro="valor"`), evitando erros de posicionamento.
* **Lógica de Criptografia**: Manipulação de strings e listas usando aritmética de módulo (`%`) para criar deslocamentos infinitos no alfabeto.

## 📈 Evolução e Refatoração do Projeto

O projeto da Cifra de César foi desenvolvido em um ciclo de melhoria contínua:

1.  **v1.0 (Versão Original)**: Implementação de duas funções distintas (`encrypt` e `decrypt`). Embora mais longo, este código demonstrou domínio total do fluxo lógico e tratamento de caracteres especiais.
2.  **v2.0 (Refatoração)**: Consolidação da lógica em uma única função controladora (`caesar`). Utilizei a lógica de multiplicadores de direção para aplicar o princípio **DRY (Don't Repeat Yourself)**, tornando o código mais limpo e eficiente.

## 🛠️ Tecnologias e Ferramentas
* Python 3
* VS Code (Ambiente de Desenvolvimento)
* Git para Versionamento

---
*Status: Dia 8 concluído. Código funcional, robusto e refatorado.*
