# 🧠 Sistema Inteligente de Mapeamento de Processos

## 📌 Descrição

Este projeto tem como objetivo desenvolver um sistema capaz de capturar, registrar e analisar eventos de interação do usuário, com o propósito de reconstruir automaticamente fluxos de processos e gerar descrições textuais estruturadas.

A proposta busca reduzir a dependência de modelagem manual de processos, automatizando a identificação de padrões e a documentação de atividades realizadas em sistemas computacionais.

---

## 🎯 Objetivo

Desenvolver um protótipo funcional que permita:

* Capturar eventos de interação do usuário (em ambiente controlado)
* Armazenar dados de forma estruturada
* Reconstruir automaticamente o fluxo de processos
* Gerar descrições textuais dos processos executados

---

## ⚙️ Funcionamento

O sistema opera em três etapas principais:

### 1. Captura de eventos

Eventos de interação do usuário são registrados contendo informações como:

* Usuário
* Contexto do processo
* Ação executada
* Data e hora
* Tela ou módulo
* Sequência de execução

### 2. Processamento

Os eventos são organizados e analisados para:

* Ordenar cronologicamente as ações
* Identificar o fluxo do processo
* Estruturar a sequência lógica das atividades

### 3. Geração de saída

A partir do fluxo reconstruído, o sistema gera:

* Lista de etapas do processo
* Descrição textual automática em linguagem natural

---

## 🧱 Estrutura do Projeto

```
mapeamento-processos-ia/
│
├── main.py
├── models/
│   └── evento.py
├── services/
│   ├── capturador.py
│   ├── processador.py
│   └── gerador_documentacao.py
├── data/
│   └── eventos.json
└── utils/
```

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* JSON (armazenamento de dados)
* Git/GitHub

---

## 🚀 Execução do Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/mapeamento-processos-ia.git
```

2. Acesse a pasta:

```bash
cd mapeamento-processos-ia
```

3. Execute o projeto:

```bash
python main.py
```

---

## 📊 Exemplo de Saída

```text
Fluxo reconstruído:
['Acessar sistema', 'Realizar login', 'Preencher formulário', 'Salvar dados']

Descrição:
O usuário realizou as seguintes etapas do processo: Acessar sistema, depois Realizar login, depois Preencher formulário e, por fim, Salvar dados.
```

---

## 🔬 Características Acadêmicas

Este projeto está sendo desenvolvido como parte de uma disciplina de projeto, servindo como base para evolução futura em um Trabalho de Conclusão de Curso (TCC).

A solução atual utiliza eventos simulados em ambiente controlado para validação da arquitetura e dos mecanismos de processamento.

---

## 🔮 Trabalhos Futuros

O sistema poderá ser evoluído para incluir:

* Captura automática de eventos reais (mouse e teclado)
* Identificação de padrões com técnicas de IA
* Geração automática de fluxogramas
* Exportação de documentação no formato POP
* Integração com ferramentas de Process Mining

---

## 👩‍💻 Autores

* Sara Thais dos Santos Graciano
* Gabriel Henrique de Medeiros Penha

---

## 📄 Licença

Projeto acadêmico desenvolvido para fins educacionais.
