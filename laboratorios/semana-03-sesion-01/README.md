# Semana 3, Sesión 1: Casos de Uso

> Objetivo de la sesión: documentar un caso de uso completo (actor, precondiciones, flujo principal, flujos alternos) a partir de los requerimientos elicitados, evitando los errores más comunes de redacción.

**Lectura previa de esta sesión:** [7 Mistakes Even the Best Make When Writing Use Cases (Bridging the Gap)](https://www.bridging-the-gap.com/7-use-case-writing-mistakes/)

**Referencia de esta sesión:** [What is Use Case Diagram? (Visual Paradigm)](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-use-case-diagram/)

Esta sesión no tiene código. Seguimos con el sistema de reservas de canchas deportivas que empezamos a levantar en la Sesión 2: hoy documentamos sus casos de uso a partir de esos requerimientos.

## Sobre la lectura previa

De los 7 errores que menciona el artículo, ¿cuál te parece el más difícil de detectar en tu propio caso de uso, no en el de otra persona?

_(tu respuesta)_

## El caso de hoy: dos versiones del mismo caso de uso

**Versión 1:**

```
Caso de uso: Reservar una cancha

Actor: Usuario

Flujo:
1. El usuario abre la app y ve la pantalla principal con el menú hamburguesa
   arriba a la izquierda.
2. Hace clic en el botón verde "Reservar".
3. El sistema muestra un calendario desplegable con las canchas disponibles
   en color azul.
4. El usuario selecciona una fecha y hora, y presiona el botón "Confirmar"
   que aparece en la esquina inferior derecha.
5. El sistema guarda la reserva en la base de datos y muestra un mensaje
   de éxito en un recuadro verde.
```

**Versión 2:**

```
Caso de uso: Reservar una cancha

Actor: Estudiante

Precondiciones: el estudiante tiene una cuenta activa y ha iniciado sesión.

Flujo principal:
1. El estudiante selecciona una cancha, una fecha y un horario disponible.
2. El sistema verifica que el horario elegido está disponible para esa cancha.
3. El sistema registra la reserva a nombre del estudiante.
4. El sistema confirma la reserva al estudiante.

Flujos alternos:
3a. El horario ya está reservado por otro estudiante: el sistema rechaza la
solicitud y le muestra al estudiante los horarios disponibles más cercanos.
3b. El estudiante intenta reservar la misma cancha y el mismo horario dos
veces en el mismo día: el sistema rechaza la segunda solicitud.
```

¿Qué está mal en la Versión 1, más allá de los colores de los botones?

El diagrama especifica detalles de la interfa, lo que puede generar confusion, ya que en un diagrama de casos de uso no es drecomendable incluir detalles técnicos, además, no especifica el rol del cliente. "Usuario" es muy vago y no dice nada acerca de lo que el cliente puede hacer en el sistema. Por último, no declara el estado inicial del sistema ni los flujos alternos que podrían ocurrir para completar el cuadro. 

## Ejercicio 1: identificar los errores y reescribir
Antes de que yo revise cada línea de la Versión 1: lista, paso por paso, qué le sobra o le falta comparada con la Versión 2.

_(tu respuesta)_

## Ejercicio 2: un caso de uso nuevo
Antes de que yo lo escriba: ¿qué debería pasar si un estudiante intenta cancelar una reserva faltando menos de 2 horas para el inicio? Escribe tu propia hipótesis de flujo alterno.

3c. El Estudiange intenta cancelar la reserva con menos de 2 horas de anticipación: El sistema registra esa cancelación bajo la categoría de "no-show."

## Ejercicio 3: caso de uso de prioridad
En la Sesión 2 levantamos un requerimiento que todavía no se ha convertido en caso de uso: los equipos oficiales de la universidad pueden reservar con prioridad automática antes de las 6pm.

Documenta el caso de uso completo "Reservar con prioridad de equipo oficial", con esta plantilla:

```
Caso de uso: Reservar con prioridad de equipo oficial

Actor: El estudiante.

Precondiciones: el estudiante tiene una cuenta activa identificada por el sistema como perteneciente a un equipo oficial de la universidad y ha iniciado sesión.

Flujo principal:
Flujo principal:
1. El estudiante selecciona una cancha, una fecha y un horario disponible.
2. El sistema verifica que el horario elegido está disponible para esa cancha y que la reserva se esté realizando antes de las 6pm.
3. El sistema registra la reserva a nombre del estudiante.
4. El sistema confirma la reserva al estudiante.

Flujos alternos:
3a. La cancha y hora han sido reservados por otro estudiante: El sistema toma la reserva del equipo especial como prioridad y cancela la reserva del estudiante anterior por esta.
3b. El estudiante intenta reservar la misma cancha y el mismo horario dos
veces en el mismo día: el sistema rechaza la segunda solicitud.

Necesitas al menos 2 flujos alternos. Uno de ellos debe cubrir qué pasa si un estudiante individual ya había reservado ese horario antes de las 6pm, y ahora un equipo oficial pide el mismo horario con prioridad.

Antes de dar por terminado el caso de uso, revisa: ¿algún paso de tu flujo principal describe un color, una posición de botón, o cualquier otro detalle de interfaz? Si sí, bórralo y describe solo la lógica de negocio.

## Antes de la próxima sesión

Pregunta: en el caso de uso que acabas de escribir, ¿qué entidades (sustantivos, no acciones) tuviste que nombrar para poder describir el flujo? Esa lista es el punto de partida de la próxima sesión.
