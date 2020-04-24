

import collections 


# if x is a contiguous subsequence of all the arrays in y return true
# Assuming it takes O(n)
def subseq(x,y):
    pass
def LLCS(flat):
    
    freq = collections.defaultdict(int)
    n = len(flat)
    for row in flat:
        #make subsequences
        for i in range(0,n):
            for j in range(i,n):
                seq = row[i:j+1]
                if subseq(seq,flat): # check if in all other rows
                    # increment frequency
                    if seq in freq:
                        freq[seq]+=1
                    else:
                        freq[seq]=1
    
    # Find largest sequence with count = n 
    length = 0
    for x in freq.keys():
        if len(x)>length and freq[x]==n:
            length = len(x)
    return length



flat_table = [[0,0,1,1],[0,0,0,1],[0,1,1,1],[2,0,1,0]]
l = LLCS(flat_table)
print(l)