# m1_majeur_meyer
TP Audit de code PHP

## Recherche des points d'entrées de l'application :
 
> **En règle générale, quels sont les points d'entrée vers le code d'une application web ?**  
Les points d'entrée principaux d'une application web sont dans le fichier `fichier.xml` et dans les requêtes pour transmettre des paramètres à l'application web (`GET`, `POST`, `REQUEST`, etc.)  
Nom de l'étape : `Ground Zero`

```python3
from collections import defaultdict
import glob
from itertools import count
from unittest import result

* 
http_requests = ['$_GET', '$_POST', '$_REQUEST']

dir = ['./wp-mobile-detector/*.php', './wp-mobile-detector/*/*.php', './wp-mobile-detector/*/*/*.php', './wp-mobile-detector/*/*/*/*.php', './wp-mobile-detector/*/*/*/*/*.php', './wp-mobile-detector/*/*/*/*/*/*.php']

def occurence1(string_list):
    results =  defaultdict(int)
    count = 0
    for d in dir:
        for file_name in glob.iglob(d):
            print(file_name)
            with open(file_name) as input_file:
                for line in input_file:
                    for s in string_list:
                        if s in line:
                            results[s] += 1
                            count += 1
    return results, count

print(occurence1(http_requests), count)
```

