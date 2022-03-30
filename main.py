from grade.grade import Grade, Aula
from grade.professor import Professor

# periodo1 = grade.Grade('Brayan', 'IA', 'Segunda', 'Matutino', '2', '1')
# periodo2 = grade.Grade('Brayan', 'IA', 'Segunda', 'Matutino', '2', '2')

professor1 = Professor('Jânio', 'segunda')
grade1 = Aula('1 período')

print(grade1)

professores = {'professor': [Professor('Jânio'), Professor('Silvano'), Professor('Thamires')]}