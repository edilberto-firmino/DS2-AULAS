# Avaliação de Programação Orientada a Objetos — Python

**Aluno(a):** ____________________________________________________

**Turma:** __________________ **Data:** ____/____/________ **Nota:** __________

**Professor(a):** _________________________________________________

**Valor:** 10,0 pontos · **Quantidade:** 20 questões · **Tempo sugerido:** 120 minutos

## Instruções

- Nas questões 1 a 10, assinale apenas uma alternativa. Cada questão vale **0,3 ponto**.
- Nas questões 11 a 16, apresente as respostas e justificativas solicitadas. Cada questão vale **0,5 ponto**.
- Nas questões 17 a 20, escreva código em Python 3, respeitando a indentação. Cada questão vale **1,0 ponto**.
- Responda às questões abertas em folha separada, identificando seus números.
- Considere cada trecho de código independente dos demais. Não é necessário usar `input()` nas implementações.

## Parte I — Questões objetivas (3,0 pontos)

### Questão 1 — Classe e objeto

No comando `carro1 = Carro("Toyota", "Corolla", 2020)`, considerando que `Carro` é uma classe, qual afirmação está correta?

A) `carro1` é uma classe e `Carro` é um atributo.

B) `Carro` é o modelo e `carro1` referencia uma instância desse modelo.

C) `Carro` e `carro1` são métodos do Python.

D) O comando apenas declara uma função, sem criar um objeto.

### Questão 2 — Atributos e métodos

Uma classe `Cachorro` armazena `nome` e `idade` em cada objeto e possui a ação `latir()`. Esses elementos são, respectivamente:

A) Dois métodos e um atributo.

B) Três classes diferentes.

C) Dois objetos e uma classe.

D) Dois atributos e um método.

### Questão 3 — Inicialização

Qual é a função usual de `__init__` em uma classe Python?

A) Inicializar os atributos da instância durante sua construção.

B) Destruir o objeto após a primeira chamada de método.

C) Imprimir automaticamente todos os atributos do objeto.

D) Transformar todos os métodos em variáveis globais.

### Questão 4 — O parâmetro self

Em um método de instância, o que representa o parâmetro chamado convencionalmente de `self`?

A) Uma referência obrigatória à classe pai.

B) Uma variável global compartilhada por todos os programas.

C) A instância sobre a qual o método está sendo executado.

D) O valor retornado pelo último método chamado.

### Questão 5 — Encapsulamento

Uma classe `Conta` oferece os métodos `depositar()` e `sacar()`, que validam valores antes de atualizar o saldo. Qual princípio é evidenciado pelo controle das alterações do saldo?

A) Herança, porque toda conta precisa herdar de outra conta.

B) Encapsulamento, porque o objeto concentra regras para controlar seu estado.

C) Polimorfismo, porque todos os métodos têm nomes diferentes.

D) Abstração, porque nenhum atributo pode existir na classe.

### Questão 6 — Herança

Observe:

```python
class SerVivo:
    def respirar(self):
        return "Respirando"

class Pessoa(SerVivo):
    pass
```

Qual afirmação está correta?

A) `SerVivo` herda automaticamente todos os métodos de `Pessoa`.

B) `Pessoa` não pode ser instanciada por não declarar `__init__`.

C) É obrigatório copiar `respirar()` para dentro de `Pessoa`.

D) Uma instância de `Pessoa` pode chamar `respirar()` por herança.

### Questão 7 — Polimorfismo

As classes `Passaro`, `Gato` e `Cachorro` implementam `falar()` com sons diferentes. Uma função recebe qualquer um desses objetos e chama `animal.falar()`. O que caracteriza o polimorfismo nesse exemplo?

A) A mesma chamada de método produz comportamentos de acordo com o objeto recebido.

B) Todos os objetos precisam produzir exatamente o mesmo som.

C) As três classes precisam ter os mesmos atributos e valores.

D) A função deve converter cada objeto em uma string antes de chamar o método.

### Questão 8 — Abstração

Um sistema escolar precisa registrar nome, matrícula e notas, além de calcular a média de cada aluno. Qual decisão melhor representa a abstração nesse contexto?

A) Registrar todos os detalhes da vida do aluno, mesmo os que o sistema não utiliza.

B) Impedir que a classe possua métodos.

C) Modelar os dados e comportamentos relevantes para a finalidade do sistema.

D) Substituir todos os objetos por variáveis globais.

### Questão 9 — Estado de cada instância

Qual é a saída do código?

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Ana", 20)
p2 = Pessoa("Carlos", 30)
p1.idade += 1
print(p1.idade, p2.idade)
```

A) `20 30`

B) `21 31`

C) `30 21`

D) `21 30`

### Questão 10 — Retorno de um método

Qual é a saída do código?

```python
class Pessoa:
    def falar(self, mensagem="Olá"):
        return mensagem

p = Pessoa()
p.falar("Bom dia")
print(p.falar())
```

A) Apenas `Bom dia`.

B) Apenas `Olá`.

C) `Bom dia` e depois `Olá`.

D) `None`.

## Parte II — Análise e explicação (3,0 pontos)

### Questão 11 — Leitura de uma classe

Observe:

```python
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        return f"{self.nome} está latindo!"

dog1 = Cachorro("Rex", 3)
```

Identifique o nome da classe, a variável que referencia o objeto, os dois atributos de instância e o método que representa uma ação do cachorro. Explique também o papel de `__init__` nesse exemplo.

### Questão 12 — Alteração de estado

Escreva as **duas linhas de saída** e explique por que a velocidade não termina negativa.

```python
class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, aumento):
        self.velocidade += aumento

    def frear(self, reducao):
        self.velocidade -= reducao
        if self.velocidade < 0:
            self.velocidade = 0

carro = Carro()
carro.acelerar(50)
carro.frear(20)
print(carro.velocidade)
carro.frear(40)
print(carro.velocidade)
```

### Questão 13 — Correção de código

A intenção é guardar o nome recebido e exibir `Maria`. Reescreva a classe corrigindo **os dois problemas** e explique cada correção.

```python
class Aluno:
    def __init__(self, nome):
        nome = nome

    def apresentar():
        return self.nome

aluno = Aluno("Maria")
print(aluno.apresentar())
```

### Questão 14 — Herança e especialização

Escreva as duas linhas de saída e explique de onde vem cada método chamado.

```python
class SerVivo:
    def __init__(self, nome):
        self.nome = nome

    def respirar(self):
        return f"{self.nome} está respirando."

class Pessoa(SerVivo):
    def falar(self):
        return f"{self.nome} está falando."

pessoa = Pessoa("Ana")
print(pessoa.respirar())
print(pessoa.falar())
```

### Questão 15 — Polimorfismo sem herança explícita

Escreva as três linhas de saída. Explique por que a função `som_animal()` pode trabalhar com as três classes, embora nenhuma delas declare herança de uma classe base comum criada pelo programador.

```python
class Passaro:
    def falar(self):
        return "Piu"

class Gato:
    def falar(self):
        return "Miau"

class Cachorro:
    def falar(self):
        return "Au Au"

def som_animal(animal):
    print(animal.falar())

for animal in [Passaro(), Gato(), Cachorro()]:
    som_animal(animal)
```

### Questão 16 — Diferenciando dois pilares

Uma biblioteca precisa de uma classe `Livro` com título, autor, situação de empréstimo e métodos `emprestar()` e `devolver()`. A cor dos olhos do autor não é relevante para esse sistema. O método `emprestar()` deve impedir um novo empréstimo quando o livro já estiver emprestado.

Explique como a **abstração** aparece na escolha das informações modeladas e como o **encapsulamento** aparece no controle do empréstimo. Relacione cada conceito a uma decisão concreta desse cenário.

## Parte III — Implementação em Python (4,0 pontos)

### Questão 17 — Cadastro de um pet

Implemente a classe `Pet` com os atributos de instância `nome`, `tipo` e `idade`, inicializados por `__init__`. Crie o método `apresentar()`, que **retorna** uma frase com os três dados. Instancie um pet chamado `Thor`, do tipo `cachorro`, com `3` anos, e imprima o resultado de `apresentar()`.

Saída esperada:

```text
Thor é um cachorro de 3 anos.
```

### Questão 18 — Controle de saldo

Implemente a classe `Conta` com saldo inicial zero e os métodos:

- `depositar(valor)`: aceita somente valor maior que zero; retorna `True` quando realiza o depósito e `False` quando rejeita.
- `sacar(valor)`: aceita somente valor maior que zero e menor ou igual ao saldo; retorna `True` quando realiza o saque e `False` quando rejeita.
- `consultar_saldo()`: retorna o saldo atual.

Use `_saldo` para sinalizar, por convenção, um atributo de uso interno. Operações rejeitadas devem manter o saldo anterior. Considere entradas numéricas válidas; não é necessário tratar strings ou outros tipos. No uso externo, consulte e altere o saldo pelos métodos.

Após criar a conta, demonstre um depósito de `100`, uma tentativa de saque de `150` e um saque de `40`, imprimindo o retorno de cada operação e, por último, o saldo final. Em uma frase, explique se o prefixo `_` impede tecnicamente o acesso direto ao atributo.

### Questão 19 — Reutilização por herança

Crie a classe `Pessoa` com `nome` e `idade`, inicializados em `__init__`, e o método `apresentar()`, que retorna `Meu nome é Ana e tenho 17 anos.` para esses dados.

Crie a classe `Aluno`, que herda de `Pessoa` e acrescenta o método `estudar(materia)`, retornando `Ana está estudando Python.` para esses argumentos. Reutilize o inicializador e o método `apresentar()` da classe base, sem copiá-los para `Aluno`. Crie `Aluno("Ana", 17)` e imprima o resultado dos dois métodos.

### Questão 20 — Aplicando polimorfismo

Crie as classes `Cachorro` e `Gato`, cada uma com um método `falar()` que retorna, respectivamente, `Au Au` e `Miau`.

Implemente a função `apresentar_sons(animais)`, que recebe uma lista, percorre seus objetos e imprime o retorno de `falar()` de cada um, sem usar `if`, `type()` ou `isinstance()` para escolher o som. Demonstre a função com uma lista contendo um cachorro e um gato, nessa ordem. Explique, em uma frase, onde ocorre o polimorfismo.
