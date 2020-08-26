class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        multiples = {3:2,5:4}
        replace = {3:"Fizz",5:"Buzz"}
        res = []
        for i in range(n):
            buffer = ""
            for num in multiples:
                if multiples[num]==0:
                    buffer+=replace[num]
                    multiples[num]=num
                multiples[num]-=1
            if buffer=="":
                res.append(str(i+1))
            else:
                res.append(buffer)
        return res