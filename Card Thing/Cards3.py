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
    x = 0
    repeat_all = False
    repeat1 = False
    repeat2 = False
    repeat3 = False
    repeat4 = False
    repeat5 = False
    loops = 0
    next1 = True
    next2 = True
    next3 = True
    next4 = True
    #while a + b + c != 15 and d + e + f != 15 and g + h + i != 15 and a + d + g != 15 and b + e + h != 15 and c + f + i != 15 and a + e +i != 15 and c + e + g != 15: 
    #while (a+ e + i != 15 and c + e + g != 15 and b + e + h != 15 and a + b + c != 15) or repeat_all == True:
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
            if d in {a, e, i, g} or e in {a, c, i, g} or f in {a, c, i, e} or 9 < (a or b or c or d or e or f or g or h or i):
                repeat2 = True
            print('phase2 done', d, e,  f)
            
        while a + e + i != 15 or repeat3 == True:
            loops = loops + 1
            repeat_all = False
            repeat3 = False
            y = 15 - e
            if y > 9:
                y=9
            a = random.randint(1,y)
            i=15-(a+e)
            '''if i > 9 or i <= 0:
               repeat3 = True
            if a > 9:
                repeat_all = True
                next3 = False'''
            if a in {a, c, e, g, h, i} or i in {a, c, e, g, b, i}:
                repeat3 = True
            if (a in {a, c, e, g, h, i} or i in {a, c, e, g, b, i}) and a + e +i != 15:
                repeat_all = True
            '''if loops > 9:
                #repeat_all = True
                next3 = False'''
            print('phase3 done', a, e, i)
        if a + e + i == 15:       
            next3 = True
        if next3 == True:            
            while c + e + g != 15 or repeat4 == True:
                repeat_all = False
                repeat4 = False
                y = 15 - e
                if y > 9:
                    y=9
                c = random.randint(1,y)
                g=15-(c+e)
                if g > 9 or g <= 0:
                    repeat4 = True
                if c > 9:
                    repeat_all = True
                if c in {a, b, c, e, f, g, h, i} or g in {a, b, c, d, e, g, h, i}:
                    x = x + 1
                    if x > 9:
                        repeat_all = True
                    print('taco', x)
                    repeat4 = True
        #while a + b + c != 15 or repeat5 == True:
        #    repeat_all = True
    print('final', a, b, c)
    print('final',d, e, f)
    print('final',g, h, i)
    print('------------------')


    