import random
def gen_beh():
    b=0
    e=0
    h=0
    global_z = 27
    repeat1= False
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
    return b, e, h
    
def wich(c):
    d = 4 + c
    return d
def taco():
    b, e, h = gen_beh()
    print(b, e, h, gen_beh.global_z)