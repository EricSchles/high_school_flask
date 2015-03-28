from functools import wraps
from time import time

class ExampleOne:
    def currency(f):
        @wraps(f)
        def wrapper(self,*args,**kwargs):
            return "$" + str(f(self,*args,**kwargs)[0])
        return wrapper

    def logger(f):
        @wraps(f)
        def wrapper(self,*args,**kwargs):
            start = time()
            result = f(self,args)
            print f.__name__,"ran in:", time() - start
            return result
        return wrapper

    @logger
    @currency
    def dollars(self,amount):
        return amount

    def run_examples(self):
        print self.dollars(5.00)
        print self.dollars(60)

class ExampleTwo:    
    def functor(f):
        @wraps(f)
        def wrapper(self,*args,**kwargs):
		print "First print this out"
		f(self)
		print "Last print this out"
	return wrapper

    @functor
    def func(self):
	print "Hello there"

    def run_examples(self):
        self.func()

example_one = ExampleOne()
example_one.run_examples()
example_two = ExampleTwo()
example_two.run_examples()
