# Functions
def sumOf(a=0, b=20):
    '''Add two numbers together.

    Both numbers need to be strings.
    '''
    return a+b

sumOf(150, 15)

f = sumOf
f()
f(10,20)

# Default arguments values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye','yes'):
            return True
        if ok in ('n', 'no', 'nope'):
            return False
        retries = retries - 1
        if retries <0:
            raise ValueError('invalid user response')
        print(reminder)


# The default values are evaluated at the point of function definition
i=5

def f(arg=i):
    print(arg)

i=6
f()
f(i)

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# Keyword Arguments
def func(first="1", second="2", third="3"):
    print(first+second+third)

func()
func(first="7", third="8") 


# Formal parmeters
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")        
