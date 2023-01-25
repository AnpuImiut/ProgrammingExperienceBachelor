import numpy as np
import math
import time
import cProfile

def Hamming_dis(q,p):
    tmp = [q[index]!=p[index] for index in range(len(q))]
    tmp = filter(lambda x : x == True,tmp)
    return len(list(tmp))

def create_query_points(points,dim):
    query_points = points[:1000]
    for q in query_points:
        flips = np.random.choice(range(dim),10,replace=False)
        #print(flips)
        for ind in flips:
            q[ind] = not q[ind]
    return query_points

class PLEB_via_localitly_sensitive_hashing:
    def __init__(self,eps,delta,r,d,p_cloud,q_cloud):
        self.eps = eps
        self.delta = delta
        self.radius = r
        self.dim = d
        self.n = len(p_cloud)
        self.p1 = 1-self.radius/self.dim
        self.p2 = 1-(1+eps)*self.radius/self.dim
        self.rho = math.log2(self.p1)/math.log2(self.p2)
        self.k = math.ceil(math.log(self.n,(1/self.p2)))
        self.L = math.ceil(math.pow(self.n,self.rho)/self.p1)
        self.m = 1
        #self.m = math.ceil(math.log(self.delta)/math.log(5/6))
        self.points = p_cloud
        self.queries = q_cloud

        self.count1 = []
        self.count2 = []
        self.count3 = []
        self.list_of_AND_hashfuncs = None
        self.hash_table = None
    def restart(self):
        self.list_of_AND_hashfuncs = np.random.randint(0,self.dim-1,size=(self.L*self.k))
        self.list_of_AND_hashfuncs = self.list_of_AND_hashfuncs.tolist()
        # print(len(self.list_of_AND_hashfuncs))
        # for i in range(self.L):
        #     print(self.list_of_AND_hashfuncs[self.k*i:self.k*(i+1)])
        print("creating hash table")
        self.hash_table = []
        # counter = 0
        for point in self.points:
            for i in range(self.L):
                for j in range(self.k):
                # print(point)
                # print(self.list_of_AND_hashfuncs[self.k*i:self.k*(i+1)])
                # if self.hash_AND(point,i) == True:
                #     counter +=1
                # print(self.hash_AND(point,i))
                    self.hash_table.append(self.hash(point,i,j))
        #print("counter",counter)
    def run(self):
        for i in range(self.m):
            print("m_loop:",i)
            self.restart()
            print("start querying")
            tmp1 = 0
            tmp2 = 0
            tmp3 = 0
            counter= 0
            for q in self.queries:
                #print(q)
                counter += 1
                if counter%100 == 0:
                    print(counter)
                tmp1,tmp2,tmp3 = self.evaluate(q,tmp1,tmp2,tmp3)
            self.count1.append(tmp1)
            self.count2.append(tmp2)
            self.count3.append(tmp3)
    def evaluate(self,value, c1,c2,c3):
        counter = 0
        for i in range(self.L):
            for j in range(self.n):
                if self.hash_table[j*self.k*self.L+self.k*i:j*self.k*self.L+self.k*i+self.k] == self.hash_AND_alternative(value,i):
                    if Hamming_dis(self.points[j],value) <= (1+self.eps)*self.radius:
                        #print("index of point",j)
                        c1 += 1
                        return c1,c2,c3
                    else:
                        counter += 1
                        if counter > 3*self.L:
                            c2 += 1
                            return c1,c2,c3
        c3 += 1
        #print(counter)
        return c1,c2,c3
    def hash_AND_alternative(self,value,i):
        compare_list = self.list_of_AND_hashfuncs[self.k*i:self.k*(i+1)]
        answer = []
        for ind in compare_list:
            answer.append(value[ind])
        return answer
    def hash(self,value,i,j):
        return value[self.list_of_AND_hashfuncs[i*self.k+j]]
    def output(self):
        print("(eps,delta,radius):",self.eps,self.delta,self.radius)
        print("(n,dim)",self.n,self.dim)
        print("(p1,p2,rho)",self.p1,self.p2,self.rho)
        print("(k,L,m)",self.k,self.L,self.m)
        #print(self.list_of_AND_hashfuncs)
        #print(self.hash_table)
    def get_counts(self):
        return self.count1,self.count2,self.count3
    def change_queries(self,query_points):
        self.queries = query_points
        self.count1.clear()
        self.count2.clear()
        self.count3.clear()

# pr = cProfile.Profile()
np.random.seed(int(time.time()))
dim = 100
r = 20
points = np.random.randint(0,2,size=(10000,dim))
query_points_nrnd = create_query_points(points,dim)
query_points_rnd = np.random.randint(0,2,size=(1000,dim))
LHS = PLEB_via_localitly_sensitive_hashing(0.2,0.05,r,dim,points,query_points_nrnd)
LHS.output()

# pr.enable()
LHS.run()
# pr.disable()
counts1_nrnd,counts2_nrnd,counts3_nrnd = LHS.get_counts()
print("distribution(not random):",counts1_nrnd,counts2_nrnd,counts3_nrnd)

LHS.change_queries(query_points_rnd)
# pr.enable()
LHS.run()
# pr.disable()

counts1_rnd,counts2_rnd,counts3_rnd = LHS.get_counts()
print("distribution(random):",counts1_rnd,counts2_rnd,counts3_rnd)
# pr.print_stats(sort="calls")

