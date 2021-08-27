class Stack:# creamos la clase stack
    def _init_(self):
        self.items=[] 
    def is_empty(self):
        return self.items==[]
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        return self.items.pop(0)
    def print_stack(self):
        print(self.items)
pila = Stack()

pila.push('a')
pila.push('b')
pila.push('c')

pila.print_stack()

pila.pop()
pila.print_stack()