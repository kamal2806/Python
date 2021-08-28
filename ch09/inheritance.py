class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs : self._type = kwargs['type'] 
        if 'name' in kwargs : self._name = kwargs['name']
        if 'sound' in kwargs : self._sound = kwargs['sound'] 
    
    def type(self,t=None):
        if t : self._type = t 
        try : return self._type 
        except AttributeError : return None 

    def name(self,t=None):
        if t : self._name = t
        try : return self._name
        except AttributeError : return None 

    def sound(self,t=None):
        if t : self._sound = t 
        try : return self._sound 
        except AttributeError : return None 
    
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

class Duck(Animal):
    def __init__(self,**kwargs):
        self._type = 'duck'
        if 'type' in kwargs:del kwargs['type']
        super().__init__(**kwargs)

class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs:del kwargs['type']
        super().__init__(**kwargs)  # super to call the parent class

    def kill(self,s):
        print(f'The {self.name()} will kill all {s}!!!')

def print_animal(o):
    if not isinstance(o,Animal):
        raise TypeError('print_animal() : requires an Animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}"')

def main():
    a0 = Kitten(name = 'fluffy', sound='rwar')
    a1 = Duck(name = 'donald', sound = 'quack')
    print_animal(a0)
    print_animal(a1)
    a0.kill('humans')

if __name__ == '__main__' : main()
