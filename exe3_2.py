def exe3(szoveg):
    x = '*'
    max = -1
    for m in szoveg:
        if len(m) > max:
            max = len(m)
    print((max+4)*x)
    for k in szoveg:
        k += (max-len(k))*' '
        print("{0} {1} {2}".format(x,k,x))
    print((max+4)*x)


szov = input("Szöveg:")
m=szov.split()
exe3(m)