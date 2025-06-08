🎮 Piedra, Papel o Tijera

Clásico juego en el que competis contra la máquina eligiendo una de tres opciones. El primero en derrotar al oponente gana la partida.

El código está contenido en un único archivo PiedraPapelTijera.py, sin dependencias externas más allá de la librería estándar de Python.

📂 Estructura del proyecto
/ (raíz del proyecto)
├── Dockerfile
├── PiedraPapelTijera.py
└── README.md  

📝 Descripción del juego

-Reglas:
--Piedra vence a Tijera.
--Tijera vence a Papel.
--Papel vence a Piedra.

-Flujo del script (PiedraPapelTijera.py):
--Solicita al jugador una opción: piedra, papel o tijera.
--La máquina elige aleatoriamente.
--Se comparan las elecciones y se muestra el resultado: victoria, derrota o empate.
--Pregunta si deseas jugar otra vez; escribe salir para terminar.

🚀 Cómo jugar?
1- Clona el repositorio:
---git clone https://github.com/tu-usuario/piedra-papel-tijera.git
---cd piedra-papel-tijera
2- Construye la imagen Docker:
---docker build -t piedra-papel-tijera .
3- Ejecuta el contenedor y lanza el juego:
---docker run --rm -it piedra-papel-tijera
4- Sigue las instrucciones en pantalla ingresando piedra, papel o tijera. Para salir escribe salir o presiona Ctrl+C.

📥 Requisitos previos

Docker instalado.
Conexión a Internet para descargar la imagen base de Python.

🔗 Enlace al repositorio

https://github.com/tu-usuario/piedra-papel-tijera