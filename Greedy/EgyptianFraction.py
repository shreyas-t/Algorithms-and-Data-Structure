import math

def egyptianFraction(nr, dr):

    if nr == 0 or dr == 0:
        return
    
    if dr%nr == 0:
        print("1/{0}".format(int(dr/nr)),end ='')
        return
    
    if nr%dr == 0:
        print("Not a fraction")
        return

    #Handling the condition nr > dr
    if(nr>dr):
        print("{} + ".format(math.floor(nr/dr)),end ='')
        egyptianFraction(nr%dr, dr)
        return
    

    n = math.ceil(dr/nr)

    print("1/{} + ".format(n),end ='')
    egyptianFraction(n*nr-dr, n*dr)

egyptianFraction(14, 6) 