from grade.professor import Professor


class Aula():
    # def __init__(self, professor, materia, dia, turno, sala, periodo):
    def __init__(self, periodo, professor, materia, sala):
        self.periodo = periodo
        self.professor = Professor()
        self.materia = materia
        self.sala = sala
        
    def peso():
        return 1
    
    def __str__(self) -> str:
        return f'Período: {self.periodo}'
    
    #Disciplinas repetidas no mesma grade
    #Professores não podem dar aula em dias e turnos nas quais ele não está disponível