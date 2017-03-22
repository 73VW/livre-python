﻿"""Module d'exemple pour les types bytes, memoryview et struct."""


from collections import namedtuple
from struct import *


# Bytes-------------------------------------------------------------------------------

msg = bytes('exemple', encoding='utf-8')
# On peut aussi affecter une chaine directement
# mais l'encodage par défaut sera utilisé.
msg = b"exemple$"

b'exemple'

msg[0]

# Cast string en bytes.
my_str = "exemple"
bytes = str.encode(my_str)

# Cast bytes en string.
my_decoded_str = str.decode(bytes)
type(my_decoded_str)  # vérifie que le type est string

i = 16

# Crée 1 byte avec un int 16.
# Attention à utiliser le bon encodage (little ou big endian).
# vérifiez avec sys.byteorder.
single_byte = i.to_bytes(1, byteorder='big', signed=True)
print(single_byte)

# Crée un bytes avec une liste de int (0-255).
# sortie: b'\xff\xfe\xfd\xfc.
bytes_from_list = bytes([255, 254, 253, 252])

# Print out binary string (e.g. 0b010010).
print(bin(22))

# Bytes à Integer.
# Crée un int avec un bytes (non signé par défaut).
i = int.from_bytes('12', byteorder='big')

# Crée un int signé.
i = int.from_bytes(b'\x00\x0F', byteorder='big', signed=True)

# Utilise une liste d'entiers comme source pour le cast.
i = int.from_bytes([255, 0, 0, 0], byteorder='big')

with open("test_file.dat", "rb") as binary_file:
    # Lit tout le fichier.
    data = binary_file.read()
print(data)


# Lit N bytes depuis une certaine position.
binary_file.seek(0)
couple_bytes = binary_file.read(2)
print(couple_bytes)


# BytesArray--------------------------------------------------------------------

# Crée un bytearray à partir d'un objet bytes.
msg = bytearray(b"exemple")
# Crée un  bytearray à partir d'une chaine de caractères.
msg = bytearray("exemple", "utf-8")
# Crée un  bytearray à partir d'une liste d'entiers entre 0 et 255.
msg = bytearray([94, 91, 101, 125, 111, 35, 120, 101, 115, 101, 200])

# hexadécimal.
0xff  #sortie 255.
# binaire.
0b100  #sortie 4.

# autres possibilitées.
"{:x}".format(int.from_bytes("exemple".encode("utf-8"), byteorder="big"))                                     
# sortie '6578656d706c65'.

# 65 est la lettre 'e' en hexadécimal.
f"{ord('e'):x}"  # sortie '65'.

msg[0]

# Cast bytes à bytearray.
mutable_bytes = bytearray(b'\x00\x0F')

# Cast bytearray à bytes.
immutable_bytes = bytes(mutable_bytes)


# MemoryView-----------------------------------------------------------------------

# Crée une memoryview à partir de l'objet qui définit le nouveau buffer.
PyObject * PyMemoryView_FromObject(PyObject * obj)

# retourne les données comme string de bytes.
# sortie: b'abc'.
mv = memoryview(b"abc")
mv.tobytes()

# retourne les données en hexadécimale.
# sortie: '616263'.
mv = memoryview(b"abc")
mv.hex()

# retourne les données en une lsite d'élements.
# sortie: [97, 98, 99].
memoryview(b'abc').tolist()

# relacher le buffer.
mv.release()

# mybuf = ...  un grand buffer de bytes.
mv_mybuf = memoryview(mybuf)  # une memoryview de mybuf.
func(mv_mybuf[:len(mv_mybuf)//2])
# passe la première moitié de mybuf dans func comme une "sous-view"
# créé par le découpage de la memoryview.
# Aucune copie n'est faite ici!

buf = bytearray(b'abcdefgh')
mv = memoryview(buf)
mv[4:6] = b'ZA'
buf
bytearray(b'abcdZAgh')


# Struct----------------------------------------------------------------------------

# Crée une memoryview à partir de l'objet qui définit le nouveau buffer.
PyObject * PyMemoryView_FromObject(PyObject * obj)

# Crée une memoryview et wrappe le buffer en structure de view.
# La memoryview détient le buffer et il sera désalloué automatiquement
# lors de la destruction de l'objet.
PyObject * PyMemoryView_FromBuffer(Py_buffer * view)

# Crée une memoryview d'une partie mémoire contiguë.
# Si dans la mémoire l'objet est stocké de manière contiguë,
# le pointeur pointe sur cette.
# zone mémoire sinon une copie est faite.
PyObject * PyMemoryView_GetContiguous
(PyObject * obj, int buffertype, char order)

# packing et unpacking de trois entiers.

pack('hhl', 1, 2, 3)
# sortie : '\x00\x01\x00\x02\x00\x00\x00\x03'
unpack('hhl', '\x00\x01\x00\x02\x00\x00\x00\x03')
# sortie : (1, 2, 3)

# On peut assigner des noms aux champs.
record = 'raymond   \x32\x12\x08\x01\x08'
name, serialnum, school, gradelevel = unpack('<10sHHb', record)

Student = namedtuple('Student', 'name serialnum school gradelevel')
Student._make(unpack('<10sHHb', record))
Student(name='raymond   ', serialnum=4658, school=264, gradelevel=8)
