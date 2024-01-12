import numpy as np
nombre=np.empty([4, 3], dtype=np.dtype('U100'))
print(nombre[:])
nom=input("")
nombre[2][2]=nom
print(nombre[:])
print(len(nombre[:]))