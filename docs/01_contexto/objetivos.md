# 2. Objetivos del proyecto

## 2.1. Objetivo general

Diseñar y desarrollar un sistema robótico asistencial basado en TurtleBot 4, capaz de integrar navegación autónoma, percepción del entorno e interacción persona-robot para ofrecer actividades adaptables de estimulación cognitiva y comunicación dirigidas a niños con Trastorno del Espectro Autista (TEA), como herramienta complementaria en contextos educativos y de rehabilitación.

## 2.2. Objetivos específicos

Para alcanzar el objetivo general, se establecen los siguientes objetivos específicos:

1. **Analizar las necesidades y el contexto de aplicación:** estudiar las características de los entornos de intervención y las posibilidades de la robótica social y asistencial como herramienta complementaria de apoyo a niños con TEA.

2. **Estudiar las plataformas robóticas existentes:** analizar diferentes robots sociales, asistenciales y móviles utilizados en investigación, identificando sus capacidades de percepción, movilidad e interacción.

3. **Diseñar una arquitectura robótica modular:** definir una arquitectura basada en ROS 2 que permita integrar los módulos de navegación, percepción, interacción y gestión de actividades.

4. **Implementar capacidades de movilidad autónoma:** utilizar las funcionalidades de navegación de TurtleBot 4 para desplazarse por un entorno interior, aproximarse de forma controlada a una persona y evitar obstáculos.

5. **Incorporar mecanismos de percepción:** utilizar los sensores disponibles para obtener información del entorno y detectar la presencia de personas, sin realizar identificación biométrica ni inferir características personales.

6. **Diseñar mecanismos de interacción persona-robot:** establecer una comunicación accesible mediante mensajes verbales, apoyos visuales y opciones de respuesta adaptadas.

7. **Diseñar actividades de estimulación cognitiva:** desarrollar una propuesta de actividades organizadas en módulos de memoria, atención, secuenciación, clasificación, razonamiento, comunicación y autonomía.

8. **Desarrollar un sistema de gestión de actividades:** implementar una lógica de control que permita seleccionar actividades, gestionar sus etapas, proporcionar ayudas y adaptar determinados parámetros de dificultad.

9. **Definir mecanismos de seguridad y adaptación:** establecer medidas para controlar el movimiento del robot, regular los estímulos, respetar la participación voluntaria y permitir la interrupción de las actividades.

10. **Implementar una demostración funcional:** desarrollar una misión representativa que integre diferentes capacidades del sistema sobre TurtleBot 4 y permita comprobar su funcionamiento.

11. **Evaluar el funcionamiento de la propuesta:** definir pruebas e indicadores para valorar la navegación, la interacción, la ejecución de las actividades y la respuesta del sistema ante diferentes situaciones.

## 2.3. Resultados esperados

Como resultado del proyecto se espera obtener:

- Una propuesta de diseño de un robot móvil asistencial orientado al acompañamiento y la estimulación cognitiva.
- Una arquitectura modular basada en ROS 2 que permita integrar las diferentes funcionalidades.
- Una colección estructurada de actividades cognitivas y comunicativas.
- Una máquina de estados que coordine el funcionamiento general del robot.
- Una demostración funcional sobre TurtleBot 4 que integre una misión completa.
- Una documentación técnica que describa el diseño, la implementación y las pruebas realizadas.

## 2.4. Relación entre objetivos y demostración

No todos los objetivos específicos tendrán que materializarse en la demostración práctica. Algunos se abordarán mediante el diseño conceptual y la documentación, mientras que otros se implementarán y validarán directamente sobre TurtleBot 4.

La demostración se centrará en comprobar la integración de las capacidades fundamentales de movilidad, percepción, interacción y ejecución de una actividad, dejando abierta la posibilidad de ampliar el sistema con nuevos módulos en desarrollos posteriores.
