# OC-QL-P12 / Epic_Even

***

## 1.Presentation
***
Développement d'une architecture back-end sécurisé avec Django ORM


## 2-Installation  :
***
Se diriger sur le repertoire où l'on souhaite installer l'application.

Pour installer le programme via un terminal :  

Sous Windows :  
```sh
$ git clone https://github.com/quentin8469/OC-QL-P12.git    
$ python3 -m venv env  
$ venv/scripts/activate  
$ pip3 install -r requirements.txt   
```
Sous linux/Mac :      
```sh
$ git clone https://github.com/quentin8469/OC-QL-P12.git   
$ python3 -m venv env    
$ source env/bin/activate    
$ pip3 install -r requirements.txt    
```


**Lancement du serveur Django** :

* Se rendre dans le repertoire contenant le fichier python ' manage.py ' ( EpicEvents_CRM )
* Puis exécuter python manage.py runserver
* La page sera accessible à l'URL suivante:  http://127.0.0.1:8000/admin/


## 3-Fonctionnement:
***

* Se referer à la documentation POSTMAN pour efectuer les tests.
* lien: https://documenter.getpostman.com/view/16984358/UVCB9Pg5



***
Créer un rapport flake8 :  

`flake8 --exclude=env,venv --format=html --htmldir=flake8_report --max-line-lengt=119`
