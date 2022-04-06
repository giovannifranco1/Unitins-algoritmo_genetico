# -*- coding: utf-8 -*-

from prettytable import PrettyTable
from matplotlib import pyplot as pl
import random as rd

from ag import AG
from models.professor import Professor
from models.aula import Aula

my_table = PrettyTable()

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

# lista_aulas = []

# lista_aulas.append(Aula(periodo=1, professor=lista_professores[0], materia='Algoritmos', sala='Sala 1'))
# lista_aulas.append(Aula(periodo=1, professor=lista_professores[1], materia='Redes', sala='Sala 2'))
# lista_aulas.append(Aula(periodo=1, professor=lista_professores[2], materia='Inglês', sala='Sala 3'))
# lista_aulas.append(Aula(periodo=1, professor=lista_professores[3], materia='Português', sala='Sala 4'))
# lista_aulas.append(Aula(periodo=1, professor=lista_professores[4], materia='Front End', sala='Sala 5'))

nomes = []
dias = []
turnos = []

for professor in lista_professores:
    nomes.append(professor.nome)
    dias.append(professor.dia)
    turnos.append(professor.turno)
limite = 3  
tamanho_populacao = 20
taxa_mutacao = 0.01
numero_geracoes = 100

ag = AG(tamanho_populacao)

resultado = ag.solve(taxa_mutacao,numero_geracoes,espacos,valores,limite)

for i in range(len(lista_professores)):
    if resultado[i] == 1:
      print(f'Professor: {lista_professores[i].nome}')
        # print("Nome: %s \n R$: %s \n " % (
        #     lista_professores[i].name, 
        #     lista_professores[i].value))
    
pl.plot(ag.solution_list)
pl.title("Acompanhamento dos valores")
pl.show()

# my_table.field_names = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
# my_table.add_row([lista_professores[rd.randint(0, 14)], lista_professores[rd.randint(0, 14)], lista_professores[rd.randint(0, 14)], lista_professores[rd.randint(0, 14)], lista_professores[rd.randint(0, 14)]])
# my_table.add_row([lista_professores[5], lista_professores[6], lista_professores[7], lista_professores[8], lista_professores[9]])
# my_table.add_row([lista_professores[10], lista_professores[11], lista_professores[12], lista_professores[13], lista_professores[14]])
# print(my_table)

# for professor in lista_professores:
#     print(professor)
