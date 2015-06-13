


def dirf(w):
    xs = dir(w)
    for x in xs:
        if(x[0] != "_"):
            print x
