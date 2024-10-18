def decifrar(p, x, modulo):

    binario= format(p, "b")

    w=1
    
    for Y in binario:
        w= w*w
        
        if Y == "1":
            w= w*x 
            

    rta= w % modulo
    return rta

print(decifrar(3149,5869,8051))