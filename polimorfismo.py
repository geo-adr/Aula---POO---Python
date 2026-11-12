class Animal:
    # Permite que objetos diferentes respondam à mesma chamada
    #  de método de maneiras distintas e específicas para cada classe. 
    def emitir_som(self):
        print("O animal que faz um som")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

class Vaca(Animal):
    def emitir_som(self):
        print("Muuu!")

animais = [ Cachorro(), Gato(), Vaca()]
for animal in animais:
    animal.emitir_som()