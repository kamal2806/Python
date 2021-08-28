import platform

def function(n):
    print(n)

function(47)


def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))

if __name__ == '__main__' : main()

def isPrime(n):
    if n<=1 :
        return False
    for x in range(2,n):
        if n%x == 0:
            return False
    else:
        return True

num = int(input("Enter number : "))

if isPrime(num):
    print(f'{num} is Prime')
else:
    print(f'{num} is not prime')
