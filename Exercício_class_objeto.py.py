# Exercícios de POO em Python

# 1
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

p1 = Pessoa("Maria")
p2 = Pessoa("João")
print(p1.nome)
print(p2.nome)


# 2
class Animal:
    def __init__(self, tipo):
        self.tipo = tipo

a1 = Animal("Cachorro")
a2 = Animal("Gato")
print(a1.tipo)
print(a2.tipo)


# 3
class Carro:
    def __init__(self, nome, estado="novo"):
        self.nome = nome
        self.estado = estado

fusca = Carro("Fusca")
ferrari = Carro("Ferrari", "usado")

print(fusca.estado)
print(ferrari.estado)


# 4
class Carro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

fusca = Carro("Fusca", "azul")
ferrari = Carro("Ferrari", "vermelha")

print(fusca.nome, "-", fusca.cor)
print(ferrari.nome, "-", ferrari.cor)


# 5
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota: "))
aluno1 = Aluno(nome, nota)
print("Aluno:", aluno1.nome, "- Nota:", aluno1.nota)


# 6
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

c1 = ContaBancaria(500)
c2 = ContaBancaria(1200)

print(c1.saldo)
print(c2.saldo)


# 7
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def mostrar_saldo(self):
        print("Saldo:", self.saldo)

c1 = ContaBancaria(300)
c2 = ContaBancaria(700)

c1.mostrar_saldo()
c2.mostrar_saldo()


# 8
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p1 = Produto("Arroz", 10)
p2 = Produto("Feijão", 8)
p3 = Produto("Macarrão", 6)

print(p1.nome, "-", p1.preco)
print(p2.nome, "-", p2.preco)
print(p3.nome, "-", p3.preco)


# 9
class Computador:
    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True

pc = Computador()
pc.ligar()
print("Computador ligado?", pc.ligado)


# 10
class Lampada:
    def __init__(self):
        self.estado = "apagada"

    def ligar(self):
        self.estado = "acesa"

l = Lampada()
l.ligar()
print("A lâmpada está", l.estado)


# 11
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

f1 = Funcionario("Carlos", 2500)
f2 = Funcionario("Ana", 3000)
print(f1.nome, "-", f1.salario)
print(f2.nome, "-", f2.salario)


# 12
class Cachorro:
    def latir(self):
        print("Au Au!")

dog = Cachorro()
dog.latir()


# 13
class Celular:
    def __init__(self, bateria=0):
        self.bateria = bateria

    def carregar(self):
        self.bateria += 10

c = Celular()
c.carregar()
print("Bateria:", c.bateria, "%")


# 14
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

l1 = Livro("Dom Casmurro", "Machado de Assis")
l2 = Livro("O Quinze", "Rachel de Queiroz")

print(l1.titulo, "-", l1.autor)
print(l2.titulo, "-", l2.autor)


# 15
class Aluno:
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso

a1 = Aluno("Paulo", "Biomedicina")
a2 = Aluno("Clara", "Direito")

print(a1.nome, "-", a1.curso)
print(a2.nome, "-", a2.curso)


# 16
class Conta:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

c = Conta()
c.depositar(100)
c.depositar(50)
print("Saldo atual:", c.saldo)


# 17
class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")

c = Conta(100)
c.sacar(50)
c.sacar(100)


# 18
class Pessoa:
    def falar(self):
        print("Olá, tudo bem?")

p = Pessoa()
p.falar()


# 19
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

marca = input("Digite a marca: ")
modelo = input("Digite o modelo: ")
ano = input("Digite o ano: ")

carro = Carro(marca, modelo, ano)
print(carro.marca, carro.modelo, carro.ano)


# 20
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

r = Retangulo(4, 5)
print("Área:", r.area())


# 21
class Aluno:
    def media(self, n1, n2):
        return (n1 + n2) / 2

a = Aluno()
print("Média:", a.media(8, 6))


# 22
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)

p = Produto("Camisa", 100)
p.desconto(10)
print("Preço com desconto:", p.preco)


# 23
class Pessoa:
    def __init__(self, idade):
        self.idade = idade

    def maior_de_idade(self):
        return self.idade >= 18

p = Pessoa(20)
print("Maior de idade?", p.maior_de_idade())


# 24
class Banco:
    def __init__(self):
        self.clientes = []

b = Banco()
b.clientes.append("Ana")
b.clientes.append("Pedro")
b.clientes.append("Lucas")

print(b.clientes)


# 25
class Motor:
    def __init__(self):
        self.ligado = False

    def ligar_motor(self):
        self.ligado = True

m = Motor()
m.ligar_motor()
print("Motor ligado?", m.ligado)


# 26
class Casa:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho

c1 = Casa("azul", "grande")
c2 = Casa("amarela", "pequena")

print(c1.cor, "-", c1.tamanho)
print(c2.cor, "-", c2.tamanho)


# 27
class Pessoa:
    def __init__(self):
        print("Pessoa criada")

p1 = Pessoa()
p2 = Pessoa()


# 28
class Carro:
    def __init__(self, estado):
        self.estado = estado

    def mostrar_estado(self):
        print("O carro está", self.estado)

c1 = Carro("novo")
c2 = Carro("usado")

c1.mostrar_estado()
c2.mostrar_estado()


# 29
class Computador:
    def __init__(self, ligado):
        self.ligado = ligado

    def info(self):
        if self.ligado:
            print("Computador ligado")
        else:
            print("Computador desligado")

pc1 = Computador(True)
pc2 = Computador(False)

pc1.info()
pc2.info()


# 30
class Aluno:
    def situacao(self, nota):
        if nota >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

a = Aluno()
a.situacao(8)
a.situacao(5)
