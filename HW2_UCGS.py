#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Frontier is a queue, and we use a 4 elements sublist in the Frontier to represent a node on the tree
# closed is used to represent nodes that have been visited          
#sublist[0] shows the level of the node & the action sequences 
#                      the first digit in sublist[0] shows the level of the node, other digits after that shows the action sequences 
#                   like 3513 3 level3
#                              5 the action at level1 up
#                              1 the action at level2 no op
#                              3 the action at level3 left
#           sublist[1]   the total cost
#           sublist[2]   the vauum cleaner location x asis
#           sublist[3]   the vauum cleaner location y asis
#sublist[0] shows the level of the node 1 means level1                       
# Result has the same structure with Frontier, and it's the output of the program


# In[2]:


import math
import time
import sys
sys.setrecursionlimit(1000000000)


# In[3]:


vcl1=[3,2]
vcl2=[3,3]


# In[4]:


ds1 = [[1,1],[1,4],[1,5],[2,1],[2,4],[2,5],[3,5],[4,1],[4,3],[5,1],[5,4],[5,5]] #Dirty squares
ds2 = [[1,1],[1,3],[2,4],[3,1],[3,4],[4,1],[4,4],[5,1]]


# In[5]:


Left_Cost = -1
Right_Cost = -1.1
Up_Cost = -1.2
Down_Cost = -1.3
Suck_Cost = -0.2
NoOp_Cost = 0
Clean_up_Cost = 4


# In[6]:


Action = ['Block','NoOp', 'Suck', 'Left', 'Right', 'Up', 'Down'] #There are 5 actions for agent & order by cost decs 
# The list start from 1
Action_Cost = [0,NoOp_Cost, Suck_Cost, Left_Cost, Right_Cost, Up_Cost, Down_Cost]


# In[7]:


def Sort(List): 
    # https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    List.sort(key = lambda x: x[1], reverse=True) 
    return List


# In[8]:


def firstDigit(n) : 
    #https://www.geeksforgeeks.org/find-first-last-digits-number/  
    if n == 0:
        return n
    else:
        # Find total number of digits - 1 
        digits = (int)(math.log10(n)) 
        # Find first digit 
        n = (int)(n / pow(10, digits)) 
        # Return first digit 
        return n; 


# In[9]:


def fromStart(inp, del1):
    if inp == 0:
        return 0
    else:
        #https://www.geeksforgeeks.org/program-to-delete-nth-digit-of-a-number/  
        inp = str(inp)
        inp1 = inp[0:del1 - 1]
        inp2 = inp[del1:len(inp)]
        return int(inp1 + inp2)


# In[10]:


def UCGS(ds,vcl,depth):
    path_cost=0
    Frontier=[[0,path_cost,vcl[0],vcl[1]]]
    Result=[]
    Closed=[]
    
    UCGS_Visit(ds,vcl,depth,Frontier,Result,Closed)
    return Result
    
    


# In[11]:


def UCGS_Visit(ds,vcl,depth,Frontier,Result,closed):
    Index=[]
    
    for n in Frontier:
        if n[0]-pow(10,depth)>=0:
            Result.append(n)
            Index.append(n)
    for n in Index:
        Frontier.remove(n)
    if len(Frontier)==0:
        return Result
    else:
        previous_values=Frontier.pop(0)
        path_cost_previous=previous_values[1]
        level_previous=firstDigit(previous_values[0])
        #print("The level_previous is"+str(level_previous))
        node_previous=fromStart(previous_values[0],1)
        #print("the previous node is"+str(node_previous))
        vclx=previous_values[3]
        vcly=previous_values[2]
        
        level=level_previous+1
        
        for i in range(len(Action[1:])):
            i=i+1
            print("Action is "+str(i))
            clean_cost=0
            
            if i==2:
                vclytmp=vcly
                vclxtmp=vclx
                for n in ds:
                    if[vclytmp,vclxtmp]==n:
                        clean_cost=4
                        ds.remove(n)
            elif i==3:
                vclxtmp=vclx-1
                vclytmp=vcly
            elif i==4:
                vclxtmp=vclx+1
                vclytmp=vcly
            elif i==5:
                vclytmp=vcly-1
                vclytmp=vclx
            elif i==6:
                vclytmp=vcly+1
                vclxtmp=vclx
            else:
                vclytmp=vcly
                vclxtmp=vclx
            if vclxtmp>5 or vclxtmp<1:
                continue
            elif vclytmp>5 or vclytmp<1:
                continue
            #print("The VCL is["+str(vclytmp)+","+str(vclxtmp))
            
            node=level*(pow(10,level))+node_previous*10+i
            path_cost=path_cost_previous+Action_Cost[i]+clean_cost
            
            
            if node not in closed:
                closed.append(node)
                Frontier.append([node,path_cost,vclytmp,vclxtmp])
        Sort(Frontier)
        print("The Frontier is "+str(Frontier))
        #print("The Result is "+str(Result))
        UCGS_Visit(ds,vcl,depth,Frontier,Result,closed)


# ## Test Case 1

# In[12]:


#Start CPU Time
start = time.clock()


# In[13]:


Result=UCGS(ds1,vcl1,6)


# In[14]:


#End CPU Time
end =  time.clock()
CPU_Time = end - start


# In[15]:


cost = []
for i in Result:
    cost.append(i)
    
cost = Sort(cost)


# In[16]:


print("b.The best solution " + str(cost[0][0]) 
      + " And the point is " + str(cost[0][1]))
print("c.The number of nodes (6 depths) " + str(len(cost)))
print("d.CPU time is " + str(CPU_Time))

