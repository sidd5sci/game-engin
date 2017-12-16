


def f1(func,**args):
    func(**args)

def f2(a,b):
    print a,' | ',b

    
f1(f2,a=6,b=7)
