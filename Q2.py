count=0

str = 'affhvcdadcds101e1'
#initialize a dictionary
d = {}
for x in str:
    if x in d:
        d[x]+=1
    else:
        d[x] = 1   

print(d)         
    
