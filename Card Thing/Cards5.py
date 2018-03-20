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
    repeat4 = False 
    counter4 = 0
    
    def gen_beh():
        repeat1 = False
        b = 0
        e = 0
        h = 0
        while b + e + h != 15 or repeat1 == True:
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
        return b, e, h
    b, e, h = gen_beh()  
       
    def gen_def():
        d = 0
        e = 0
        f = 0
        repeat2 = False
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
        return d, e, f
    def gen_aei():
        repeat3 = False
        a = 0
        e = 0
        i = 0
        counter3 = 0
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
        return a, e, i
    '''while a + b + c != 15 or repeat4 == True:
        counter4 += 1
        repeat4 = False
        c = 15 - (a + b)'''
    gen_def()
    gen_aei()
    print('final', a, b, c)
    print('final',d, e, f)
    print('final',g, h, i)
    print('------------------')


