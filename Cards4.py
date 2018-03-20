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
    repeat_all = False
    repeat1 = False
    repeat2 = False
    repeat3 = False
    repeat4 = False
    repeat5 = False
    counter3 = 0
    counter4 = 0
    while (a+ e + i != 15 and c + e + g != 15 and b + e + h != 15 and a + b + c != 15) or repeat_all == True:
        while b+ e + h != 15 or repeat1 == True:
                repeat1 = False
                e = e + 1
                y = 15 - e
                if y > 9:
                    y=9
                b= random.randint(1,y)
                h=15-(b+e)
                if h > 9 or h <= 0:
                    repeat1 = True                
                if b == e or e == h or h == b:
                    repeat1 = True
                print('phase 1 done' ,b, e, h)
        while d + e + f != 15 or repeat2 == True:
                repeat2 = False
                y = 15 - e
                if y > 9:
                    y=9
                d = random.randint(1,y)
                f=15-(d+e)
                if f <= 0 or f > 9:
                    repeat2 = True
                if d in {a, b, c, f, e, g, h, i} or e in {a, b, c, d, f, g, h, i} or f in {a, b, c, d, e, g, h, i}:
                    repeat2 = True
                print('phase2 done', d, e,  f)
                
        while a + e + i != 15 or repeat3 == True:
                counter3 += 1
                repeat3 = False
                y = 15 - e
                if y > 9:
                    y=9
                a = random.randint(1,y)
                i=15-(a+e)
                if i > 9:
                    repeat3 = True
                if a in { b, c, d, e, g, h, i} or i in {a, b, c, e, d, g, b}:
                    repeat3 = True
                if counter3 > 9:
                    break
                print('phase3 done', a, e, i, counter3)
        while a + b + c != 15 or repeat4 == True:
            counter4 += 1
            repeat4 = False
            c = 15 - (a + b)
            if c in { b, c, d, e, f, g, h, i}:
                repeat4 = True
            if c > 9 or c <= 0:
                break
            if counter4 > 9:
                break
            print('phase4 done', a, b, c) 
    print('final', a, b, c)
    print('final',d, e, f)
    print('final',g, h, i)
    print('------------------')