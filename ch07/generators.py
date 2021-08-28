def main():
    for i in inclusive_range(25):
        print(i, end=' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0 
    step = 1

    if numargs < 1 :
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        end = args[0]
    elif numargs == 2:
        (start,end) = args
    elif numargs == 3:
        (start,end,step) = args
    else :
        raise TypeError(f'expected atmost 3 arguments, got {numargs}')
    
    
    i = start
    while i<=end:
        yield i
        i += step

if __name__ == '__main__' : main()