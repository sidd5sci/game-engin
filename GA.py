
import random,time
import math
from dna import *
from vector import *

class population:

      def __init__(self):
          self.dna = DNA()
          self.fitness = 100
          self.pos = vertex()
          self.objectType = ' '
          self.objectId = -1
      def randomPopulation(self):#this shold create each time differently
          
          self.fitness = 100
          self.pos.assign(10,0,10)
          self.dna.randomDna(8)
          
      
              
      



        

def Genration():
    global genration
    global Population
    global initialPopulation
    genration += 1
    
    for i in range(0,initialPopulation):
        Population[i].LiveThePopulation()
      
         
def ShowFitness():
    global Population
    global initialPopulation
    
    for i in range(0,initialPopulation):
        Population[i].CalFitness()
        
def FindBestFitesest():
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
#======================================
Population = []
initialPopulation = 10
genration = 0
mutationRate = 10 # in percentage
crossOverRate = 2 # in percentage
#======================================
def main():
    print 'Starting genetic sequence'

if __name__ == '__main__':
   main()
