import scipy.spatial.distance as ssd
import scipy as scpy
import math as m
import time as t
import numpy.random as rnd
import matplotlib.pyplot as mpl
import numpy as np

def bruteforce(query_point,cloud):
    max_dis = ssd.euclidean(query_point,cloud[0])
    index = 0
    for point in cloud:
        tmp_dis = ssd.euclidean(query_point,point)
        if tmp_dis < max_dis:
            max_dis = tmp_dis
            index = cloud.index(point)
    return cloud[index]

def generate_random_data(dim,cloud_count,query_count):
    cloud = rnd.randint(-2**30,2**30,size=(cloud_count,dim))
    query_cloud = rnd.randint(-2**30,2**30,size=(query_count,dim))
    return cloud.tolist(),query_cloud.tolist()

the_value = 10000
rnd.seed(int(t.time()))
dim_arr_kd_tree = range(1,100)
# we tested 10 different dimension for bruteforce with variation of "the_value" to see
# if how the runtime of bruteforce behaves. Our hope is to see that there is a linear scaling
# or sth. else which is usefull. We found that the queary size is linear scaling. For the cloud size
# it seems linear but it should be quadradic.
dim_arr_bruteforce = range(1,100,10)
bruteforce_times = [0]*len(dim_arr_bruteforce)
kd_tree_times = [0]*len(dim_arr_kd_tree)

for dim in dim_arr_bruteforce:
    print(dim_arr_bruteforce.index(dim))
    cloud, query_cloud = generate_random_data(dim,int(the_value/100),int(the_value/10))
    start = t.time()
    for query_point in query_cloud:
        tmp = bruteforce(query_point, cloud)
    end = t.time()
    bruteforce_times[dim_arr_bruteforce.index(dim)] = end - start

for dim in dim_arr_kd_tree:
    if dim%25 == 0:
        print(dim)
    cloud,query_cloud = generate_random_data(dim,the_value,int(the_value/10))
    start = t.time()
    tree = scpy.spatial.KDTree(cloud,100)
    for query_point in query_cloud:
        tmp = tree.query(query_point)
    end = t.time()
    kd_tree_times[dim-1] = end - start

mpl.subplot(2,1,1)
mpl.title("bruteforce: " + str(int(the_value/100)) + " " + str(int(the_value/10)))
mpl.ylabel("time in sec")
mpl.xlabel("dimension")
mpl.tight_layout()
mpl.plot(dim_arr_bruteforce,bruteforce_times,"b")

mpl.subplot(2,1,2)
mpl.title("kd-tree:" + str(the_value) + " " + str(int(the_value/10)))
mpl.ylabel("time in sec")
mpl.xlabel("dimension")
mpl.tight_layout()
mpl.plot(dim_arr_kd_tree,kd_tree_times,"r")

mpl.tight_layout()
mpl.show()


