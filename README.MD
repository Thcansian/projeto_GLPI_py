# 🎫 Sistema de Gerenciamento de Chamados (GLPI Simplificado)

## 📌 Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de **Tecnologia Orientada a Objetos (TOO)** do curso de **Bacharelado em Ciência da Computação**.

O sistema simula uma versão simplificada de uma central de atendimento semelhante ao GLPI, permitindo que clientes registrem chamados e que o sistema os encaminhe automaticamente para o setor responsável.

O principal objetivo do projeto é demonstrar a aplicação dos conceitos de **Programação Orientada a Objetos (POO)** e dos padrões de projeto estudados na disciplina.

---

# 🎯 Objetivos do Sistema

O sistema permite:

* Cadastro de clientes;
* Abertura de chamados;
* Direcionamento automático dos chamados;
* Controle de status dos atendimentos;
* Centralização dos chamados em uma única central de atendimento;
* Organização do código utilizando padrões de projeto.

---

# 🏗️ Estrutura do Projeto

```text
Projeto_GLPI_py/
│
├── status_chamado.py
├── setor.py
├── usuario.py
├── cliente.py
├── atendente.py
├── chamado.py
├── chamado_suporte.py
├── chamado_financeiro.py
├── chamado_comercial.py
├── chamado_factory.py
├── sistema_chamados.py
└── main.py
```

---

# 🗺️ Diagrama UML

O diagrama abaixo representa a estrutura geral do sistema, incluindo as relações de herança, associação e os padrões de projeto utilizados.

![Diagrama UML](./projeto_GLPI_py/imagens/UML-diagrama.png)

> Caso a imagem não carregue na visualização do GitHub, ela pode ser acessada diretamente na pasta `imagens` do repositório.

---


# 📚 Classes do Sistema

## Usuario

Classe base responsável por representar qualquer pessoa do sistema.

### Atributos

* nome
* email

### Responsabilidade

Armazenar informações comuns entre clientes e atendentes.

---

## Cliente

Classe derivada de Usuario.

### Responsabilidades

* Armazenar chamados abertos pelo cliente;
* Adicionar novos chamados.

---

## Atendente

Classe derivada de Usuario.

### Responsabilidades

* Representar funcionários da empresa;
* Informar o setor de atuação.

---

## Chamado

Classe base para todos os tipos de chamados.

### Atributos

* titulo
* descricao
* status

### Responsabilidades

* Abrir chamado;
* Iniciar atendimento;
* Finalizar atendimento;
* Servir de base para os demais tipos de chamados.

---

## ChamadoSuporte

Representa chamados relacionados a problemas técnicos.

### Exemplos

* Internet indisponível;
* Problemas em computadores;
* Falhas em sistemas.

---

## ChamadoFinanceiro

Representa chamados relacionados ao setor financeiro.

### Exemplos

* Boletos;
* Cobranças;
* Pagamentos.

---

## ChamadoComercial

Representa chamados relacionados ao setor comercial.

### Exemplos

* Solicitação de orçamento;
* Compra de produtos;
* Informações comerciais.

---

## ChamadoFactory

Classe responsável pela criação automática dos chamados.

Analisa a mensagem enviada pelo cliente e cria o objeto correto.

---

## SistemaChamados

Classe responsável por centralizar todos os chamados cadastrados no sistema.

Implementa o padrão Singleton.

---

# 🧠 Pilares da Programação Orientada a Objetos

## 1. Abstração

A abstração consiste em representar elementos do mundo real através de classes.

### Aplicação no Projeto

As seguintes classes representam entidades reais:

* Usuario
* Cliente
* Atendente
* Chamado

Exemplo:

```python
cliente = Cliente("Thomas", "email@email.com")
```

Nesse caso, a classe Cliente representa um cliente real da empresa.

---

## 2. Encapsulamento

O encapsulamento consiste em proteger os dados internos dos objetos.

### Aplicação no Projeto

Foram utilizados atributos privados:

```python
self.__nome
self.__email
self.__chamados
```

Esses atributos não devem ser acessados diretamente por outras classes.

O acesso ocorre através de métodos e propriedades.

### Benefício

Evita alterações indevidas nos dados do sistema.

---

## 3. Herança

A herança permite que uma classe reutilize características de outra.

### Aplicação no Projeto

```text
Usuario
├── Cliente
└── Atendente
```

Cliente e Atendente herdam os atributos da classe Usuario.

Também foi utilizada herança nos chamados:

```text
Chamado
├── ChamadoSuporte
├── ChamadoFinanceiro
└── ChamadoComercial
```

### Benefício

Evita duplicação de código e facilita manutenção.

---

## 4. Polimorfismo

O polimorfismo permite que objetos diferentes respondam ao mesmo método de formas distintas.

### Aplicação no Projeto

Todas as subclasses de Chamado possuem o método:

```python
resolver()
```

Porém cada uma possui comportamento diferente.

Exemplo:

```python
ChamadoSuporte.resolver()
```

Resultado:

```text
Problema técnico enviado para o suporte.
```

Já:

```python
ChamadoFinanceiro.resolver()
```

Resultado:

```text
Chamado encaminhado para o financeiro.
```

### Benefício

Permite tratar diferentes tipos de chamados de forma uniforme.

---

# 🏭 Padrão de Projeto Factory

## O que é?

O Factory Pattern centraliza a criação de objetos.

Ao invés de criar diretamente:

```python
ChamadoSuporte()
```

ou

```python
ChamadoFinanceiro()
```

o sistema utiliza uma fábrica.

---

## Aplicação no Projeto

Classe:

```python
ChamadoFactory
```

Método:

```python
criar_chamado()
```

Exemplo:

Mensagem recebida:

```text
Minha internet caiu
```

A Factory cria:

```python
ChamadoSuporte
```

Mensagem recebida:

```text
Problema com boleto
```

A Factory cria:

```python
ChamadoFinanceiro
```

### Benefícios

* Centraliza a criação dos objetos;
* Facilita manutenção;
* Facilita expansão do sistema.

---

# 🔒 Padrão de Projeto Singleton

## O que é?

Singleton é um padrão de projeto que garante que exista apenas uma instância de determinada classe durante toda a execução do programa.

---

## Aplicação no Projeto

Classe:

```python
SistemaChamados
```

A central de atendimento deve ser única.

Todos os chamados do sistema ficam armazenados nela.

Exemplo:

```python
sistema1 = SistemaChamados()
sistema2 = SistemaChamados()
```

Mesmo criando duas variáveis, ambas apontam para a mesma instância.

### Benefícios

* Evita duplicação de centrais de atendimento;
* Mantém todos os chamados organizados em um único local;
* Garante consistência dos dados.

---

# 🔄 Fluxo do Sistema

1. Cliente envia uma mensagem.
2. A Factory analisa o texto.
3. O chamado correto é criado.
4. O chamado é registrado na central.
5. O atendimento é iniciado.
6. O método resolver() é executado.
7. O chamado é finalizado.

---

# ▶️ Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/Thcansian/projeto_GLPI_py.git
```

2. Acesse a pasta:

```bash
cd projeto_GLPI_py
```

3. Execute:

```bash
python main.py
```

---

# 🧪 Exemplo de Uso

Entrada:

```text
Minha internet caiu
```

Saída:

```text
Chamado criado!

Título: Problema de Internet
Descrição: Minha internet caiu
Status: ABERTO

Atendimento iniciado.

Problema técnico enviado para o suporte de TI.

Chamado finalizado.
```

---

# 📖 Detalhamento de Aprendizado

## Dificuldades Encontradas

* Compreensão dos padrões de projeto Factory e Singleton;
* Aplicação prática do polimorfismo;
* Organização do sistema utilizando múltiplas classes.

## Como Resolvi

* Revisão do conteúdo apresentado em aula;
* Pesquisa complementar sobre Design Patterns;
* Testes práticos e refatoração do código.

## Principal Aprendizado

O principal aprendizado foi compreender como os pilares da Programação Orientada a Objetos trabalham juntos para construir sistemas organizados, reutilizáveis e de fácil manutenção.

Também foi possível entender a importância dos padrões de projeto para resolver problemas recorrentes de arquitetura de software.

---

# 🤖 Declaração de Uso de IA

Utilizei IA como ferramenta de apoio.

### Ferramentas

* ChatGPT

### Finalidade

* Esclarecimento de conceitos;
* Revisão de código;
* Apoio na documentação;
* Sugestões de arquitetura.

### Validação

Declaro que todo o código gerado foi lido, testado e ajustado conforme as necessidades específicas do projeto e da disciplina.

A responsabilidade pelas decisões de projeto, implementação, testes e correções é inteiramente minha.

---

# 👨‍💻 Autor

Thomas Cansian

Curso: Bacharelado em Ciência da Computação

Disciplina: Tecnologia Orientada a Objetos (TOO)
