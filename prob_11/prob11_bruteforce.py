#!/usr/bin/env python
#
# The is the brute force attempt at problem 11.
#
# Total number of checks for NxN array with a sequence of k neighboring
#  elements:
# - Horizontal and Vertical
#    N^2(N-(k-1))
# - Diagonals:
#    2[N-(k-1) + 2 sum_{i=k, N-1}(i - (k-1))]
#
import csv, random
import numpy as np

# function to retrieve k x k subarray of a given the upper-left corner index
def get_subarray(a,i,j,k):
    return a[i:i+k][:,j:j+k]

# function to retrieve the all the lists to check for max
def get_lists(array):
    fin = []
    #get horizontals
    fin += [list(array[i]) for i in range(0,len(array))]
    #get verticals
    fin += [list(array[:][:,i]) for i in range(0,len(array))]
    # get diagonal
    fin.append(list(array.diagonal()))
    # get anti-diagonal
    fin.append(list(array[:,::-1].diagonal()))
    return fin

#function to return max product of elements in list
def get_max(lists):
    prods = [np.array(temp).prod() for temp in lists]
    maximum = np.amax(prods)
    values = lists[prods.index(maximum)]
    return values, maximum

if __name__ == '__main__':
    #Some constants
    N = 20
    seq = 4
    
    #first import array
    filename = "array.tsv"
    tsv_file = csv.reader(open(filename, 'rb'), delimiter='\t')
    temp_a = [int(ele) for row in tsv_file for ele in row]
    array = np.array([temp_a[i:i+N] for i in range(0, len(temp_a), N)])
    
    # code to generate new random array
    #temp_array = [random.randint(0,100) for i in N for j in N]
    #array = np.array([new_array[i:i+N] for i in range(0, len(temp_array), N)])
    
    curr_max = 0
    indx = []
    array_values = []
    
    for i in range(0,N-seq):
        for j in range(0,N-seq):
            values, maximum = get_max(get_lists(get_subarray(array,i,j,seq)))
            if maximum > curr_max:
                curr_max = maximum
                indx = [i,j]
                array_values = values
    
    print "max: "+str(curr_max)
    print "values: "+str(array_values)
    print "upper index: "+str(indx)
