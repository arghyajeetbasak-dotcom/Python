class Fibonacci:
    def fib(self,n):
        if(n==0 or n==1):
            return n
        return self.fib(n-1)+self.fib(n-2)
    def display(self,n:int) -> int:
        return self.fib(n)
obj=Fibonacci()
print(obj.fib(6))