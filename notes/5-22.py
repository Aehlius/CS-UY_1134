#dont use temp
#add comments

#list(range(n))
#creates a list of numbers from 0 to n-1


#CREATING A RANGE FUNCTION

def myRange(n):
    count = 0
    while count < n:
        yield count     #Functions with yield are called a generator
        count += 1

#range(n) yields values from 0 to n-1
#generators are usually for looping



#OOP

class Dragon:
    def __init__(self, name):
        self.name = name

    def display(self):
        print('Dragon:', self.name)

    def __str__(self):
        return 'name is ' + self.name


if __name__ == '__main__':
    # puff = Dragon()
    # print(puff.__class__)
    # print(puff.__class__.__name__)
    #
    # puff.name = 'Puff'  #you could add an attribute on the fly
    # print(puff.name)

    puff = Dragon('Puff')
    print(puff.name)
    puff.display()
    print(puff)


'''
Efficiency

def func0(n):
    print(17)
constant O(1)

def func1(n): 

logarithmic O(log n)

def func2(n):
    for i in n:
        print(i)
linear O(n)

def func2.5(n)

linearithmic O(n * log n)

def func3(n):
    for i in n:
        for j in n:
            print(i*j)
quadratic O(n^2)

def func3(

exponential O(2^n)

'''

'''
Linked list - reference to the following value is at every individual value


'''
