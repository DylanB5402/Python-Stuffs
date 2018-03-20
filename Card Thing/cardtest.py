import random
def taco():
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    x = 1
    repeat1 = False
    repeat2 = False
    repeat3 = False
    repeat4 = False
    repeat5 = False

    while a + b + c != 15 and d + e + f != 15 and g + h + i != 15 and a + d + g != 15 and b + e + h != 15 and c + f + i != 15 and a + e +i != 15 and c + e + g != 15: 
        while a+ e + i != 15 or repeat1 == True:
            repeat1 = False
            e = random.randint(1,9)
            y = 15 - e
            if y > 9:
                y=9
            a= random.randint(1,y)
            x=15-(a+e) + 1
            i= random.randint(1,x)
            if a == e or e == i or i == a:
                repeat1 = True
            print(a, e, i)
        print('phase1 done')
        while c + e + g != 15 or repeat2 == True:
            repeat2 = False
            y = 15 - e
            if y > 9:
                y=9
            c = random.randint(1,y)
            x=15-(c+e) + 1
            g= random.randint(1,x)
            if c in {a, e, i, g} or e in {a, c, i, g} or g in {a, c, i, e} or 9 < (a or b or c or d or e or f or g or h or i):
                repeat2 = True
        print('phase2 done')
        while (b + e + h != 15 and a + b + c != 15) or repeat3 == True:
            repeat3 = False
            y = 15 - e
            if y > 9:
                y=9
            b = random.randint(1,y)
            x=15-(b+e) + 1
            h= random.randint(1,x)
            if b in {a, c, e, g, h, i} or h in {a, c, e, g, b, i}:
                repeat3 = True
        print('phase3 done')
        while g + h + i != 15 or repeat4 == True:
            g = random.randint(1, h)
            x=15-(g+e) + 1
            h= random.randint(1,x)
            if g in {a, c, e, b, h, i} or i in {a, c, e, g, h, b}:
                repeat4 = True
            print(g, h, i)
        print('phase4 done')        
        while d + e + d != 15 or repeat5 == False:
            g = random.randint(1, h)
            x=15-(c+e) + 1
            h= random.randint(1,x)
            
    print('final', a, b, c)
    print('final',d, e, f)
    print('final',g, h, i)