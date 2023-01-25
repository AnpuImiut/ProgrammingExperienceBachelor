import numpy as np
import math
import time

def is_prime(number):
    for counter in range(2,math.ceil(math.sqrt(number))):
        if number%counter == 0:
            return False
    return True

class CMK_Tree:
    def __init__(self,eps,delta):
        self.eps = eps
        self.delta = delta
        self.file = None
        self.sketches= None
        self.p = None
        self.k = None
        self.n = None
        self.log_n = None
        self.m = None
        self.hashfkt_count = None
        self.tao = None
    def init_parameters(self,n,m):
        self.p = self.compute_p(math.ceil(2/self.eps))
        tmp = math.log2(n)
        tmp = math.ceil(tmp)
        self.n = int(math.pow(2,tmp))
        self.log_n = int(math.log2(self.n))
        self.compute_k()
        self.m = m
        self.hashfkt_count = math.ceil(math.log2(1/self.delta))
        self.build_sketches()
    # function for computing the vector from Z_p^k
    def get_Z_p_k_representation(self,number):
        answer = []
        while(number):
            old=number
            number=number//self.p
            answer.append(old-number*self.p)
        zeros = [0]* (self.k - len(answer))
        return answer+zeros
    # function to compute hash_values for given number(needs to be converted)
    def hash_func(self,hash_vec,number_vec):
        answer = 0
        for i in range(self.k):
            answer += hash_vec[i]*number_vec[i]
        return answer%self.p
    def build_sketches(self):
        self.sketches = []
        for i in range(self.log_n+1):
          self.sketches.append(np.zeros((self.hashfkt_count,self.p)))
    def compute_p(self,w):
        while(not is_prime(w)):
            w += 1
        return w
    def compute_k(self):
        self.k = int(math.ceil(math.log(self.n+1, self.p)+1))
    def read_data(self,filename):
        self.file = open(filename,"r")
        n = int(self.file.readline())
        m = int(self.file.readline())
        self.tao = int(self.file.readline())
        self.init_parameters(n,m)
    def run(self):
        start_time = time.time()
        count = 0
        percent = [True,True,True]
        for entry in self.file:
            self.compute_one_value(entry)
            if(count/self.m >= 1/4 and percent[0]):
                print("25%")
                percent[0]=False
            if (count / self.m >= 2 / 4 and percent[1]):
                print("50%")
                percent[1]=False
            if (count / self.m >= 3 / 4 and percent[2]):
                print("75%")
                percent[2]=False
            count = count + 1
        runtime = time.time() - start_time
        print("Runtime of CountMinSketchTree: ", runtime, " sec")
    def compute_representative(self,interval_size,value):
        return int(max([(value - 1) // (interval_size) * interval_size, 0]))
    def compute_one_value(self,number):
        interval_size = self.n
        val = int(number)
        for j in range(self.log_n + 1):
            representative = self.compute_representative(interval_size, val)+1
            repres_vec = self.get_Z_p_k_representation(representative)
            for i in range(1,self.hashfkt_count+1):
                vec_a = self.get_Z_p_k_representation(i)
                tmp_hash_value = self.hash_func(vec_a,repres_vec)
                self.sketches[j][i-1][tmp_hash_value] = self.sketches[j][i-1][tmp_hash_value] + 1
            interval_size = interval_size / 2
    def ausgabe(self):
        print("p:",self.p)
        print("k",self.k)
        print("n",self.n)
        print("log_n",self.log_n)
        print("m",self.m)
        print("sketches")
        for i in self.sketches:
            print(i)
            print()
