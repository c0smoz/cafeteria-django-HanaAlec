# cafeteria-django-HanaAlec

## Pour relancer un projet 

Pour activer l'env + lancer VSCode
```
student@D261-PC5-Ubuntu24:~/cafeteria-django-HanaAlec$ source venv/bin/activate
(venv) student@D261-PC5-Ubuntu24:~/cafeteria-django-HanaAlec$ code .
```

![alt text](img/restart_project.png)

## Ebauche d'organigramme (sur dbdiagramme.io)

```
Table Student {
  id int [pk]
  name varchar
  email varchar
  credit float
  shop_history list [ref: > Product.name]
}

Table Group {
  id int [pk]
  student_id int [ref: > Student.id]
  service varchar
}

Table Product {
  id int [pk]
  name varchar
  price float
  available boolean
}

Table Transaction {
  id int [pk]
  student_id int [ref: > Student.id]
  product_id int [ref: > Product.id]
  date datetime
}
```
