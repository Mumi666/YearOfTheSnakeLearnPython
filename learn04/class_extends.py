class A:
    def __init__(self):
        print('init A')

class B(A):
    def __init__(self):
        A.__init__(self)
        print('init B')

class C(A):
    def __init__(self):
        A.__init__(self)
        print('init C')

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print('init D')

d = D()
# a b a c d