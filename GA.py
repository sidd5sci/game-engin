
import random,time
import math
from dna import *


class population:

      def __init__(self):
          self.dna = DNA()
          self.fitness = 0 # fitness is how good the creature is in finding the goal into the simulation 
          self.objectType = ' '
          self.objectId = -1
          self.health = 100 # health is physical health of the creature
          self.state = 'alive'
      def randomize(self):
          
          self.fitness = 0
          self.health = 100
          self.dna.randomDna(8)
          
      
class GA:
    def __init__(self):
        #======================================
        Population = []
        initialPopulation = 10
        genration = 0
        mutationRate = 10 # in percentage
        crossOverRate = 2 # in percentage
        #======================================

      
    def createRandomPopulation(self,n):
        for i in range(0,n):
                p = population()
                p.randomize()
                Population.append(p)


            

    def Genration(self):
        global genration
        genration += 1
            
    def naturalSelection(self,task,**args):
        # run the GA simulation in physical world
        for i in range(0,len(Population)):
            fit(Population[i],task,**args)# pass the fintness function into this
            # by default fitness is depends on the time taken by the creature to perform the task
        for i in range(0,len(Population)):
            if Population[i].health < 20:
                Population[i].state = 'dead'

                
    def ShowFitness(self):
        global Population
        global initialPopulation
        
        for i in range(0,initialPopulation):
            Population[i].CalFitness()
            
    def findBestFitesest(self):
        global parent1
        global parent2
        global Population
        global initialPopulation
        parent1 = parent2 = Population[0]
        for i in range(1,initialPopulation):
            #print(parent1.fitness," | ",parent2.fitness," || ",Population[i].fitness)
            if parent1.fitness < Population[i].fitness:
                parent2 = parent1
                parent1 = Population[i]
            elif parent2.fitness < Population[i].fitness:
                parent2 = Population[i]


def main():
    print 'Starting genetic sequence'
    createRandomPopulation(5)
    Genration()
if __name__ == '__main__':
   main()
