import re
class Solution:
        # try:
        #     x = float(s)
        #     return True
        # except:
        #     return False
        without_space = s.strip(" ")
        if without_space=="":
            return False
        pattern = re.compile(r"^([\s]*[+-]?(([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)|([0-9]+))[\s]*)$|^([\s]*[+-]?(([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)|([0-9]+))e[+-]?[0-9]+[\s]*)$")
        return pattern.search(without_space)

"""
1
+1
-1


1.11
+11.1
-1.1
.1


1e9
1e-9
1e+9

1.1e9
+1.1e9
-1.1e9
46.e3

.1e9
.1e-9


1 
1.1
.1212
3.
+.8

^([\s]*[+-]?(([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)|([0-9]+))[\s]*)$|^([\s]*[+-]?(([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)|([0-9]+))e[+-]?[0-9]+[\s]*)$


[\s]*[+-]? this will match spaces and symbols at the start of the number ? means 0 or 1 only 
([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)|([0-9]+) number starting like 1. 1.1 .1 123, padded with space or not
e[+-]?[0-9]+ matches numbers like e9 e+9 e-9    
---
abc
a1
1e
--6
-+1
96a34e
1.1e9e9
1.1.1
.
.0e


"""