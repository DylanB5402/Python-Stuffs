import random
def cards():
    a=0
    b=0
    c=0
    d=0
    e=5
    f=0
    g=0
    h=0
    i=0
    h1=a + b + c
    h2=d + e + f
    h3=g + h + i
    v1 = a + d + g
    v2 = b + e + h
    v3 = c + f + i
    d1 = a + e + i
    d2 = c + e + g
    while h1 != 15 and h2 != 15 and h3 != 15 and v1 != 15 and v2 != 15 and v3 != 15 and d1 != 15 and d2 != 15:
        y = 1
        x = 1
        while d1 != 15 and x != 0:
                a = random.randint(1,9)
                y = 15 - a
                
                x=15-(a+e) + 1
                i= random.randint(1,x)
        while v2 != 15 and x != 0:
                b = random.randint(1,9)
                y = 15 - b
                
                x=15-(b+e)+ 1
                h= random.randint(1,x)
        while d2 != 15 and x != 0:
                c = random.randint(1,9)
                y = 15 - c
                
                x=15-(c+e)
                g= random.randint(1,x)
        while h2 != 15  and x != 0:
                d = random.randint(1,9)
                y = 15 - d
                
                x=15-(d+e)+ 1
                f= random.randint(1,x)
        while h1 != 15  and x != 0:
                a = random.randint(1,9)
                y = 15 - a
                b= random.randint(1,y)
                x=15-(a+b)+ 1
                c= random.randint(1,x)
        while h3 != 15  and x != 0:
                g = random.randint(1,9)
                y = 15 - g
                h= random.randint(1,y)
                x=15-(g+h)+ 1
                i= random.randint(1,x)
        while v1 != 15  and x != 0:
                a = random.randint(1,9)
                y = 15 - a
                d= random.randint(1,y)
                x=15-(a+d)+ 1
                g= random.randint(1,x)
        while v3 != 15  and x != 0:
                c = random.randint(1,9)
                y = 15 - c
                f= random.randint(1,y)
                x=15-(c+f)+ 1
                i= random.randint(1,x)
    print(a, b, c, d, e, f, g, h, i)