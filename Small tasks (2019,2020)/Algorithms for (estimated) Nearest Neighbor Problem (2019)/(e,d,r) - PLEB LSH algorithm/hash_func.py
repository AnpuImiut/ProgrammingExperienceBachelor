import random as rnd

class hashfunc_hamming:
    def __init__(self,d,i):
        self.dim = d
        self.index = i
    def random_hashfunc(self):
        self.index = rnd.randint(0,self.dim-1)
    def hash(self,value):
        return value[self.index]

class hashfunc_hamming_AND:
    def __init__(self,k,d):
        self.dim = d
        self.hashfunc_count = k
        self.hashfuncs = [hashfunc_hamming(self.dim,0) for i in range(self.hashfunc_count)]

        self.generate_hash_funcs()
    def generate_hash_funcs(self):
        for hashfunc in self.hashfuncs:
            hashfunc.random_hashfunc()
    def hash(self,value):
        return all(hfunc == self.hashfuncs[0].hash(value) for hfunc in self.hashfuncs)
    def setting(self):
        return str()
