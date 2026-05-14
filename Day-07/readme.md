# 🪓 Day 7: Jogo da Forca (Hangman)

O sétimo dia foi dedicado à lógica de loops complexos e controle de fluxo, utilizando o jogo da Forca como projeto principal. O objetivo foi transformar um processo de decisão visual (fluxograma) em um programa funcional.

## 🗺️ Planejamento Lógico
Antes da codificação, a estrutura do jogo foi mapeada através de um fluxograma para garantir que todos os cenários (vitória, derrota, acerto e erro) fossem cobertos:

## 🧠 Conceitos Aplicados
* **Gerenciamento de Estados**: Uso da variável `game_over` para controlar a continuidade do loop `while`.
* **Manipulação de Listas e Strings**: Criação dinâmica do `display` para mostrar letras adivinhadas e espaços vazios (`_`).
* **Lógica de Vidas**: Implementação de um sistema de pontuação negativa onde o jogador perde uma "vida" a cada erro, progredindo a arte ASCII da forca.
* **Tratamento de Repetição**: Armazenamento de letras corretas em uma lista (`correct_letters`) para persistir o progresso do usuário a cada rodada.

## 🛠️ Detalhes da Implementação
O código foi estruturado de forma independente no VS Code, utilizando:
* **Arte ASCII**: Inclusão direta dos `stages` da forca e do `logo` dentro do script para garantir a execução autônoma.
* **Aritmética de Índices**: A variável `lives` serve como o índice para a lista `stages`, permitindo que a arte mude conforme a vida diminui.

## 🚀 Como Jogar
1. O programa escolhe uma palavra aleatória da lista.
2. O jogador deve digitar uma letra por vez.
3. Se a letra estiver na palavra, ela é revelada na posição correta.
4. Se a letra não estiver, uma parte do corpo do boneco é desenhada.
5. O jogo termina em **Vitória** se todas as letras forem reveladas ou em **Derrota** se as 6 vidas acabarem.

---
*Status: Projeto funcional e documentado com base na lógica de programação estruturada.*
