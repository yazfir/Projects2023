Jupyter QtConsole 5.4.2
Python 3.11.4 | packaged by Anaconda, Inc. | (main, Jul  5 2023, 13:38:37) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.0 -- An enhanced Interactive Python. Type '?' for help.

import re

nombre = 'MARGARITO LOPEZ'

telefono = '55565811'

oracion = 'mi casa nueva'

re?

nombre
Out[6]: 'MARGARITO LOPEZ'

re.search('A', nombre)
Out[7]: <re.Match object; span=(1, 2), match='A'>

if re.search('A',nombre):
    print('Tiene A')
else:
    print('No hay')
    
Tiene A

if re.search('[0-9'], telefono)
  Cell In[9], line 1
    if re.search('[0-9'], telefono)
                       ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('


if re.search('[0-9]', telefono)
  Cell In[10], line 1
    if re.search('[0-9]', telefono)
                                   ^
SyntaxError: expected ':'


re.search('[0-9]', telefono)
Out[11]: <re.Match object; span=(0, 1), match='5'>

re.findall('5', telefono)
Out[12]: ['5', '5', '5', '5']

oracion
Out[13]: 'mi casa nueva'

re.finall('casa',oracion)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[14], line 1
----> 1 re.finall('casa',oracion)

AttributeError: module 're' has no attribute 'finall'

re.findall('casa',oracion)
Out[15]: ['casa']
