import numpy as np
import math
import time

class bruteforce:
    def __init__(self):
        self.file = None
        self.n = None
        self.m = None
        self.count = None
    def read_data(self,filename):
        self.file = open(filename,"r")
        n = int(self.file.readline())
        m = int(self.file.readline())
        self.tao = int(self.file.readline())
        self.count = np.zeros(n)
    def run(self):
        start = time.time()
        for entry in self.file:
            tmp = int(entry)
            self.count[tmp-1] = self.count[tmp-1] + 1
        runtime = time.time() - start
        print("Runtime of Bruteforce: ", runtime, " sec")
    def ausgabe(self):
        print(self.count)