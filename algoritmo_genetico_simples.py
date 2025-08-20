#!/bin/python3
import random

####
#   Algoritmo Genético simples
#   Gera uma população definida por 'populationSize'
#   Dentre os membros da população pega o mais apto de e adiciona 'genes' dele em todos os outros
#   Itera durante epochs, definida previamente
####
class GeneticAlgorithm:

    def __init__(self, populationSize: int, epochs):

        self.pouplationSize = populationSize
        self.epochs = epochs
        self.population = []
        self.beginPopulation()


    def beginPopulation(self):

        for i in range(0, self.pouplationSize):
            random_list = [str(random.randint(0,1)) for x in range(0,5)]
            self.population.append(''.join(random_list))

    def fitnetssScore(self):
        global_solution = 0

        for epoch in range(0, self.epochs):
            self.summaryEpoch(epoch)
            local_solution = 0
            member_position = 0
            for pos, i in enumerate(self.population):

                local_result = self.desired(int(i, 2))
                if(local_result > local_solution):
                    local_solution = local_result
                    member_position = pos

            if(local_solution > global_solution):
                global_solution = local_solution

            self.updatePopulation(member_position,)
            self.summaryLocal(self.population[member_position], epoch)

        self.summaryGlobal(global_solution)

    def updatePopulation(self, member):
        for pos, i in enumerate(self.population):
            if(pos == member):
                continue

            self.population[pos] = str(self.population[member][:2] + self.population[pos][2:5])


    def desired(self, input):
        return input ** 2

    def getActualPopulation(self):
        return self.population

    def summaryLocal(self, member: str, epoch: int):
        print(f"Fim da {epoch} geração")
        print(F"Best member: {member}")

    def summaryEpoch(self, epoch):
        print(f"{epoch} Geração")

    def summaryGlobal(self, global_solution):
        print(f"Global score is {global_solution}")


geneticAlgo = GeneticAlgorithm(
    epochs=5,
    populationSize=5
)

geneticAlgo.fitnetssScore()