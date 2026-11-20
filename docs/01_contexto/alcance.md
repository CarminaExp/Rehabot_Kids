# 3. Alcance del proyecto

## 3.1. Alcance general

REHABOT KIDS contempla el diseño de un sistema robótico móvil asistencial orientado al acompañamiento y la estimulación cognitiva de niños con Trastorno del Espectro Autista (TEA). La propuesta se desarrollará tomando como plataforma principal TurtleBot 4 e integrando diferentes capacidades mediante ROS 2.

El alcance comprende tanto el diseño conceptual de un sistema completo como la implementación de una demostración funcional que permita validar una parte representativa de sus capacidades.

El sistema se plantea para su utilización en entornos interiores controlados, como centros de intervención temprana, espacios de rehabilitación pediátrica y aulas de educación especializada. Su funcionamiento estará supervisado por un profesional responsable de configurar y acompañar las sesiones.

## 3.2. Funcionalidades contempladas en el diseño completo

El diseño global de REHABOT KIDS incluirá los siguientes bloques funcionales:

### 3.2.1. Navegación y movilidad autónoma

El robot podrá desplazarse por un entorno interior, evitando obstáculos y siguiendo trayectorias planificadas. Se contempla la posibilidad de desplazarse hasta una ubicación determinada, aproximarse a una persona y regresar a una posición inicial.

### 3.2.2. Percepción del entorno

El sistema utilizará los sensores disponibles en TurtleBot 4 para obtener información del entorno. Entre las capacidades previstas se encuentran la detección de obstáculos, la percepción de elementos próximos y la detección de la presencia de personas.

La percepción estará orientada a facilitar la interacción y la navegación, sin realizar identificación biométrica ni inferir diagnósticos o características personales.

### 3.2.3. Interacción persona-robot

El robot podrá iniciar y mantener interacciones sencillas mediante mensajes de voz, preguntas, respuestas y apoyos visuales. Se contempla la utilización de pictogramas y alternativas de comunicación para facilitar la participación de personas con diferentes necesidades comunicativas.

### 3.2.4. Gestión de actividades cognitivas

El sistema dispondrá de diferentes módulos de actividades:

- Memoria y atención.
- Secuenciación y organización.
- Clasificación y razonamiento.
- Comunicación funcional.
- Comprensión de situaciones sociales y emocionales.
- Autonomía y anticipación mediante rutinas.

Cada módulo podrá incluir diferentes ejercicios y niveles de dificultad, permitiendo adaptar la actividad a las características y preferencias del participante.

### 3.2.5. Adaptación de las sesiones

Se contempla que el sistema pueda ajustar determinados parámetros de las actividades, como su duración, complejidad, cantidad de elementos o nivel de ayuda proporcionado.

También deberá permitir solicitar ayuda, realizar descansos, cambiar de actividad o finalizar la sesión.

### 3.2.6. Supervisión y registro

El diseño incluirá mecanismos para que un profesional pueda supervisar las sesiones y consultar información básica sobre las actividades realizadas, su duración y los resultados obtenidos.

El registro deberá limitarse a los datos necesarios para la finalidad prevista y respetar los principios de privacidad y protección de datos.

## 3.3. Alcance de la demostración funcional

Debido a las limitaciones de tiempo y a la complejidad de desarrollar todas las funcionalidades del sistema, la demostración práctica se centrará en una misión completa que integre los principales componentes de la arquitectura.

La misión propuesta contempla las siguientes etapas:

1. **Estado inicial:** el robot permanece en una posición de espera.
2. **Detección de una persona:** el sistema utiliza la cámara para detectar la presencia de una persona mediante un mecanismo de visión artificial.
3. **Aproximación segura:** el robot se desplaza hacia una posición próxima, manteniendo una distancia controlada y evitando obstáculos.
4. **Inicio de la interacción:** el robot saluda y pregunta si la persona desea realizar una actividad.
5. **Selección de la actividad:** se ofrece una actividad sencilla de estimulación cognitiva.
6. **Ejecución del ejercicio:** el robot presenta una secuencia o tarea de ordenación, recibe las respuestas y proporciona retroalimentación.
7. **Finalización:** el sistema ofrece continuar, descansar o finalizar la interacción.
8. **Registro:** se almacena información básica sobre el desarrollo de la misión para facilitar su evaluación.

La actividad concreta y el mecanismo de respuesta se definirán durante el desarrollo, teniendo en cuenta los recursos disponibles en el entorno ROS 2 de prácticas.

## 3.4. Funcionalidades fuera del alcance de la implementación

Aunque algunas de las siguientes capacidades se contemplan en el diseño global, no se consideran imprescindibles para la demostración funcional:

- Implementación completa de todos los módulos de actividades cognitivas.
- Desarrollo de una aplicación profesional de gestión de usuarios y sesiones.
- Integración con historiales clínicos o plataformas sanitarias.
- Diagnóstico, evaluación clínica o seguimiento terapéutico automatizado.
- Reconocimiento de identidad o identificación biométrica de los participantes.
- Adaptación automática basada en modelos de inteligencia artificial entrenados con datos personales.
- Validación clínica de la eficacia de las actividades.
- Funcionamiento autónomo sin supervisión profesional en entornos reales.

Estas funcionalidades podrían estudiarse en futuras ampliaciones, siempre que se disponga de los recursos técnicos, humanos y éticos necesarios.

## 3.5. Entorno de funcionamiento y limitaciones

La propuesta se orienta a espacios interiores controlados y previamente evaluados, con condiciones adecuadas para el desplazamiento seguro del robot.

Se tendrán en cuenta las siguientes limitaciones:

- La autonomía de navegación dependerá de las condiciones del entorno y de la configuración de los sensores.
- La detección de personas podrá verse afectada por la iluminación, la distancia y posibles oclusiones.
- La interacción por voz dependerá del ruido ambiental y de las características del sistema de reconocimiento utilizado.
- La comprensión de respuestas abiertas no será una capacidad garantizada en la primera implementación.
- La seguridad del desplazamiento requerirá supervisión y mecanismos de parada ante situaciones imprevistas.
- La aceptación de la interacción y los estímulos deberá respetar las preferencias individuales de cada participante.

## 3.6. Posibles ampliaciones futuras

Una vez validada la demostración inicial, el sistema podría ampliarse mediante:

- Incorporación de nuevos módulos de actividades.
- Desarrollo de una interfaz gráfica accesible para profesionales.
- Integración de sistemas de comunicación aumentativa y alternativa.
- Personalización de las actividades mediante perfiles configurables.
- Incorporación de herramientas de análisis de resultados.
- Desarrollo de mecanismos de interacción multimodal.
- Evaluación del sistema en entornos reales con la supervisión y las autorizaciones correspondientes.

## 3.7. Síntesis del alcance

REHABOT KIDS se plantea como una propuesta modular y ampliable de robótica asistencial. El diseño contempla un sistema completo de navegación, percepción e interacción orientado a actividades de estimulación cognitiva, mientras que la implementación práctica se centrará en una misión funcional sobre TurtleBot 4.

Esta separación permitirá demostrar la viabilidad técnica de los componentes principales sin confundir el prototipo desarrollado con un sistema clínico terminado.
