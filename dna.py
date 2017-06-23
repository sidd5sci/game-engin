
  



"""
======================================
| id,name ,code,active,comment| 
-------------------------------
|                             |
======================================

"""
class Gene:

   def __init__(self,_id_,name,state,comment,code):
       self._id_ = _id_  # gene id
       self.name = name  # name of the gene
       self.state = state # active/inactive
       self.comment = comment  # description of gene
       self.code = list(code) # gene 8 binary bits  
   def get(self):
       print   '\n+===============================================================+'
       print   '| ID        :  ',self._id_
       print   '| Name      :  ',self.name
       print   '| State     :  ',self.state
       print   '| Comment   :  ',self.comment
       print   '| Sequence  :  ',self.code
       print   '+===============================================================+\n'

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
       if len(code) <= 8:
          gene = Gene(_id_,name,state,comment,code)
          self.dna.append(gene)
       else:
         print 'gene code sequence must be 8 bits only'
   def removeGene(self,_id_):
       for gene in self.dna:
          if gene._id_ == _id_:
             self.dna.remove(gene)
             break
   def crossOver(self,dna2,crossOverRate):
       pass
   def readDna(self):
       for gene in self.dna:
          gene.get()
   def modifyGene(self,_id_):
       pass
   def activateGene(self,_id_):
       for gene in self.dna:
          if gene._id_ == _id_:
             gene.state = True
   def deactivateGene(self,_id_):
       for gene in self.dna:
          if gene._id_ == _id_:
             gene.state = False
   def randomDna(self,length):
       for i in range(0,length):
          if random.uniform(0,2) == 1:
             state = True
          else:state = False
          
          comment = ''
          code = randomBinaryCodes()
          name = readGeneLib('names')
          self.addGene(name,state,comment,code)
   def mutateDna(self,mutationRate):
       # mutation rate lise between 0 and 1
       pass
 
if __name__ == '__main__':
   d1 = DNA()
   d1.addGene('legs',True,'this gene controlls the number of legs of the creature','10101011')
   d1.addGene('hands',True,'this gene controlls the number of legs of the creature','10101011')
   d1.readDna()
