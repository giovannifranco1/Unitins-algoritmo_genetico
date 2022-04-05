from grade.aula import Aula
from grade.professor import Professor

lista_professores = []

lista_professores.append(Professor(nome='Jânio', dia='segunda', turno='manhã'))
lista_professores.append(Professor(nome='Tamies', dia='terça', turno='tarde'))
lista_professores.append(Professor(nome='Yhan', dia='quarta', turno='noite'))
lista_professores.append(Professor(nome='Júlio', dia='quinta', turno='manhã'))
lista_professores.append(Professor(nome='Brayan', dia='sexta', turno='tarde'))
lista_professores.append(Professor(nome='Iann', dia='segunda', turno='noite'))
lista_professores.append(Professor(nome='Giovanni', dia='terça', turno='manhã'))
lista_professores.append(Professor(nome='Alex', dia='quarta', turno='tarde'))
lista_professores.append(Professor(nome='Silvano', dia='quinta', turno='noite'))
lista_professores.append(Professor(nome='Napoleão', dia='sexta', turno='manhã'))
lista_professores.append(Professor(nome='Leandra', dia='segunda', turno='tarde'))
lista_professores.append(Professor(nome='Carlos', dia='terça', turno='noite'))
lista_professores.append(Professor(nome='Ligia', dia='quarta', turno='manhã'))
lista_professores.append(Professor(nome='Odi', dia='quinta', turno='tarde'))
lista_professores.append(Professor(nome='Mailson', dia='sexta', turno='noite'))

for professor in lista_professores:
    print(professor)
