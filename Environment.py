#Prepared by Jonah Marz
#Pawprint jmmpxc
# This file serves to create the Environment for the program and nothing more

class Environment:
    def __init__(self,DirtDistribution,total):
        locations=[[(i,j) for j in range(1,total+1)] for i in range(1,total+1)]
        self.grid={j:False for i in locations for j in i}
        for dirt in DirtDistribution:
            if dirt in self.grid.keys():
                self.grid[dirt]=True

# class Cell:
#     def __init__(self,location,dirty):
#         self.location=location
#         self.dirty=dirty
# DirtDistribution=[(1,1),(1,4),(1,5),(2,1),(2,4),(2,5),(3,5),(4,1),(4,3),(5,1),(5,4),(5,5)]
#
# instance=Environment(DirtDistribution,5)
# for i  in sorted(instance.grid.keys(),key=lambda tup:(tup[0],tup[1])):
#     print i,instance.grid[i]
