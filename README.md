# pypdfy
Pypdfy is a python package in coninuous development that provides a set of tools to extract metadata from PDF files

Docs:
Very easy to use, first import pypdfy

```python
from pypdfy import Pypdfy
```

Then use the method ```is_image('path_to_pdf')```
the return value is a Boolean.

For exended usage you can use ```are_images(array_of_paths)```
and pypdfy will take care of the rest. The return will be an array of Booleans.

You can also return the statistics of that array in ````are_images()````
likewise -> 
```python
results = pypdfy.are_images('array_of_paths', statistics=True)
```
This will return ->
```python
{
    'results': 'array_of_boleans',
    'satistics': ('%_of_not_images_pdfs', 'viceversa')
} 
```