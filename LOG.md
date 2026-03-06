# LOG.md

## Daily Scrum - 01/03/26

### Equipo completo (Product Owner, Scrum Master, T.L y Developers)

- Qué hicimos hoy:
  Nos reunimos para planificar la distribución del trabajo. Realizamos una autoevaluación del nivel de conocimientos de cada integrante con el fin de asignar los archivos según su nivel de complejidad.

- Qué haremos mañana:
  Iniciar la implementación de la lógica base en `inicio.py` para establecer las variables principales del juego y permitir la integración posterior con los demás módulos.

- Bloqueos:
  No se presentaron bloqueos.


---

## Daily Scrum - 02/03/26

### Deyanis y Laimen (inicio.py)

- Qué hicimos hoy:
  Definimos las variables iniciales del juego. Implementamos la validación de dificultad y la asignación de recursos según el nivel elegido. También solicitamos al usuario el nombre y la dificultad mediante `input`.

- Qué haremos mañana:
  Integrar la lógica de consumo y estado dentro del bucle principal del juego.

- Bloqueos:
  No se presentaron bloqueos.


### Melissa (motor.py)

- Qué hice hoy:
  Creé el archivo `motor.py` e inicié la importación del módulo `inicio.py` para acceder a sus variables y comenzar a estructurar el bucle principal que orquesta el juego.

- Qué haré mañana:
  Apoyar a los demás integrantes en la estructura de sus módulos para facilitar la integración con el motor principal.

- Bloqueos:
  Sí.

- Motivo:
  El código desarrollado se encuentra únicamente en entorno local y no se logró subir a GitHub, lo que dificulta la integración con el equipo.

### Saul (eventos.py)

- Qué hice hoy:
  No se realizaron avances en el módulo asignado debido a que se estaba a la espera de la definición final del flujo principal del juego en `inicio.py` y `motor.py`.

- Qué haré mañana:
  Iniciar la estructuración de la lógica de eventos diarios y definir los posibles escenarios aleatorios.

- Bloqueos:
  Sí.
  Dependencia de la estructura base del motor para garantizar compatibilidad.


### Angela (consumo.py)

- Qué hice hoy:
  No se realizaron avances técnicos. Se revisaron los requerimientos funcionales del módulo de consumo para planificar la implementación.

- Qué haré mañana:
  Implementar la lógica de reducción diaria de recursos según la población definida.

- Bloqueos:
  No.


### Elianis (interfaz.py)

- Qué hice hoy:
  No se registraron avances debido a que el diseño visual depende de la estructura final de salida definida en el motor principal.

- Qué haré mañana:
  Diseñar la estructura base de tablas visuales y pruebas iniciales con formato en consola.

- Bloqueos:
  Sí.
  Dependencia parcial del flujo principal del juego.


### Gustavo (README.md)

- Qué hice hoy:
  Se realizó revisión general del proyecto para comenzar a estructurar la documentación técnica, supervisé los push a la rama dev, para hacer los merges sin generar conflictos.

- Qué haré mañana:
  Redactar la sección inicial del README con descripción del proyecto y objetivos.

- Bloqueos:
  No.


---

## Daily Scrum - 03/03/26

### Deyanis y Laimen (inicio.py)

- Qué hicimos hoy:
  Refactorizamos variables innecesarias, traducimos el código al inglés para mantener coherencia técnica y enviamos los cambios al repositorio.

- Qué haremos mañana:
  Mejorar la documentación interna del código, eliminar comentarios redundantes y simplificar la lógica donde sea posible.

- Bloqueos:
  No se presentaron bloqueos.

### Saul (eventos.py)

- Qué hice hoy:
  Se definió la estructura base del módulo de eventos y se plantearon los posibles tipos de eventos (negativos o sin evento).

- Qué haré mañana:
  Implementar la función de generación aleatoria diaria.

- Bloqueos:
  No.


### Angela (consumo.py)

- Qué hice hoy:
  Se diseñó la lógica base para calcular el consumo diario de recursos en función de la población.

- Qué haré mañana:
  Integrar pruebas iniciales del cálculo con valores simulados.

- Bloqueos:
  No.


### Elianis (interfaz.py)

- Qué hice hoy:
  Se realizaron pruebas iniciales de formato en consola y estructura de presentación de datos, no se logró subir los archivos debido a un problema con git, los cambios quedaron en la maquina local.

- Qué haré mañana:
  Ajustar el diseño visual para mejorar claridad en la presentación de recursos y estado.

- Bloqueos:
  Sí.
  Problema con Git que impidió subir los cambios al repositorio.


### Gustavo (README.md)

- Qué hice hoy:
  Se comenzó la redacción del README incluyendo descripción general del juego y estructura del proyecto.

- Qué haré mañana:
  Agregar sección de instalación y ejecución.

- Bloqueos:
  No.

### Juan (estado.py)

- Qué hice hoy:
  Me integré al equipo de desarrollo y revisé la estructura actual del proyecto para comprender la arquitectura y responsabilidades de cada módulo.

- Qué haré mañana:
  Iniciar la implementación del módulo `estado.py`, definiendo las validaciones principales del juego.

- Bloqueos:
  No.

---

## Daily Scrum - 04/03/26

### Deyanis y Laimen (inicio.py)

- Qué hicimos hoy:
  Se mejoró la estructura del módulo `inicio.py`, simplificando la validación de dificultad y ajustando el tipado de funciones para facilitar su integración con los demás módulos del juego.

- Qué haremos mañana:
  Realizar pruebas de integración con el motor y validar la correcta inicialización de recursos.

- Bloqueos:
  No se presentaron bloqueos.


### Juan (estado.py)

- Qué hice hoy:
  Implementé la función `verify_state`, estableciendo la normalización de recursos negativos y definiendo las condiciones de derrota del jugador.

- Qué haré mañana:
  Integrar la validación de estado dentro del ciclo principal del motor y realizar pruebas de funcionamiento.

- Bloqueos:
  No se presentaron bloqueos.


### Saul (eventos.py)

- Qué hice hoy:
  Implementé la generación de eventos aleatorios y la lógica de aplicación de efectos según la dificultad seleccionada.

- Qué haré mañana:
  Ajustar la interacción entre eventos y el módulo de estado para validar condiciones posteriores a cada evento.

- Bloqueos:
  No se presentaron bloqueos.


### Angela (consumo.py)

- Qué hice hoy:
  Implementé la lógica inicial del cálculo de consumo de recursos en función de la población del jugador.

- Qué haré mañana:
  Integrar el módulo con el motor principal y validar que el consumo se aplique correctamente en cada día del ciclo.

- Bloqueos:
  Sí.
  No fue posible realizar el push al repositorio debido a un problema de autenticación en Git. Los cambios permanecen en entorno local.


### Elianis (interfaz.py)

- Qué hice hoy:
  Implementé la estructura inicial de impresión en consola utilizando `colorama` para mejorar la apariencia visual del juego. Se añadieron condicionales para cambiar el color según la cantidad de recursos disponibles.

- Qué haré mañana:
  Ajustar la presentación visual para integrarla con los datos reales generados por el motor del juego.

- Bloqueos:
  Sí.
  Problema de autenticación en Git que impidió subir los cambios al repositorio.


### Melissa (motor.py)

- Qué hice hoy:
  Avancé en la estructura del ciclo principal del juego, definiendo el bucle de días y preparando la integración con los módulos de eventos, consumo y estado.

- Qué haré mañana:
  Completar la integración entre módulos y validar el flujo completo del juego.

- Bloqueos:
  No se presentaron bloqueos.


### Gustavo (Scrum Master / README)

- Qué hice hoy:
  Realicé revisión técnica de los módulos desarrollados para asegurar coherencia en estructura, tipado y flujo general del proyecto. Supervisé el estado de los commits y apoyé en la resolución de problemas relacionados con Git.

- Qué haré mañana:
  Coordinar la integración de los módulos pendientes y continuar con la documentación del proyecto.

- Bloqueos:
  No.


### Gustavo (Scrum Master / README)

- Qué hice hoy:
  Realicé una revisión de la estructura de ramas del repositorio y consolidé el desarrollo en la rama `dev`, eliminando las ramas `feature/*` ya integradas para simplificar el flujo de trabajo. Se sincronizaron los módulos principales y se verificó la correcta actualización del repositorio remoto.

- Qué haré mañana:
  Coordinar la integración final entre módulos y continuar con la documentación técnica del proyecto.

- Bloqueos:
  No.
 
---

## Daily Scrum - 06/03/26

### Equipo completo (Product Owner, Scrum Master, T.L y Developers)

- Qué hicimos hoy:
  Nos reunimos para comunicar el cómo nos manejariamos con las ramas en el repositorio ahora, puesto que las ramas `feature/*` fueron eliminadas, ahora todos trabajaron bajo la rama dev, modificando nada más su archivo asignado. 

- Qué haremos mañana:
  Presentar un M.V.P de lo que llevamos al cliente al cliente.

- Bloqueos:
  No se presentaron bloqueos.

### Gustavo (Scrum Master / README)

- Qué hice hoy:
  Realicé una revisión de lo que se lleva en el proyecto, inicio.py, eventos.py, consumo.py, interfaz.py, etc. Y empecé a añadir comentarios DOCSTRINGS a cada función

- Qué haré mañana:
  Explicar al equipo, que de ahora en adelante, documentaremos cada función usando DOCSTRINGS, con el formato de pequeña descripción de lo que hace la función, argumentos y returns.

- Bloqueos:
  No.

### Gustavo (Scrum Master / README)

- Qué hice hoy:
  Realicé una revisión en `inicio.py` y hice unas refactorizaciones con respecto al bucle en entry_difficulty, además que ahora `choose_difficulty()` retorna un diccionario con los recursos dependiendo de la dificultad, para facilitar su uso en otros archivos

- Qué haré mañana:
  Presentar el M.V.P al cliente.

- Bloqueos:
  No.

### Gustavo (Scrum Master / README)

- Qué hice hoy:
  Realicé una revisión en `estado.py` para ver como manejaba las condiciones de derrota y realicé un refactor de la función, para usar dicciones en vez de listas, para facilitar la lectura y el mantenimiento del código.

- Qué haré mañana:
  Presentar el M.V.P al cliente.

- Bloqueos:
  No.

### Gustavo (Scrum Master / README)

- Qué hice hoy:
  Realicé una revisión en `eventos.py` para ver como manejaba la generación de eventos y realicé un refactor para usar diccionarios en vez de listas, para facilitar la lectura y el mantenimiento del código. Además, de moficiar varios eventos, debido a una confusión del developer, añadió eventos que no corresponden a nuestra ambientación, como lluvia acida, por lo que tuve que eliminar esos eventos y añadir eventos más acordes a la ambientación del juego.

- Qué haré mañana:
  Presentar el M.V.P al cliente.

- Bloqueos:
  No.