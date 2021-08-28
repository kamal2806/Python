def main():
    kitten('meow','grrr','purrr')
    kittens(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

def kitten(*args):
    if len(args):
        for s in args:
            print(s,end=' ')
        print()
    else:
        print('Meow')


def kittens(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k,kwargs[k]))
    else:
        print('Meow')

if __name__ == '__main__' : main()