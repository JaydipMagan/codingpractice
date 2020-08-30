import collections,math
class DSU:
    # Disjoint-set data structure
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr
        
class Solution:
    def primes_set(self,n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        dsu = DSU(n)
        
        primes = collections.defaultdict(list)
        
        for i, num in enumerate(A):
            ps = self.primes_set(num)
            for p in ps: primes[p].append(i)
                
        for _, indexes_list in primes.items():
            for i in range(len(indexes_list)-1):
                dsu.union(indexes_list[i],indexes_list[i+1])
                
        return max(collections.Counter(dsu.find(i) for i in range(n)).values())
            