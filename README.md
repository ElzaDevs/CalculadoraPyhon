# 🧮 Calculadora CLI.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Licença](https://img.shields.io/badge/licença-MIT-blue)

Uma calculadora simples que roda direto no terminal. Foi meu projeto guiado para treinar lógica de programação em Python — nada revolucionário, mas todo mundo precisa começar por algum lugar, certo?

---

## 📑 Índice.

- [O que ela faz](#-o-que-ela-faz)
- [Por que fiz esse projeto](#-por-que-fiz-esse-projeto)
- [Como rodar](#-como-rodar)
- [Exemplo de uso](#-exemplo-de-uso)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Sobre mim](#-sobre-mim)
- [Licença](#-licença)

---

## 🧩 O que ela faz???

Você escolhe uma operação, digita dois números, e ela te dá o resultado. Depois volta pro menu automaticamente, então dá pra fazer quantas contas quiser sem precisar reiniciar o programa toda hora.

| Opção | Operação      |
|:-----:|---------------|
| `1`   | Soma          |
| `2`   | Subtração     |
| `3`   | Multiplicação |
| `4`   | Divisão       |
| `s`   | Sair          |

> ⚠️ A divisão vem com proteção contra divisão por zero — sem isso o programa quebra na primeira tentativa.

---

## 💡 Por que fiz esse projeto??

Queria praticar o básico do básico de um jeito que realmente fixasse:

- Laços de repetição
- Estruturas condicionais
- Entrada e saída de dados
- Operações matemáticas
- Coleções de dados (organizando as opções do menu)

É o tipo de projeto pequeno que ajuda a entender como essas peças se encaixam antes de partir pra coisas mais complexas.

---

## 🚀 Como rodar

**Pré-requisito:** Python 3 instalado ([baixar aqui](https://www.python.org/downloads/))

```bash
git clone https://github.com/ElzaDevs/calculadora-cli.git
cd calculadora-cli
python calculadora.py
```

E pronto, o menu já aparece no terminal.

---

## 💻 Exemplo de uso:

**Fazendo uma soma:**

```
===== CALCULADORA =====
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
s - Sair
========================
Escolha uma opção: 1

Digite o primeiro número: 10
Digite o segundo número: 5

Resultado: 10 + 5 = 15
```

**Tentando dividir por zero:**

```
Escolha uma opção: 4

Digite o primeiro número: 8
Digite o segundo número: 0

Erro: não é possível dividir por zero!
```

**Saindo do programa:**

```
Escolha uma opção: s

Obrigado por usar a calculadora! Até a próxima.
```

---

## 📂 Estrutura do projeto.

```
calculadora-cli/
├── calculadora.py
└── README.md
```

Nada complicado — um arquivo só, focado em fazer bem uma coisa simples.

---

## 👩‍💻 Sobre mim.

Sou a Elza, estudante de Engenharia de Software, treinando os fundamentos de Python e Java enquanto construo meu caminho no desenvolvimento de software.

[![GitHub](https://img.shields.io/badge/GitHub-ElzaDevs-181717?style=flat&logo=github)](https://github.com/ElzaDevs)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Elza_Aquino-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/elzaaquino)

---

## 📄 Licença

Este projeto está sob a licença MIT — usa, estuda, adapta à vontade.
