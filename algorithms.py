from Environment import Environment


class node:
    def __init__(self,pathcost,action):
        self.pathcost=pathcost
        self.action=action

class depth_limited_tree_search:
    def __init__(self,DirtDistribution,start):
        self.env=Environment(DirtDistribution)
        
