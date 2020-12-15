# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:49:42 2020

@author: briya
"""
import random
#Resultado a la que se quiere llegar de los 10 individuos que cumplen la funcion objetivo
#En realidad se espera el resultado [5,4,4,3,3,3,2,2,1,1] que es el valor de x en la funcion f(x)
#Ya que la funcion hallara al individuo que cumpla esa caracteristica
modelEnd = [155,84,84,39,39,39,14,14,3,3] 
largeIndividual = 10 

num = 10 #Cantidad de individuos
generation = 100 #Generaciones
pressure = 3 #individual>2
mutation_chance = 0.2



def individual(min, max):
    return[random.randint(min, max) for i in range(largeIndividual)]

def newPopulation():
    return [individual(1,5) for i in range(num)]

# Funcion f(x) = x^3 + x^2 + x 
def functionType(individual):
    fitness = 0
    for i in range(len(individual)):
        #Se elige al individuo con mejores genes tal que cumpla la funcion
        #No se guarda el resultado de la funcion sino al individuo que cumple los requisitos
        var = (individual[i]**3 + individual[i]**2 + individual[i])
        #Buscamos si el individuo tiene los genes en el orden correcto si es asi se aumenta el fitness
        if var == modelEnd[i]:
            fitness += 1
    return fitness

def selection_and_reproduction(population):
    evaluating = [(functionType(i), i) for i in population]
    print("eval",evaluating)
    evaluating = [i[1] for i in sorted(evaluating)]
    
    population = evaluating
    selected = evaluating[(len(evaluating)-pressure):]
    print("selected :",selected)
    #Apartir de aqui se aplica el cruce
    for i in range(len(population)-pressure):
        
        pointChange = random.randint(1,largeIndividual-1)
        father = random.sample(selected, 2)
        population[i][:pointChange] = father[0][:pointChange]
        population[i][pointChange:] = father[1][pointChange:]
        
        #print("-------------")
        #print(father[0])
        #print(father[1])
        #print(pointChange)
        #print(population[i])
        
    return population

def mutation(population):
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance: 
            pointChange = random.randint(1,largeIndividual-1) 
            new_val = random.randint(1,5) 
            while new_val == population[i][pointChange]:
                new_val = random.randint(1,5)
            population[i][pointChange] = new_val
    return population

#Funcion para verificar en que generacion se encuentra el individuo buscado
def buscar(population, modelEnd):
    cont = 0
    for i in range(len(population)):
        for j in range(len(population[i])):
            #print(population[i][j] ,"[",i,"] ","[", j,"]\n")
            f = (population[i][j]**3 + population[i][j]**2 + population[i][j])
            if(f == modelEnd[j]):
                cont = cont + 1
        if(cont == len(modelEnd)):
            print("\nIndividuo Buscado :\n")
            print(population[i],"\n")
            break
        else:
            cont = 0
    if(cont == len(modelEnd)):
        return True
    else:
        return False
                

population = newPopulation()

for i in range(generation):
    
    print("\n*********GENERACION ",i," ***********\n")
    print("\nPopulation Begin:\n%s"%(population))
    population = selection_and_reproduction(population)
    print("\Selection Population:\n%s"%(population))
    population = mutation(population)
    print("\Mutation Population:\n%s"%(population))
    evaluating = [(functionType(i), i) for i in population]
    print("eval",evaluating)
    if(buscar(population, modelEnd)):break

