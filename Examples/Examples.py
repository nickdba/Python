# Hello World
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")

# If-Else Conditions
x = int (input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to 0')
elif x==0:
    print('Zero')
elif x==1:
    print('Single')
else:
    print('Multiple')

# For loop that modify sequence 
ph = 'Nick doesn\'t hate cats'
words = ph.split(' ')
for w in words[:]:
    print(w, len(w))
    if len(w) > 4:
        words.insert(0,w)


# For Range function
for i in range(9,15):
    print(i)
a=['Mary','had','a','little','lamb!']
for i in range(len(a)):
    print(i,a[i])

# Finding prime numbers until 100
print('Prime numbers:')
for n in range(2, 100):
    for i in range(2,n):
        if (n%i ==0):
            #print(n,' is divisible by ', i)
            break
    # Else condition that catches all non break cases    
    else:
        print(n, end=' ')

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