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

## Tecnologías utilizadas para la contrucción
<p align="left">
<img src="https://github.com/sebastiannarvaez23/event-anywhere/assets/88569352/d96abd89-7804-4fa5-816c-5ea41e8100ab" width="100" />
<img src="https://static-00.iconduck.com/assets.00/git-icon-1024x1024-pqp7u4hl.png" width="auto" height="90">
<img src="https://user-images.githubusercontent.com/88569352/218375255-d9a28190-10e2-44ad-b13d-721292e46815.png" width="90">
<img src="https://github.com/sebastiannarvaez23/window-quote-machine/assets/88569352/30b6bdc0-3bf9-4c6d-a3af-8b43ed9e27f3" width="95">
<img src="https://github.com/sebastiannarvaez23/window-quote-machine/assets/88569352/8be2479b-f1da-4d44-a379-a2050d40ec5e" width="auto" height="80">
</p>

## Navegación por las interfaces
#### Pagina principal sin usuario autenticado
<br />
<img src="https://github.com/sebastiannarvaez23/window-quote-machine/assets/88569352/09d85ead-7822-453b-aece-ed7795a32311" width="60%" height="auto">
<br />

#### Pagina principal con usuario autenticado
<br />
<img src="https://github.com/sebastiannarvaez23/window-quote-machine/assets/88569352/8e57f355-821e-4b3a-88ed-dd9e147b1b59" width="60%" height="auto">
<br />


#### Login para autenticar usuarios
<br />
<img src="https://github.com/sebastiannarvaez23/window-quote-machine/assets/88569352/df282b00-8e69-4cae-8cb4-f2356724d0f5" width="60%" height="auto">
<br />
