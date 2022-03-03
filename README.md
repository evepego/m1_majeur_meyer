# m1_majeur_meyer
TP Audit de code PHP

## Recherche des points d'entrées de l'application :
 
> **En règle générale, quels sont les points d'entrée vers le code d'une application web ?**  
Les points d'entrée principaux d'une application web sont dans le fichier `fichier.xml` et dans les requêtes pour transmettre des paramètres à l'application web (`GET`, `POST`, `REQUEST`, etc.)  
**Nom de l'étape :** `Ground Zero`

### Script
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

### Sortie

```bash
eve@Evux:~/m1_majeur_meyer$ python3 script1.py 
./wp-mobile-detector/default-widgets.php
./wp-mobile-detector/resize.php
./wp-mobile-detector/functions.php
./wp-mobile-detector/websitez-wp-mobile-detector.php
./wp-mobile-detector/timthumb.php
./wp-mobile-detector/admin/home.php
./wp-mobile-detector/admin/themes.php
./wp-mobile-detector/admin/upgrade.php
./wp-mobile-detector/admin/admin-page.php
./wp-mobile-detector/js/sharing.php
./wp-mobile-detector/themes/amanda-mobile/index.php
./wp-mobile-detector/themes/amanda-mobile/footer.php
./wp-mobile-detector/themes/amanda-mobile/comments.php
./wp-mobile-detector/themes/amanda-mobile/404.php
./wp-mobile-detector/themes/amanda-mobile/single.php
./wp-mobile-detector/themes/amanda-mobile/header.php
./wp-mobile-detector/themes/amanda-mobile/archive.php
./wp-mobile-detector/themes/amanda-mobile/page.php
./wp-mobile-detector/themes/amanda-mobile/sidebar-right_home.php
./wp-mobile-detector/themes/amanda-mobile/functions.php
./wp-mobile-detector/themes/amanda-mobile/style.php
./wp-mobile-detector/themes/jester-mobile/index.php
./wp-mobile-detector/themes/jester-mobile/footer.php
./wp-mobile-detector/themes/jester-mobile/category.php
./wp-mobile-detector/themes/jester-mobile/comments.php
./wp-mobile-detector/themes/jester-mobile/404.php
./wp-mobile-detector/themes/jester-mobile/single.php
./wp-mobile-detector/themes/jester-mobile/header.php
./wp-mobile-detector/themes/jester-mobile/archive.php
./wp-mobile-detector/themes/jester-mobile/page.php
./wp-mobile-detector/themes/jester-mobile/search.php
./wp-mobile-detector/themes/jester-mobile/functions.php
./wp-mobile-detector/themes/jester-mobile/sidebar.php
./wp-mobile-detector/themes/jester-mobile/searchform.php
./wp-mobile-detector/themes/viper-mobile/index.php
./wp-mobile-detector/themes/viper-mobile/footer.php
./wp-mobile-detector/themes/viper-mobile/comments.php
./wp-mobile-detector/themes/viper-mobile/404.php
./wp-mobile-detector/themes/viper-mobile/single.php
./wp-mobile-detector/themes/viper-mobile/header.php
./wp-mobile-detector/themes/viper-mobile/archive.php
./wp-mobile-detector/themes/viper-mobile/page.php
./wp-mobile-detector/themes/viper-mobile/search.php
./wp-mobile-detector/themes/viper-mobile/functions.php
./wp-mobile-detector/themes/viper-mobile/sidebar.php
./wp-mobile-detector/themes/viper-mobile/searchform.php
./wp-mobile-detector/themes/casper-mobile/index.php
./wp-mobile-detector/themes/casper-mobile/footer.php
./wp-mobile-detector/themes/casper-mobile/comments.php
./wp-mobile-detector/themes/casper-mobile/404.php
./wp-mobile-detector/themes/casper-mobile/single.php
./wp-mobile-detector/themes/casper-mobile/header.php
./wp-mobile-detector/themes/casper-mobile/archive.php
./wp-mobile-detector/themes/casper-mobile/page.php
./wp-mobile-detector/themes/casper-mobile/search.php
./wp-mobile-detector/themes/casper-mobile/functions.php
./wp-mobile-detector/themes/casper-mobile/sidebar.php
./wp-mobile-detector/themes/casper-mobile/searchform.php
./wp-mobile-detector/themes/bluesteel-mobile/index.php
./wp-mobile-detector/themes/bluesteel-mobile/footer.php
./wp-mobile-detector/themes/bluesteel-mobile/category.php
./wp-mobile-detector/themes/bluesteel-mobile/comments.php
./wp-mobile-detector/themes/bluesteel-mobile/404.php
./wp-mobile-detector/themes/bluesteel-mobile/single.php
./wp-mobile-detector/themes/bluesteel-mobile/header.php
./wp-mobile-detector/themes/bluesteel-mobile/archive.php
./wp-mobile-detector/themes/bluesteel-mobile/page.php
./wp-mobile-detector/themes/bluesteel-mobile/search.php
./wp-mobile-detector/themes/bluesteel-mobile/functions.php
./wp-mobile-detector/themes/bluesteel-mobile/sidebar.php
./wp-mobile-detector/themes/bluesteel-mobile/searchform.php
./wp-mobile-detector/themes/colbalt-mobile/index.php
./wp-mobile-detector/themes/colbalt-mobile/footer.php
./wp-mobile-detector/themes/colbalt-mobile/comments.php
./wp-mobile-detector/themes/colbalt-mobile/404.php
./wp-mobile-detector/themes/colbalt-mobile/single.php
./wp-mobile-detector/themes/colbalt-mobile/header.php
./wp-mobile-detector/themes/colbalt-mobile/archive.php
./wp-mobile-detector/themes/colbalt-mobile/page.php
./wp-mobile-detector/themes/colbalt-mobile/search.php
./wp-mobile-detector/themes/colbalt-mobile/functions.php
./wp-mobile-detector/themes/colbalt-mobile/sidebar.php
./wp-mobile-detector/themes/colbalt-mobile/searchform.php
./wp-mobile-detector/themes/wz-mobile/index.php
./wp-mobile-detector/themes/wz-mobile/footer.php
./wp-mobile-detector/themes/wz-mobile/comments.php
./wp-mobile-detector/themes/wz-mobile/404.php
./wp-mobile-detector/themes/wz-mobile/single.php
./wp-mobile-detector/themes/wz-mobile/header.php
./wp-mobile-detector/themes/wz-mobile/archive.php
./wp-mobile-detector/themes/wz-mobile/sidebar-right_single.php
./wp-mobile-detector/themes/wz-mobile/page.php
./wp-mobile-detector/themes/wz-mobile/sidebar-right_home.php
./wp-mobile-detector/themes/wz-mobile/functions.php
./wp-mobile-detector/themes/wz-mobile/style.php
./wp-mobile-detector/themes/wz-mobile/sidebar-left_home.php
./wp-mobile-detector/themes/mojo-mobile/index.php
./wp-mobile-detector/themes/mojo-mobile/footer.php
./wp-mobile-detector/themes/mojo-mobile/comments.php
./wp-mobile-detector/themes/mojo-mobile/404.php
./wp-mobile-detector/themes/mojo-mobile/single.php
./wp-mobile-detector/themes/mojo-mobile/header.php
./wp-mobile-detector/themes/mojo-mobile/archive.php
./wp-mobile-detector/themes/mojo-mobile/page.php
./wp-mobile-detector/themes/mojo-mobile/search.php
./wp-mobile-detector/themes/mojo-mobile/functions.php
./wp-mobile-detector/themes/mojo-mobile/sidebar.php
./wp-mobile-detector/themes/mojo-mobile/searchform.php
./wp-mobile-detector/themes/websitez-mobile/index.php
./wp-mobile-detector/themes/websitez-mobile/footer.php
./wp-mobile-detector/themes/websitez-mobile/category.php
./wp-mobile-detector/themes/websitez-mobile/comments.php
./wp-mobile-detector/themes/websitez-mobile/404.php
./wp-mobile-detector/themes/websitez-mobile/single.php
./wp-mobile-detector/themes/websitez-mobile/header.php
./wp-mobile-detector/themes/websitez-mobile/archive.php
./wp-mobile-detector/themes/websitez-mobile/page.php
./wp-mobile-detector/themes/websitez-mobile/search.php
./wp-mobile-detector/themes/websitez-mobile/functions.php
./wp-mobile-detector/themes/websitez-mobile/sidebar.php
./wp-mobile-detector/themes/websitez-mobile/style.php
./wp-mobile-detector/themes/websitez-mobile/searchform.php
./wp-mobile-detector/themes/corporate-mobile/index.php
./wp-mobile-detector/themes/corporate-mobile/footer.php
./wp-mobile-detector/themes/corporate-mobile/category.php
./wp-mobile-detector/themes/corporate-mobile/comments.php
./wp-mobile-detector/themes/corporate-mobile/404.php
./wp-mobile-detector/themes/corporate-mobile/single.php
./wp-mobile-detector/themes/corporate-mobile/header.php
./wp-mobile-detector/themes/corporate-mobile/archive.php
./wp-mobile-detector/themes/corporate-mobile/page.php
./wp-mobile-detector/themes/corporate-mobile/search.php
./wp-mobile-detector/themes/corporate-mobile/functions.php
./wp-mobile-detector/themes/corporate-mobile/sidebar.php
./wp-mobile-detector/themes/corporate-mobile/style.php
./wp-mobile-detector/themes/corporate-mobile/searchform.php
./wp-mobile-detector/themes/corporate-mobile/twitter.php
./wp-mobile-detector/themes/anakin-mobile/index.php
./wp-mobile-detector/themes/anakin-mobile/footer.php
./wp-mobile-detector/themes/anakin-mobile/comments.php
./wp-mobile-detector/themes/anakin-mobile/404.php
./wp-mobile-detector/themes/anakin-mobile/single.php
./wp-mobile-detector/themes/anakin-mobile/header.php
./wp-mobile-detector/themes/anakin-mobile/archive.php
./wp-mobile-detector/themes/anakin-mobile/page.php
./wp-mobile-detector/themes/anakin-mobile/search.php
./wp-mobile-detector/themes/anakin-mobile/functions.php
./wp-mobile-detector/themes/anakin-mobile/sidebar.php
./wp-mobile-detector/themes/anakin-mobile/searchform.php
./wp-mobile-detector/themes/amanda-mobile/partials/header-home.php
./wp-mobile-detector/themes/wz-mobile/partials/header-single.php
./wp-mobile-detector/themes/wz-mobile/partials/header-home.php
(defaultdict(<class 'int'>, {'$_REQUEST': 8, '$_GET': 31, '$_POST': 15}), 54)
```
