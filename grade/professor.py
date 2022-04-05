class Professor():
    def __init__(self, nome, dia, turno):
        self.nome = nome
        self.dia = dia
        self.turno = turno

    def __str__(self) -> str:
        return f'Professor: {self.nome}, Dia: {self.dia}, Turno: {self.turno}'