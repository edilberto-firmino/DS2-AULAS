# Gabarito comentado — POO em Python

**Uso do professor.** Valor total: **10,0 pontos**. Aceitar soluções equivalentes que atendam aos enunciados. Nas questões abertas, atribuir pontuação parcial conforme os critérios abaixo, sem penalizar duas vezes a mesma falha.

## Questões objetivas — 0,3 ponto cada

| Questão | Resposta | Justificativa |
| --- | --- | --- |
| 1 | B | `Carro` é a classe; `carro1` referencia uma instância. |
| 2 | D | Nome e idade são dados; `latir()` é um comportamento. |
| 3 | A | `__init__` inicializa a instância. Tecnicamente, a criação é responsabilidade de `__new__`; não exigir esse detalhe na prova. |
| 4 | C | `self` referencia a instância que recebe a chamada. É um nome convencional, não uma palavra reservada. |
| 5 | B | Os métodos concentram a validação e a alteração do saldo. |
| 6 | D | `Pessoa` herda `respirar()` de `SerVivo`. |
| 7 | A | A chamada `falar()` utiliza o comportamento do objeto recebido. |
| 8 | C | Abstrair é selecionar características relevantes para o problema. |
| 9 | D | Alterar `p1.idade` não altera o atributo de `p2`. |
| 10 | B | A primeira chamada retorna uma string que não é impressa. A segunda usa o argumento padrão e seu retorno é impresso. |

## Questões de análise — 0,5 ponto cada

### Questão 11

Classe: `Cachorro`. Variável que referencia a instância: `dog1`. Atributos: `self.nome` e `self.idade`. Método de ação: `latir()`. O inicializador armazena `"Rex"` e `3` nos atributos do novo objeto.

**Correção:** classe 0,1; referência ao objeto 0,1; dois atributos 0,1 (0,05 cada); método de ação 0,1; inicialização 0,1.

### Questão 12

```text
30
0
```

A velocidade passa de 0 para 50 e depois para 30. A segunda frenagem produz temporariamente -10, mas o `if` redefine o atributo para zero.

**Correção:** 0,15 por linha correta; 0,2 pela explicação do limite aplicado pelo método.

### Questão 13

```python
class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        return self.nome

aluno = Aluno("Maria")
print(aluno.apresentar())
```

`self.nome = nome` guarda o argumento na instância; `nome = nome` apenas reatribui a variável local. O método de instância precisa receber a referência ao objeto, convencionalmente chamada `self`. No código original, a chamada a `apresentar()` falha antes de acessar o atributo, pois o objeto é passado implicitamente e o método não declara parâmetro para recebê-lo.

**Correção:** 0,15 por correção no código; 0,1 por explicação.

### Questão 14

```text
Ana está respirando.
Ana está falando.
```

`respirar()` é herdado de `SerVivo`; `falar()` é definido em `Pessoa`. Como `Pessoa` não redefine `__init__`, utiliza o inicializador herdado para armazenar o nome.

**Correção:** 0,1 por linha correta; 0,15 pela origem de cada método chamado. A explicação do inicializador é complementar.

### Questão 15

```text
Piu
Miau
Au Au
```

Todos os objetos oferecem um método `falar()` compatível com a chamada usada na função. Python permite utilizá-los por esse comportamento comum, sem exigir uma classe base explícita criada pelo programador. Aceitar a explicação sem exigir o termo técnico *duck typing*.

**Correção:** 0,1 por linha correta; 0,2 pela explicação da chamada comum aos diferentes objetos.

### Questão 16

**Abstração:** selecionar título, autor e situação de empréstimo, pois são relevantes para a biblioteca, deixando de fora a cor dos olhos do autor. **Encapsulamento:** concentrar em `emprestar()` a regra que consulta e altera o estado, rejeitando um empréstimo duplicado. O método deve ser o caminho previsto para essa operação.

**Correção:** 0,25 por conceito corretamente relacionado ao cenário. Não exigir classes abstratas, decoradores ou bloqueio absoluto de acesso aos atributos.

## Questões de implementação — 1,0 ponto cada

### Questão 17

```python
class Pet:
    def __init__(self, nome, tipo, idade):
        self.nome = nome
        self.tipo = tipo
        self.idade = idade

    def apresentar(self):
        return f"{self.nome} é um {self.tipo} de {self.idade} anos."

pet = Pet("Thor", "cachorro", 3)
print(pet.apresentar())
```

**Correção:** classe e inicializador 0,2; três atributos de instância 0,3 (0,1 cada); método com retorno correto 0,3; instanciação e impressão 0,2.

### Questão 18

```python
class Conta:
    def __init__(self):
        self._saldo = 0

    def depositar(self, valor):
        if valor <= 0:
            return False
        self._saldo += valor
        return True

    def sacar(self, valor):
        if valor <= 0 or valor > self._saldo:
            return False
        self._saldo -= valor
        return True

    def consultar_saldo(self):
        return self._saldo

conta = Conta()
print(conta.depositar(100))
print(conta.sacar(150))
print(conta.sacar(40))
print(conta.consultar_saldo())
```

Saída: `True`, `False`, `True` e `60`, em linhas separadas. Aceitar representação numérica equivalente para o saldo.

O prefixo `_` sinaliza uso interno por convenção; não impede tecnicamente o acesso direto. O encapsulamento depende também do uso consistente da interface oferecida pela classe.

**Correção:** saldo inicial e consulta 0,15; depósito com validação e retorno 0,2; saque com validação, preservação do saldo em rejeições e retorno 0,3; demonstração solicitada 0,2; explicação da convenção 0,15.

### Questão 19

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."

class Aluno(Pessoa):
    def estudar(self, materia):
        return f"{self.nome} está estudando {materia}."

aluno = Aluno("Ana", 17)
print(aluno.apresentar())
print(aluno.estudar("Python"))
```

**Correção:** classe base e inicialização 0,25; `apresentar()` 0,2; herança com reutilização sem cópia 0,25; `estudar()` 0,2; instanciação e duas impressões 0,1.

### Questão 20

```python
class Cachorro:
    def falar(self):
        return "Au Au"

class Gato:
    def falar(self):
        return "Miau"

def apresentar_sons(animais):
    for animal in animais:
        print(animal.falar())

apresentar_sons([Cachorro(), Gato()])
```

O polimorfismo ocorre em `animal.falar()`: a chamada utiliza a implementação correspondente a cada objeto. A saída é `Au Au` e depois `Miau`, em linhas separadas.

**Correção:** classes e retornos corretos 0,3 (0,15 cada); função com laço e chamada comum, sem seleção de tipo, 0,3; demonstração com lista na ordem pedida 0,2; explicação 0,2.

## Referências locais e cobertura

Avaliação elaborada a partir do resumo fornecido pelo professor e dos materiais locais. A ementa e o cronograma também preveem interfaces gráficas, exceções e PostgreSQL; esta prova tem recorte nos fundamentos de POO e nos quatro pilares destacados no pedido, com estruturas básicas de Python aplicadas aos objetos.

| Questões | Conteúdo | Materiais de referência |
| --- | --- | --- |
| 1–4, 9, 11, 13, 17 | Classes, objetos, atributos, inicialização e métodos | `aulas/primeira aula poo.pptx`, `aulas/exemplo1_cachorro.py`, `pratica1/carro.py`, `pratica3/3pet.py` |
| 5, 16, 18 | Encapsulamento e validação de estado | Resumo fornecido; primeira aula; ementa, seção 1.6; validação em `aulas/exemplo2_carro.py` |
| 6, 14, 19 | Herança e reutilização | `pratica1/Animal.py`, `pratica1/Pessoa.py` |
| 7, 15, 20 | Polimorfismo | `polimorfismo/pratica1.py` |
| 8, 16 | Abstração | Resumo fornecido; primeira aula; ementa, seção 1.4 |
| 10 | Retorno e argumento padrão | `pratica2/aula.py` |
| 12 | Alteração de atributos e condicionais | `aulas/exemplo2_carro.py` |

Os enunciados adaptam os exemplos para serem independentes. `Conta`, `Livro` e `Aluno` são situações de avaliação criadas a partir desses conceitos. A convenção `_saldo` é explicitada no enunciado para não depender de memorização de sintaxe ausente dos exemplos práticos.
