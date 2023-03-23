# Install
Si tenes Windows, que haces? Instalate Linux.

Cuando ya tengas linux segui estos pasos:

### Python 3
Aca es donde instalamos todas las dependencias o cosas que nuestro programa va a necesitar para poder correr.
La primera dependencia y mas importante va a ser Python3 que ya viene instalado en Linux.

Ahora vamos a instalar pip, pip es nuestra formma de bajarnos las bibliotecas de Python que vamos a necesitas. Pueden pensarlo como 
pip = supermercado.
``` bash
sudo apt install python3-pip
``` 

Una vez instalado Python3 vamos a crear un Virtual Enviroment asi:

``` bash
sudo apt install python3-venv
``` 

### que es un virtual enviroment?
Es un tupper en donde va a vivir nuestro projecto y todo lo que tenga que ver con dependencias de python de nuestro projecto. 
Por que lo metemos en un tupper? Porque las diferentes dependencias de python son como salsas y hay dias que uno quiere salsa rosa, otros pesto, otros salsa blanca y nunca queres que las salsas se toquen entre si, por eso las metemos en tuppers.

Asi se crea un virtualenv nativo de python:
``` bash
python3 -m venv NOMBRE_DEL_TUPPER
```

y asi se abre el tupper y se entra adentro:
``` bash
source NOMBRE_DEL_TUPPER/bin/activate
```

Una vez adentro del tupper, vamos a ejecutar este comando que lee el archivo requirements.txt en donde van a estar ya preparadas las salsas que necesitamos. Entonces le voy a pasar a mi supermecado la lista de salsas que quiero tener:
``` bash
pip install -r requirements.txt
```

Listo! Tenemos todo lo necesario instalado.

# Tutorial!

Primero que nada para poder correr un bot de telegram, vamos a necesitar tener un bot creado en telegram en si.

1. Abrir Telegram y hablarle a @BotFather
2. Ahi sigan las instruciones que les da bot father y lo importante es que una vez creado el bot les va a devolver un Token. Copienlo, lo vamos a necesitar.

Ahora vamos a it al archivo config.py y vamos a poner donde dice TOKEN el token que nos dio el bot father.

y Listo!

``` bash
python3 bot.py
```