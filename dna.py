############################################################################
###
###                        DNA handler 
###       --------------------------------------------
###
###
###
############################################################################  

import random

"""
======================================
| id,name ,code,active,comment| 
-------------------------------
|                             |
======================================

"""

geneLib = {'legs':'2',
       'hands':'4',
       'head':'1',
       'body':'3',
       'brain_neurons_layers':'3',
       'input_neurons':'5',
       'output_neuron':'6',
       'hiden_neuron':'8'}
GeneLib = ['legs',
           'hands',
           'head',
           'body',
           'brain_neurons_layers',
           'input_neurons',
           'output_neuron',
           'hiden_neuron']


class Gene:

   def __init__(self,_id_,name,state,comment,code):
       self._id_ = _id_  # gene id
       self.name = name  # name of the gene
       self.state = state # active/inactive
       self.comment = comment  # description of gene
       self.code = str(d_to_b(code)) # gene 8 binary bits

       for i in range(0,8-len(self.code)):
          self.code = '0'+self.code
   def get(self):
       print   '\n+===============================================================+'
       print   '| ID        :  ',self._id_
       print   '| Name      :  ',self.name
       print   '| State     :  ',self.state
       print   '| Comment   :  ',self.comment
       print   '| Sequence  :  ',self.code
       print   '+===============================================================+\n'

'''
==============================
         DNA Class
==============================
'''
class DNA:
   def __init__(self):
       self.dna = list()
   def addGene(self,name,state,comment,code):
       # starting the id 
       _id_ = 0
       if len(self.dna) > 0:
          # read the dna
          lastGene =  self.dna[len(self.dna)-1]
          _id_ = lastGene._id_ + 1
       if len(str(d_to_b(code))) <= 8:
          gene = Gene(_id_,name,state,comment,code)
          self.dna.append(gene)
       else:
         print 'gene code sequence must be 8 bits only (0 to 255)'
##       gene = Gene(_id_,name,state,comment,code)
##       self.dna.append(gene)
   def removeGene(self,_id_):
       for gene in self.dna:
          if gene._id_ == _id_:
             self.dna.remove(gene)
             break
   def crossOver(self,dna2,crossOverRate):
       # crossover rategives the number of genes those will be replaced
       dnaLengths = (len(self.dna),len(dna2))
       dnaLengths.sort()
       # arrange the genes of dna in a predefined order 
       self.dna.arrange('geneOrder')
       dna2.arrange('geneOrder')
       # calculate the crossing gene number
       rate = math.floor(crossOverRate*dnaLengths[1]*8/100)
       # loop through the genes of dna
       for i in range(0,dnaLenghts[1]): 
          # cross the genes of Dna1 and Dna2
          for g1,g2 in zip(self.dna,dna2):
             g1.cross(g2,rate)
   def arrange(self,order):
      pass
   def cross(self,gene,rate):
      pass
   def fitness(func,**args):
       if func:
          func(**args)
   def readDna(self):
       print '>>> DNA'
       for gene in self.dna:
          gene.get()
   def searchGene():
       pass
   def modifyGene(self,_id_,data):
       pass
   def activateGene(self,_id_):
       for gene in self.dna:
          if gene._id_ == _id_:
             gene.state = True
   def deactivateGene(self,_id_):
       for gene in self.dna:
          if gene._id_ == _id_:
             gene.state = False
   def randomDna(self,length=4):
       
       genePos = 0
       for i in range(0,length):
          if random.uniform(0,2) == 1:
             state = True
          else:state = False
          
          comment = ''
          code = int(random.uniform(0,24))
          name = GeneLib[genePos]
          self.addGene(name,state,comment,code)
          genePos+=1
   def mutateDna(self,mutationRate):
       # mutation rate lise between 0 and 1
       for i in range():
          pass
def b_to_d(b):# binary to decimal
    return int(b,2)
def d_to_b(d):# decimal to binary
    d = int(d)
    return int(bin(d)[2:])
   
if __name__ == '__main__':
   d1 = DNA()
   d1.addGene('legs',True,'this gene controlls the number of legs of the creature',6)
   d1.addGene('hands',True,'this gene controlls the number of hands of the creature',235)
   d1.readDna()
   d1.randomDna(3)
   d1.readDna()
  # from objects_lib import  xyz.py
