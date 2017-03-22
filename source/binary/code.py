from collections import namedtuple
from struct import *

"""Module d'exemple pour les types bytes, memoryview et struct."""


# Bytes-------------------------------------------------------------------------------

msg = bytes('exemple', encoding='utf-8')
# o� mais l'encodage par d�faut sera utilis�.
msg = b"exemple"

b'exemple'

msg[0]

# Cast string en bytes.
my_str = "exemple"
bytes = str.encode(my_str)

# Cast bytes en string.
my_decoded_str = str.decode(bytes)
type(my_decoded_str)  # ensure it is string representation

i = 16

# Cr�e 1 byte avec un int 16.
# Attention � utiliser le bon encodage (little ou big endian).
# v�rifiez avec sys.byteorder.
single_byte = i.to_bytes(1, byteorder='big', signed=True)
print(single_byte)

# Cr�e un bytes avec une liste dev int (0-255).
bytes_from_list = bytes([255, 254, 253, 252])

# Cr�e un byte avec un int en base 2.
one_byte = int('11110000', 2)
print(one_byte)

# Print out binary string (e.g. 0b010010).
print(bin(22))

# Bytes � Integer.
# Cr�e un int avec un bytes (non sign� par d�faut).
i = int.from_bytes(some_bytes, byteorder='big')

# Cr�e un int sign�.
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

# Cr�e un bytearray � partir d'un objet bytes.
msg = bytearray(b"exemple")
# Cr�e un  bytearray � partir d'une chaine de caract�res.
msg = bytearray("exemple", "utf-8")
# Cr�e un  bytearray � partir d'une liste d'entiers entre 0 et 255.
msg = bytearray([94, 91, 101, 125, 111, 35, 120, 101, 115, 101, 200])

msg[0]

# Cast bytes � bytearray.
mutable_bytes = bytearray(b'\x00\x0F')

# Cast bytearray � bytes.
immutable_bytes = bytes(mutable_bytes)


# MemoryView-----------------------------------------------------------------------

# Cr�e une memoryview � partir de l'objet qui d�finit le nouveau buffer.
PyObject * PyMemoryView_FromObject(PyObject * obj)

# Cr�e une memoryview et wrappe le buffer en structure view.
# La memoryview d�tient le buffer qui sera d�sallou� automatiquement
# lors de la destruction de l'objet.
PyObject * PyMemoryView_FromBuffer(Py_buffer * view)

# Cr�e une memoryview d'une partie m�moire contigu�.
# Si dans la m�moire l'objet est stock� de mani�re contigu�,
# le pointeur pointe sur cette zone m�moire
# sinon une copie est faite.
PyObject * PyMemoryView_GetContiguous
(PyObject * obj, int buffertype, char order)

# Retourne true si l'objet obj est une memoryview.
int PyMemoryView_Check(PyObject * obj)

# Retourne un pointer sur buffer wrapper par l'objet donn�.
Py_buffer * PyMemoryView_GET_BUFFER(PyObject * obj)

# mybuf = ...  un grand buffer de bytes.
mv_mybuf = memoryview(mybuf)  # une memoryview de mybuf.
func(mv_mybuf[:len(mv_mybuf)//2])
# passe la premi�re moiti� de mybuf dans func comme une "sous-view"
# cr�e par le d�coupage de la memoryview.
# Aucune copie n'est faite ici!

buf = bytearray(b'abcdefgh')
mv = memoryview(buf)
mv[4:6] = b'ZA'
buf
bytearray(b'abcdZAgh')


# Struct----------------------------------------------------------------------------

# Cr�e une memoryview � partir de l'objet qui d�finit le nouveau buffer.
PyObject * PyMemoryView_FromObject(PyObject * obj)

# Cr�e une memoryview et wrappe le buffer en structure view.
# La memoryview d�tient le buffer et il sera d�sallou� automatiquement
# lors de la destruction de l'objet.
PyObject * PyMemoryView_FromBuffer(Py_buffer * view)

# Cr�e une memoryview d'une partie m�moire contigu�.
# Si dans la m�moire l'objet est stock� de mani�re contigu�,
# le pointeur pointe sur cette.
# zone m�moire sinon une copie est faite.
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
