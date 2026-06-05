from classes import *

def main():
    a1 = Aluno("Maria", 28, "Engenharia de Software", "1tdspf")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    
    
    f1 = Funcionario("João", 35, "Analista de Sistemas", "TI")
    f1.fazer_aniversario()
    f1.bater_ponto()
    
    
    p1 = Professor("Ana", 40, "Matemática", "Doutorado")
    p1.fazer_aniversario()
    p1.dar_aula()
    
    
    a1.estudar()
    f1.estudar()
    p1.estudar()
    
    
    
if __name__ == "__main__":
    main()