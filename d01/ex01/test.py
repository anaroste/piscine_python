from game import *

gc = GotCharacter()
print(gc.first_name, gc.is_alive, '\n')

gc2 = GotCharacter('Arya', True)
print(gc2.first_name, gc2.is_alive, '\n')

print(gc2.__doc__, '\n')

arya = Stark("Arya")
print(arya.__doc__, '\n')

print(arya.family_name, arya.house_words, arya.first_name, arya.is_alive, '\n')

arya.die()

print(arya.is_alive, '\n')

sansa = Stark('Sansa')

print(sansa.first_name, sansa.family_name, sansa.is_alive)