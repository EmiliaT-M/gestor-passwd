### Gestor
##### Proyecto final
<p>
Dentro del presente se encuentra un proyecto para gestionar contraseñas, el cual, se encarga de guardar el sitio web, usuario y contraseña.
La interacción con el gestor de contraseñas es por linea de comandos.
Tiene como propósito ser una llaveró virtual de usuarios y contaseñas personal, que permita la administración de contraseñas, permitiendo agregar, modificar datos, eliminar y guardar los cambios realizados.
Este programa cuenta con una base de datos no relacional que gestiona los datos ingresados por el usuario, es decir, guarda el nombre del usuario, la fecha
  en que se registro, el sitio y la contraseña cifrada del usuario.
</p>

------------
#### Para ejecutar el proyecto es necesario
- Python 3.10.x o version actual
- SQLite3 
- Librería Cryptography

#### Instalación de herramientas
##### Linux
sudo apt update -- Actualizar sistema

- sudo apt install python3 python3-pip  ----Instalarla  python y pip 
- pip install cryptography ----- Libreria de cifrado
- sudo apt install sqlite3 -----Intslatacion libreria de sqlite

##### Windows
- Usar sitio oficial de python o si cuentas con choco:
choco install python

- pip install cryptography   ---- Libreria de cifrado

- verificar que exista sqlite3:
python -c "import sqlite3; print(sqlite3.sqlite_version)"


##### Mac
- brew install python  ---Instalacion de python
- pip3 install cryptography ---- Libreria de cifrado
- brew install sqlite   ---Intslatacion libreria de sqlite

-------------
### Ejecucion
Para poder ejecutar es necesario posicionarse en la clase main.py 

Se mostrara un menu de acciones en el cual se puede interactuar con el programa; en el programa se pueden agregar, modificar, eliminar y guardar los nuevos datos que se agreguen.
> **Nota: Si no guardas los cambios hechos no se guardará nada, para ello sugiero salir y guardar cambios.**
