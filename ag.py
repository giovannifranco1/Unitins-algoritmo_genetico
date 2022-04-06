from random import random

'''
Bom - Se encaixa - 3
Médio - Consegue encaixar alguns individuos - 2
Ruim - Não encaixa - 1
'''

class Individuo():
    def __init__(self, nome, dia, turno, generation = 0):
        self.nome = nome
        self.dia = dia
        self.turno = turno
        self.generation = generation
        self.fitness = 0
        self.chromosome = []
        self.weight_sum = 0
        
        for i in range(len(dia)):
            if random() < 0.5:
                self.chromosome.append(0)
            else:
                self.chromosome.append(1)

    def rating(self):
        fitness = 0
        weight_sum = 0
        for i in range(len(self.chromosome)):
            if(self.chromosome[i] == 1):
                fitness += self.values[i]
                weight_sum += self.weights[i]
        if weight_sum > self.weight_limit:
            fitness = 1
        self.fitness = fitness
        self.weight_sum = weight_sum
    
    def crossover(self, other_individual):
        chromosome_split_mark = round(random() * len(self.chromosome))
        
        child1 = other_individual.chromosome[0:chromosome_split_mark] + self.chromosome[chromosome_split_mark::]
        child2 = self.chromosome[0:chromosome_split_mark] + other_individual.chromosome[chromosome_split_mark::]
        
        children = [Individuo(self.weights,self.values,self.weight_limit,self.generation + 1),
                  Individuo(self.weights,self.values,self.weight_limit,self.generation + 1)]
        children[0].chromosome = child1
        children[1].chromosome = child2
        
        return children
    
    def mutation(self,mutation_rate):
        for i in range(len(self.chromosome)):
            if random() < mutation_rate:
                if self.chromosome[i] == 1:
                    self.chromosome[i] = 0
                else:
                    self.chromosome[i] = 1
        return self

class AG():
    def __init__(self,population_size):
        self.population_size = population_size
        self.population = []
        self.generation = 0
        self.best_solution = 0
        self.solution_list = []
    
    def initialize_population(self,weights,values,weight_limit):
        for _ in range(self.population_size):
            self.population.append(Individuo(weights,values,weight_limit))
        self.best_solution = self.population[0]
        
        for individual in self.population:
            individual.rating()
        
    def order_population(self):
        self.population = sorted(self.population, 
                                key = lambda population: population.fitness, 
                                reverse=True)
    
    def best_individual(self,individual):
        if individual.fitness > self.best_solution.fitness:
            self.best_solution = individual
            
    def fitness_sum(self):
        fitness = 0
        for individual in self.population:
            fitness += individual.fitness
        return fitness
    
    def elitism(self, fitness_sum):
        individual = -1
        elite = random() * fitness_sum
        fitness = 0
        breakpoint = 0
        
        while breakpoint < len(self.population) and fitness < elite:
            fitness+= self.population[breakpoint].fitness
            individual+= 1
            breakpoint += 1
        return individual
    
    def print_generation(self):
        best_individual = self.population[0]
        print("Geração: %s -> Valor: %s -> Espaço: %s -> Cromossomo: %s" % (
        self.population[0].generation,
        best_individual.fitness,
        best_individual.weight_sum,
        best_individual.chromosome))
        
    def solve(self, mutation_rate,number_of_generations,weights,values,weight_limit):
        self.initialize_population(weights,values,weight_limit)
        
        self.order_population()
        self.best_solution = self.population[0]
        self.solution_list.append(self.best_solution.fitness)
        self.print_generation()
        for _ in range(number_of_generations):
            fitness_sum = self.fitness_sum()
            new_population = []
            for __ in range(0, self.population_size, 2):
                father1 = self.elitism(fitness_sum)
                father2 = self.elitism(fitness_sum)
                
                children = self.population[father1].crossover(self.population[father2])
                new_population.append(children[0].mutation(mutation_rate))
                new_population.append(children[1].mutation(mutation_rate))
            
            self.population = list(new_population)
            
            for individual in self.population:
                individual.rating()
                
            self.order_population()
            
            self.print_generation()
            
            best_individual = self.population[0]
            self.solution_list.append(best_individual.fitness)

            self.best_individual(best_individual)
            
        print("\nMelhor Solução -> Geração: %s \nValor: %s \nEspaço: %s \nCromossomo: %s" % (
            self.best_solution.generation,
            self.best_solution.fitness,
            self.best_solution.weight_sum,
            self.best_solution.chromosome))
            
        return self.best_solution.chromosome 