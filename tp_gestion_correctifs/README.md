# Implémentation du processus de gestion des correctifs

## Préparation et durcissement du système d'exploitation

### Préparation de la politique de gestion des correctifs


Système | Nombre | Niveau de criticité (1 à 4) | Délais d'application des correcttifs | Planning d'application des correctifs
---:|:---:|:---:|:---:|:---:
Serveur Windows PDC Active Directory, DHCP, DNS | 1 | 4 | 1 semaine | 
Serveur Windows d'impression | 1 | 1 | 1 mois | 
Serveur Windows WEB (site internet de l'organisme) | 1 | 1 | 1 semaine | 
Serveur Windows de fichiers (utilisé par le bureau d'étude) | 1 | 2 | 1 semaine | 
Poste de travail Windows de la DSI | 3 | 4 | 1 jour | 
Poste de travail Windows de la prod| 8 | 4 | 1 jour | 
Poste de travail Windows du bureau d'étude | 10 | 2 | 2 semaines | 
Poste de travail Windows des ressources humaines | 1 | 1 | 2 semaines | 
Poste de travail Windows de la direction | 2 | 2 | 1 semaine | 
Poste de travail Windows de la comptabilité | 1 | 1 | 2 semaines | 

## Installation du rôle WSUS