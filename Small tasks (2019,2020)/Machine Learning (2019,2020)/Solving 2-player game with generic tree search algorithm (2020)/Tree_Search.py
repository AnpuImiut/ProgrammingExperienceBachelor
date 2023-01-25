import math

"""
This is a implementation of the MinMax-Algorithmus for 2-Player games.
The class is able to switch on: alpha-beta-pruning, depth-restricted search and is able to return a hash map
for already evaluated game states.
The implemention functions at a abstract level and manages a internal tree with generic data structures.

The data structure must support following functions for the algorithmus to function properly:
- initial_gameState(): returns the node of the initial gameState
- is_leaf(node): returns if a given node is a leaf
- get_utility(node): returns the utility of the given node
- approximate_utility(node): in case of max depth one has to approximate the node ultility
- get_childs(node): returns the childs of given node in a fixed order(order should always be the same)
- get_nodeID(node): returns the unique identifier of the node; might be different for different classes
- set_node_utility(node,util): set the nodes utility; need for backtracking best path
- set_alpha_beta(node,vals): to set the alpha_beta vals of a node
- get_alpha_beta(node): get alpha, beta values of a node
- to_hash(node): computes a unique identificator for the node
- set_up_hash(node,util): best utility is known, but generic nodes have no utility so, they have to be greated on the fly

So a node should contain following members:
- ID
- value: equals the utility of this node( or its approximation in case of non-leaf)
- alpha_beta: list of size two(alpha=L[0],beta=L[1])
- childs: list of childs
- leaf: boolean
"""
class Tree_Search_Two_Sum_Game:
    def __init__(self, dataStructure,visible,alpha_beta,depth,hash):
        self.data_class = dataStructure
        # by default the root node is set to the initial gameState of the dataStructure, it also possible to change it to any node
        self.visible = visible
        self.alpha_beta_pruning = alpha_beta
        self.hash_able=hash
        if depth == -1:
            self.depth = math.inf
        else:
            self.depth = depth
    def set_root(self,node):
        self.root = node
    # computes the utility of the root node
    def get_root(self):
        return self.root
    def process_utility(self):
        # set up a looking up table for already processed utilities; first pos: utility, second pos: index of best child
        self.root = self.data_class.initial_gameState("max")
        if self.hash_able:
            self.hash_map = {}
        self.data_class.set_alpha_beta(self.root, [-math.inf, math.inf])
        root_util_max = self.Search(self.root,"Max",self.data_class.get_alpha_beta(self.root),0)
        self.root = self.data_class.initial_gameState("min")
        self.data_class.set_alpha_beta(self.root, [-math.inf, math.inf])
        root_util_min = self.Search(self.root,"Min",self.data_class.get_alpha_beta(self.root),0)
        return root_util_max,root_util_min
    def Search(self,node,mode,parent_alpha_beta,depth):
        if self.visible:
            print()
            print("Visit node:" ,self.data_class.get_nodeID(node), " as ",mode)
        if self.hash_able:
            if self.data_class.to_hash(node) in self.hash_map:
                return self.hash_map[self.data_class.to_hash(node)][0]
        if self.data_class.is_leaf(node):
            if self.visible:
                print("Visited leaf node ", self.data_class.get_nodeID(node), " with utility ", self.data_class.get_utility(node))
            return self.data_class.get_utility(node)
        if depth == self.depth:
            self.data_class.approximate_utility(node)
            if self.visible:
                print("Visited node ", self.data_class.get_nodeID(node), " at max depth with utility ", self.data_class.get_utility(node))
            return self.data_class.get_utility(node)
        # if we are not in a leaf node and visit node first time we want to set alpha,beta
        self.data_class.set_alpha_beta(node,parent_alpha_beta)
        if self.visible:
            print("alpha_beta before: ",self.data_class.get_alpha_beta(node))
        # this is a list of gameStates following from gameState 'node'
        possible_moves = self.data_class.get_childs(node)
        best_play = None
        if mode == "Max":
            best_util = self.Search(possible_moves[0],"Min",self.data_class.get_alpha_beta(node),depth+1)
            best_play=0
            self.data_class.set_alpha_beta(node, [max(best_util,self.data_class.get_alpha_beta(node)[0]), self.data_class.get_alpha_beta(node)[1]])
        else:
            best_util = self.Search(possible_moves[0], "Max", self.data_class.get_alpha_beta(node),depth+1)
            best_play = 0
            self.data_class.set_alpha_beta(node, [self.data_class.get_alpha_beta(node)[0], min(best_util,self.data_class.get_alpha_beta(node)[1])])
        # safe the index of the best play from current node; assumption is that the list of child is in a fixed order
        for ind,child in enumerate(possible_moves[1:]):
            alpha_beta = self.data_class.get_alpha_beta(node)
            if alpha_beta[0] >= alpha_beta[1] and self.alpha_beta_pruning:
                if self.visible:
                    print("alpha: ",alpha_beta[0],", beta: ",alpha_beta[1])
                    print("pruned at node ",self.data_class.get_nodeID(child))
                break
            tmp_util = best_util
            if mode == "Max":
                best_util = max(self.Search(child, "Min",self.data_class.get_alpha_beta(node),depth+1), best_util)
                if tmp_util != best_util:
                    best_play = (ind+1)
                self.data_class.set_alpha_beta(node, [max(best_util,self.data_class.get_alpha_beta(node)[0]), self.data_class.get_alpha_beta(node)[1]])
            else:
                best_util = min(self.Search(child, "Max", self.data_class.get_alpha_beta(node),depth+1), best_util)
                if tmp_util != best_util:
                    best_play = (ind+1)
                self.data_class.set_alpha_beta(node, [self.data_class.get_alpha_beta(node)[0], min(best_util,self.data_class.get_alpha_beta(node)[1])])
        if self.visible:
            print("Node ", self.data_class.get_nodeID(node), " gets utility ", best_util ," as ",mode)
            print("alpha_beta after: ", self.data_class.get_alpha_beta(node))
        self.data_class.set_node_utility(node,best_util)
        if self.hash_able:
            self.hash_map[self.data_class.to_hash(node)] = [best_util,best_play]
            #print(self.data_class.to_hash(node),self.hash_map[self.data_class.to_hash(node)])
        return best_util
    def backtrack_best_plays(self,node):
        plays = []
        goal_util = self.data_class.get_utility(node)
        print()
        print("Backtrack best plays")
        tmp_depth = 0
        while not (self.data_class.is_leaf(node) or tmp_depth == self.depth):
            possible_moves = self.data_class.get_childs(node)
            if self.hash_able:
                node = self.data_class.set_up_hash(node,goal_util)
                val,play = self.hash_map[self.data_class.to_hash(node)]
                plays.append(play)
            else:
                for ind,child in enumerate(possible_moves):
                    tmp_util = self.data_class.get_utility(child)
                    if tmp_util == goal_util:
                        plays.append(ind)
                        break
            if self.visible:
                print("chosen node ", self.data_class.get_nodeID(possible_moves[plays[-1]]), " with utility ",
                      self.data_class.get_utility(possible_moves[plays[-1]]))
            node = possible_moves[plays[-1]]
            tmp_depth += 1
        return plays
    def get_play(self,hash):
        print(self.hash_map[hash])



