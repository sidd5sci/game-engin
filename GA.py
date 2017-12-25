'''
Copyright {2017} {siddhartha singh | sidd5sci@gmail.com}

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''




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
        self.Population = []
        self.initialPopulation = 10
        self.genration = 0
        self.mutationRate = 10 # in percentage
        self.crossOverRate = 2 # in percentage
        #======================================
      
    def createRandomPopulation(self,n):
        for i in range(0,n):
                p = population()
                p.randomize()
                self.Population.append(p)
        
    def Genration(self):
        self.genration += 1
            
    def naturalSelection(self,task,**args):
        # run the GA simulation in physical world
        for i in range(0,len(self.Population)):
            fit(self.Population[i],task,**args)# pass the fintness function into this
            # by default fitness is depends on the time taken by the creature to perform the task
        for i in range(0,len(self.Population)):
            if self.Population[i].health < 20:
                self.Population[i].state = 'dead'

                
    def ShowFitness(self):
                
        for i in range(0,self.initialPopulation):
            self.Population[i].CalFitness()
            
    def findBestFitesest(self):
        parent1 = parent2 = self.Population[0]
        for i in range(1,self.initialPopulation):
            #print(parent1.fitness," | ",parent2.fitness," || ",Population[i].fitness)
            if parent1.fitness < self.Population[i].fitness:
                parent2 = parent1
                parent1 = self.Population[i]
            elif parent2.fitness < self.Population[i].fitness:
                parent2 = self.Population[i]
    def crossOverEngine(self):
        pass
    def mutation(self):
        pass
    def regenration(self):
        pass

def main():
    print 'Starting genetic sequence'
    createRandomPopulation(5)
    Genration()
if __name__ == '__main__':
   main()
