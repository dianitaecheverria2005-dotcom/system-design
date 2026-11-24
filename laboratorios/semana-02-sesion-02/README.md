# Semana 2, Sesión 2: Elicitación de Requerimientos

> Objetivo de la sesión: aplicar al menos dos técnicas de elicitación (entrevista, taller) para levantar requerimientos de un sistema propuesto, y distinguir un requerimiento verificable de uno ambiguo.

**Lectura previa de esta sesión:** [Overcoming the Top 5 Challenges in Requirements Elicitation (Medium)](https://medium.com/@tom_80522/overcoming-the-top-5-challenges-in-requirements-elicitation-a03bf6ac6557)

**Referencia de esta sesión:** [Requirements Elicitation: A Survey of Techniques, Approaches, and Tools (Zowghi & Coulin)](https://eecs481.org/readings/requirements.pdf)

Esta sesión no tiene código. El laboratorio es este documento: lo llenas durante la clase y lo entregas como está al final.

## Respuesta sobre la lectura

De los 5 retos que menciona el artículo, ¿cuál te parece el más fácil de subestimar si nunca has levantado requerimientos antes? Una frase basta.

El mas facil de subestimar en mi opinión es la ambiguedad o falta de información. AL principio del proyecto se puede creer que se tienen claros los objetivos del stakeholder, pero al avanzar es muy fácil llegar a conclusiones erróneas o confundir lo que realmente se quería decir con algún requerimiento si no se implementan las herramientas de visualización y prototipado correctamente. 

## El caso de hoy: una entrevista mal conducida

```
Analista: Entonces, ¿usted quiere una app rápida y fácil de usar, verdad?
Cliente: Sí, algo así.
Analista: Perfecto, ¿le parece bien si usamos un login con Google?
Cliente: Eh, supongo que si es lo más común...
Analista: Genial. ¿Y el sistema debe soportar muchos usuarios al mismo tiempo?
Cliente: Sí, bastantes.
Analista: Entendido, entonces lo diseñamos para alta escala. ¿Algo más?
Cliente: Bueno, en realidad lo que más me preocupa es que mi equipo de soporte
pueda ver el historial de cada cliente rápido, porque ahora se demoran
mucho buscando en tres sistemas distintos...
Analista: Ah, sí, eso lo resolvemos con la base de datos. ¿Cerramos aquí?
Cliente: Ok...
```

## Ejercicio 1: qué salió mal
Antes de que yo revise cada intercambio: marca, línea por línea, cuáles preguntas del Analista te parecen problemáticas y por qué.

El analista empezó con preguntas cerradas la entrevista, mientras que debió haber empezado preguntando los problemas que tenía el cliente con la aplicación en ese momento y partir desde allí con preguntas que validen los requerimientos verificables: "¿Qupe tan rápida debe ser esta aplicación? Por ejemplo, no debe demorar más de dos segundos." Además, debió proponer diferentes formas del inicio de sesión para verificar que el cliente esté satisfecho con un login con google y no quiera cambiar este requerimiento más adelante. 

## Ejercicio 2: de ambiguo a verificable
Antes de que yo lo resuelva: toma el requerimiento "el sistema debe soportar muchos usuarios al mismo tiempo" (extraído de la transcripción) y anota qué información falta para que alguien pueda comprobar, después de construido el sistema, si ese requerimiento se cumplió o no.

El analista acept+o un requerimiento ambiguo cuando el cliente solo describió la palabra "bastantes." Debió haber preguntado un n+umero aproxic¿mado que el stakeholder consideraría muchos usuarios, para que así, al programar la aplicación, se realice es testeo de ella con el número que el cliente propuso y verificar que se cumplió. Además, debió preguntar en qué momento del día es que los usuarios ingresan más al sistema y que debería suceder con este si se super este número.

## Ejercicio 3: elicitación simulada en parejas

Formen una pareja. Uno toma el rol de **Cliente**, el otro el de **Analista**. El sistema a levantar es un sistema de reservas de canchas deportivas para los polideportivos de la universidad.

Hay dos versiones del Cliente, Brief A y Brief B. Tu profesor les asigna a ti y a tu pareja cuál de las dos usar. Los dos briefs describen el mismo sistema y llevan a los mismos requerimientos, pero el cliente de cada uno tiene una personalidad distinta, así que la pareja de al lado no va a escuchar la misma conversación que ustedes.

**Si eres el Cliente:** lee, antes de empezar, solo el brief que tu profesor te asignó (Brief A o Brief B). No leas el otro. Revela esa información solo si tu Analista te la pregunta directamente, y respeta la personalidad del brief que te tocó. No te adelantes a contarla toda de una vez, esa es justo la parte del ejercicio.

**Si eres el Analista:** no leas ningún brief todavía. Conduce la entrevista aplicando lo que vimos en los Ejercicios 1 y 2: evita preguntas cerradas que ya sugieren la respuesta, profundiza cuando una respuesta sea vaga, y usa una segunda técnica además de la entrevista abierta (por ejemplo, una serie de preguntas de seguimiento tipo taller sobre un punto que quedó ambiguo) para llegar a un requerimiento verificable. Si tu Cliente responde con monosílabos, eso es parte del ejercicio: vas a necesitar preguntas más específicas, no solo abiertas.

### Brief A: cliente colaborador pero disperso (solo para quien tiene el rol de Cliente)

Eres el administrador de los polideportivos de la universidad. Tu petición inicial, lo único que dices sin que te pregunten, es: "necesito un sistema donde los estudiantes reserven canchas online, que sea fácil de usar."

Te gusta hablar, y sueles mezclar información importante con detalles que no vienen al caso (el clima, una anécdota del semestre pasado). Tu Analista tiene que separar lo relevante de lo que no lo es.

Información que solo revelas si te la preguntan directamente, no la ofrezcas por iniciativa propia:

- Actualmente usas una hoja de cálculo compartida, y cada semana hay al menos 2 reservas dobles para la misma cancha y hora.
- Los equipos oficiales de la universidad (baloncesto, vóley) necesitan poder reservar con prioridad automática antes de las 6pm, sin competir con reservas de estudiantes individuales.
- Las reservas se pueden cancelar hasta 2 horas antes; después de eso, quieres que quede registrado como "no-show", porque estás evaluando cobrar una multa en el futuro, aunque todavía no.
- No te importa el diseño visual. "Fácil de usar" en realidad significa que un estudiante de primer semestre lo entienda sin ayuda; no tienes una definición más precisa que esa hasta que te pregunten qué significa "fácil".

### Brief B: cliente lacónico (solo para quien tiene el rol de Cliente)

Eres la administradora de otro complejo deportivo de la universidad. Tu petición inicial, lo único que dices sin que te pregunten, es: "quiero un sistema de reservas de canchas."

Contestas en frases cortas y no ofreces contexto ni ejemplos por iniciativa propia. Si tu Analista te hace una pregunta abierta o vaga ("cuénteme más sobre eso"), respondes "sí" o "depende" y esperas a que pregunte algo más específico.

Información que solo revelas si te la preguntan de forma directa y puntual, ni ante una pregunta vaga ni por iniciativa propia:

- Usas una hoja de cálculo compartida. Cada semana hay reservas dobles, mínimo 2, para la misma cancha y horario.
- Los equipos oficiales (baloncesto, vóley) tienen prioridad para reservar antes de las 6pm, sobre cualquier estudiante individual.
- Cancelar con menos de 2 horas de anticipación cuenta como no-show, no como cancelación regular. Estás pensando en una multa a futuro, no todavía.
- "Fácil de usar" quiere decir que un estudiante de primer semestre lo entienda solo, sin que nadie le explique.

### Documentación de requerimientos

Completa esta tabla con lo que levantaste en la entrevista. Necesitas al menos 5 requerimientos, y al menos 2 deben pasar de ambiguos a verificables.

| # | Requerimiento tal como lo dijo el Cliente | ¿Verificable o ambiguo? | Si es ambiguo, reescritura verificable |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

Técnicas de elicitación que usaste (marca las que aplicaste):

- [ ] Entrevista abierta
- [ ] Preguntas de seguimiento tipo taller sobre un punto ambiguo
- [ ] Otra: _____________

## Antes de la próxima sesión

Pregunta: si dos requerimientos parecen contradecirse (por ejemplo, "prioridad automática para equipos" vs "cualquier estudiante puede reservar libremente"), ¿de dónde sacas la regla para decidir cuál gana?
