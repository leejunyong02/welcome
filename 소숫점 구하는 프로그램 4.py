l = [i for i in range(2, 50)]

a = 2

c = 0

b = l[c]

d = 2


def sosu(a, c, d):
    
    while a <= 50:
    
        if l[c] == a:
            a += d
        
        elif l.count(a) == 0:
            a += d
            
        elif l.count(a) == 1:
            l.remove(a)
            a += d
        else:
             a += 1
             d += 1
             c += 1
    return l

while a < 50:
    print(sosu(a, c, d))
   
    

print(l)
