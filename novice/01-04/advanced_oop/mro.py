class A: 
    def abc(self): 
        print(" In class A") 

class B(A): 
    def abc(self): 
        print(" In class B") 

class C(A): 
    def abc(self): 
        print("In class C") 
  
# classes ordering 
class D(B, C): 
    pass
     
r = D() 
r.abc() 
