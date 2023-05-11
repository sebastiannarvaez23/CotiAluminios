# Coti Aluminios
## ¿De qué se trata este aplicativo?
Esta aplicación permite a los usuario con o sin registro realizar las cotizaciones de las ventanas que cada uno de ellos requiere, cumpliendo a detalle con cada uno de los pequeños cambios que generan novedades en el costo, haciendo eficiente para el area comercial la construccion de cotizaciones donde se ven involucradas ventanas muy personalizadas.

## ¿Como hago funcionar el aplicativo?
Instale el entorno virtual de python 3 con `$ python3 -m venv venv`
Active el entorno con el siguiente comando:
Linux: `$ source venv/bin/activate`
windows: `$ venv/Scripts/activate`
Instale las dependencias parandose en la ruta raiz del proyecto WMSServices/ y ejecutando el comando `$ pip install -r requiriments.txt`.

Para nuestro caso y para efectos practicos, dejé en la raiz del proyecto una base de datos SQLite3, la cual está conectada al proyecto como también contiene datos ya creados para lograr hacer ver la aplicación más usable.

Luego de haber realizado los pasos anteriores, debe ejecutar el comando `$ python manage.py runserver`, de este modo se levanta un servidor de desarrollo el cual está configurado para usarse en la ruta: `http://localhost:8000/`

## ¿Cómo logro correr los tests?
En el codigo fuente del aplicativo se construyeron unas pruebas unitarias utilizando el modulo de testing integrado en el framework django. Estas funciones automatizan las pruebas de la creacion de usuarios y la obtención de la cotización. Para correr las pruebas debe detener el servidor (Si realizó los pasos anteriores y aún sigue corriendo) con el comando `cntrl + c`, posteriormente ejecute el comando `$ python manage.py test` y logrará ver todos los tests en ejecución.

# Manual de Usuario
