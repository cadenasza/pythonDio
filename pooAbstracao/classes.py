from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversário! Agora tem {self.idade} anos.")
        
    @abstractmethod
    def estudar(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"O aluno {self.nome} fez a matricula.")
        
    def estudar(self):
        print(f"O aluno {self.nome} está estudando {self.curso} na turma {self.turma}.")
        
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} acabou de bater seu ponto.")    
        
    def estudar(self):
        print(f"O funcionario {self.nome} está estudando para se aprimorar no cargo de {self.cargo}.")
                


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.especialidade}.")
        
    def estudar(self):
        print(f"O professor {self.nome} está estudando para se aprimorar no cargo de professor de {self.especialidade}.")
        
