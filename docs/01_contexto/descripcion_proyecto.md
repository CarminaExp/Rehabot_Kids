# 1. Descripción del proyecto

## 1.1. Nombre del proyecto

**REHABOT KIDS: Robot móvil inteligente para el acompañamiento y la estimulación cognitiva de niños con Trastorno del Espectro Autista (TEA).**

## 1.2. Contextualización

El Trastorno del Espectro Autista (TEA) comprende un conjunto diverso de condiciones relacionadas con el desarrollo neurológico. Puede manifestarse mediante diferencias en la comunicación y la interacción social, patrones de comportamiento e intereses específicos y distintas formas de procesar los estímulos sensoriales. Las capacidades, preferencias y necesidades de apoyo varían considerablemente entre personas y pueden cambiar a lo largo de su vida (Organización Mundial de la Salud [OMS], 2025).

En este contexto, las tecnologías de apoyo y la robótica asistencial ofrecen posibilidades para complementar las intervenciones educativas y terapéuticas mediante herramientas interactivas, adaptables y accesibles. En particular, los robots sociales pueden proporcionar entornos de interacción estructurados y actividades que permitan trabajar diferentes habilidades en compañía de profesionales.

La investigación sobre intervenciones mediadas por robots ha mostrado resultados prometedores en determinados ámbitos. Por ejemplo, la revisión sistemática y metaanálisis de Kouroupa et al. (2022) identificó resultados favorables en el funcionamiento social, aunque también señaló limitaciones en la cantidad y calidad de los estudios para algunas áreas. Por tanto, estas tecnologías deben considerarse herramientas complementarias y no sustitutos de la intervención profesional.

## 1.3. Descripción de la propuesta

REHABOT KIDS plantea el diseño y desarrollo de un sistema robótico asistencial basado en la plataforma móvil TurtleBot 4. El proyecto propone combinar capacidades de navegación autónoma, percepción del entorno e interacción persona-robot para ofrecer actividades de estimulación cognitiva en entornos interiores.

El robot podrá desplazarse por un espacio delimitado, detectar la presencia de una persona e iniciar una interacción de forma controlada. A partir de ese momento, ofrecerá diferentes actividades que podrán seleccionarse y desarrollarse mediante mecanismos de interacción verbal y apoyos visuales.

La propuesta contempla diferentes módulos de actividades:

- **Memoria y atención:** reconocimiento y recuerdo de elementos visuales, asociación de imágenes y búsqueda de elementos.
- **Secuenciación y organización:** ordenación de acontecimientos, secuencias lógicas y rutinas cotidianas.
- **Clasificación y razonamiento:** agrupación de elementos, identificación de patrones y resolución de pequeños problemas.
- **Comunicación funcional:** elección entre alternativas, solicitud de ayuda, expresión de preferencias y respeto de turnos.
- **Comprensión de situaciones sociales y emocionales:** interpretación de escenas ilustradas y exploración de posibles respuestas ante situaciones cotidianas.
- **Autonomía y anticipación:** presentación de agendas visuales, organización de actividades y preparación de transiciones.

Estas actividades estarán concebidas para poder adaptarse en dificultad, duración y forma de presentación, teniendo en cuenta las preferencias y necesidades de cada participante.

## 1.4. Enfoque de intervención

REHABOT KIDS se plantea como una herramienta complementaria de apoyo en contextos de intervención temprana, rehabilitación pediátrica y educación especializada. Su finalidad no es diagnosticar, tratar ni sustituir la atención proporcionada por profesionales, sino facilitar experiencias interactivas que puedan incorporarse a actividades previamente planificadas.

El diseño seguirá un enfoque respetuoso con la neurodiversidad. Se evitará considerar que todos los niños con TEA presentan las mismas características o necesitan las mismas formas de interacción. Por ello, se contemplarán opciones de personalización relacionadas con:

- El ritmo y la duración de las actividades.
- La complejidad de los ejercicios.
- La intensidad de los estímulos visuales y sonoros.
- La utilización de pictogramas y otros apoyos comunicativos.
- La posibilidad de solicitar ayuda, descansar, cambiar de actividad o finalizar la interacción.

La participación será voluntaria y el sistema deberá respetar los tiempos de respuesta, las preferencias sensoriales y las señales de rechazo o incomodidad.

## 1.5. Plataforma tecnológica

La plataforma robótica seleccionada es TurtleBot 4, un robot móvil basado en ROS 2 y orientado a investigación y educación. Su arquitectura integra una base móvil iRobot Create 3, un ordenador Raspberry Pi 4 y sensores que permiten obtener información del entorno, como una cámara de profundidad y un sensor LiDAR, dependiendo de la versión del modelo (Open Robotics, s. f.).

El uso de ROS 2 permitirá organizar el sistema mediante una arquitectura modular, distribuyendo las diferentes funcionalidades en nodos independientes. Entre las capacidades previstas se encuentran:

- Navegación autónoma mediante Nav2.
- Detección de personas y percepción del entorno.
- Aproximación controlada y evitación de obstáculos.
- Interacción mediante voz y apoyos visuales.
- Gestión de actividades mediante una máquina de estados finitos.
- Registro de resultados básicos de las sesiones.

La selección de TurtleBot 4 permite utilizar una plataforma móvil real para desarrollar y validar las capacidades de navegación e interacción, manteniendo una arquitectura ampliable para incorporar nuevas actividades.

## 1.6. Organización general del proyecto

El proyecto se dividirá en dos niveles de desarrollo:

**Diseño completo del sistema:** contempla la arquitectura general de REHABOT KIDS, sus módulos funcionales, las actividades cognitivas, los mecanismos de interacción, los criterios de seguridad y las posibilidades de adaptación.

**Implementación de una demostración funcional:** se desarrollará una misión reducida sobre TurtleBot 4 que permita comprobar la integración de algunas de las capacidades principales, como la detección de una persona, la aproximación segura, el inicio de una interacción y la ejecución de una actividad sencilla.

Esta separación permitirá presentar una propuesta global coherente y, al mismo tiempo, demostrar de forma práctica una parte representativa de su funcionamiento.

## Referencias

- Kouroupa, A., Laws, K. R., Irvine, K., Mengoni, S. E., Baird, A., & Sharma, S. (2022). The use of social robots with children and young people on the autism spectrum: A systematic review and meta-analysis. *PLOS ONE, 17*(6), e0269800. https://doi.org/10.1371/journal.pone.0269800
- Open Robotics. (s. f.). *TurtleBot 4 User Manual*. https://turtlebot.github.io/turtlebot4-user-manual/
- Organización Mundial de la Salud. (2025, 17 de septiembre). *Autismo*. https://www.who.int/es/news-room/fact-sheets/detail/Autism-Spectrum-Disorders
