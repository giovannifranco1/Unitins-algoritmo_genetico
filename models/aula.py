class Aula():
    def __init__(self, periodo, professor, materia, sala):
        self.periodo = periodo
        self.professor = professor
        self.materia = materia
        self.sala = sala
    
    def __str__(self) -> str:
        return f'Período: {self.periodo}, Professor: {self.professor}, Matéria: {self.materia}, Sala: {self.sala}'