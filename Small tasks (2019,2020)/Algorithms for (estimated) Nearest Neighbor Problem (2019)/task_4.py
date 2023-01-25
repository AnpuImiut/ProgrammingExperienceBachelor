import scipy.spatial.distance as ssd
import math as m

# the exact oracle for (eps,r)-PLEB
def nearest_point(eps,radius,query_point,cloud):
    for point in cloud:
        if ssd.euclidean(point,query_point) <= radius*(1+eps):
            return True, point
    return False, None

# binary search for a real numbered interval, thats why a precision value is needed
def binary_search_eps_NNS(eps,Rmax,query_point,cloud,precision):
    left=m.pow(1+eps,-m.ceil(1+m.log(2,1+eps)))
    right=Rmax/eps
    mid = (left+right)/2
    point = None
    final_mid = None
    print("starting (left/mid/right):",left,mid,right)
    print("precision:", precision)
    while(m.fabs(left-right) >= precision):
        direction,tmp = nearest_point(eps,mid,query_point,cloud)
        # it can happen that the last step results into NO and the precision is reached
        # thats why it is important to save the last successful step
        if point == None:
            point = tmp
            final_mid = mid
        elif tmp is not None:
            point = tmp
            final_mid = mid
        # part of binary search
        if(direction):
            right = mid
            mid = (left+right)/2
        else:
            left = mid
            mid = (left+right)/2
    print("ending (left/mid/right):", left, mid, right)
    return final_mid, point

def bruteforce(query_point,cloud):
    max_dis = ssd.euclidean(query_point,cloud[0])
    index = 0
    for point in cloud:
        tmp_dis = ssd.euclidean(query_point,point)
        if tmp_dis < max_dis:
            max_dis = tmp_dis
            index = cloud.index(point)
    return cloud[index]

cloud = [[0,0],[0,2],[0,4],[2,0],[4,0]]
eps = 0.02
query_point = [4,3]
precision = 1.e-10
Rmax = ssd.euclidean(cloud[2],cloud[4])   #i drew a graph and checked which points have the maximum distance
smallest_r, approx_solution = binary_search_eps_NNS(eps,Rmax,query_point,cloud,precision)
print("solution of reduction of eps-NNS on (eps,r)-PLEB:",approx_solution)
exact_solution = bruteforce(query_point,cloud)
print("solution of NNS:",exact_solution)
print("Compare exact with approximation:",ssd.euclidean(query_point,exact_solution),ssd.euclidean(query_point,approx_solution)*(1+eps))
