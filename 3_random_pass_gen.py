import random
import string
todo=string.ascii_letters+string.digits+string.punctuation
print(todo)
contra=''
for i in range(0,20):
    valor=random.randint(0,len(todo)-1)
    contra+=todo[valor]
print('Tu contraseña es:',contra,'y tiene',len(contra),'caracteres')

#se puede hacer con: password = "".join(random.sample(todo, 20))



