# Semana 3, Sesión 2: Validación de Requerimientos y Modelado del Dominio

> Objetivo de la sesión: validar los requerimientos documentados frente a un stakeholder simulado, y construir un modelo de dominio que represente las entidades, relaciones y reglas de negocio del sistema propio.

**Lectura previa de esta sesión:** [Anemic Domain Model vs. Rich Domain Model (Medium)](https://medium.com/@inzuael/anemic-domain-model-vs-rich-domain-model-78752b46098f)

**Referencia de esta sesión:** [What is Class Diagram? (Visual Paradigm)](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-class-diagram/)

Esta sesión no tiene código. Seguimos con el sistema de reservas de canchas deportivas: hoy construimos su modelo de dominio a partir de los casos de uso de la sesión anterior, usando la misma notación simplificada de la Semana 2 Sesión 1 (rectángulo con nombre, atributos y métodos; flecha "tiene un" para composición, "es un" para herencia).

## Sobre la lectura previa

Según el artículo, ¿qué se pierde exactamente cuando la lógica de una regla de negocio vive fuera de la clase a la que pertenece, en vez de dentro de ella?

Se pierde la encapsulación del comportamiento y la capacidad del objeto de poder garantizar sea válido por sí mismo. Es decir, cualquier código externo puede modifiar el estado interno del modelo de dominio y no existen funciones que validen que el objeto sea válido.

## Ejercicio 1: la misma regla, anémica y rica
Antes de que yo lo resuelva: la clase `Reserva` necesita saber si se solapa con otra reserva de la misma cancha. En un modelo anémico, ¿dónde viviría esa lógica si no dentro de `Reserva`?

En un servicio o clase aparte que lee los atributos de Reserva uno por uno.

## Ejercicio 2: agregar la regla de prioridad
Antes de que yo lo resuelva: ¿qué necesita saber la clase `EquipoOficial` para poder decidir, ella misma, si tiene prioridad a una hora dada?

Necesita saber el horario de prioridad, es decir, en qupe horas se puede realizar la reserva con rpioridad y la hora en la que se quiere realizar esta reserva para ver si concuerda con las reglas de reserva oficial. 

## Ejercicio 3: modelo de dominio completo y validación
### Parte A: construir el modelo

Construye el modelo de dominio completo del sistema, con la notación de la Semana 2 Sesión 1. Como mínimo necesitas las entidades `Cancha`, `Reserva`, `Estudiante` y `EquipoOficial`, con sus relaciones. Encapsula estas dos reglas de negocio como métodos de la clase que corresponda, no como comentarios sueltos:

- Un equipo oficial tiene prioridad automática antes de las 6pm.
- Una reserva cancelada con menos de 2 horas de anticipación se registra como no-show, no como cancelación regular.

### Parte B: validar con tu pareja

Intercambia tu modelo con tu pareja. Quien recibe el modelo hace de administrador del gimnasio (el mismo rol de la Sesión 2) y le hace al autor al menos 2 preguntas de esta lista, además de cualquier otra que se le ocurra:

- ¿Qué pasa si dos equipos oficiales piden la misma cancha, el mismo horario, antes de las 6pm?
- ¿El modelo distingue quién hizo la reserva (un estudiante o un equipo oficial), o los trata igual en todos los casos?
- Si le agrego una cancha nueva mañana, ¿qué parte del modelo tengo que tocar?

Ajusta tu modelo con lo que salga de esas preguntas.

### Checklist final

- [ ] Los actores de tus 3 casos de uso de la Sesión 1 (Estudiante, Capitán de equipo oficial) aparecen como entidades o roles en el modelo.
- [ ] La regla de prioridad está encapsulada como método, no como comentario.
- [ ] La regla de no-show está encapsulada como método.
- [ ] Ninguna entidad quedó con atributos únicamente cuando en realidad debía encapsular una regla de negocio propia.

## Antes de la próxima sesión

Pregunta: en tu modelo de dominio, ¿qué clase concentra más reglas de negocio? Si tuvieras que dibujar cómo un caso de uso completo recorre esa clase paso a paso, ¿por dónde empezarías?
