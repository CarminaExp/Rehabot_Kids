# 4. Estado del arte

## 4.1. Introducción a la robótica social y asistencial

### 4.1.1. Robótica social

La robótica social es un ámbito de la robótica que estudia el diseño y desarrollo de sistemas capaces de interactuar con personas mediante comportamientos y mecanismos de comunicación social. Estas interacciones pueden incluir el uso de voz, gestos, movimientos, expresiones, señales luminosas y otros recursos que permiten establecer una comunicación entre el robot y su usuario.

A diferencia de los robots industriales, cuyo funcionamiento suele centrarse en la ejecución de tareas físicas o productivas, los robots sociales incorporan mecanismos de interacción persona-robot (Human-Robot Interaction, HRI). Su finalidad puede incluir el acompañamiento, la educación, el entretenimiento, la asistencia y el apoyo en diferentes actividades cotidianas.

Dentro de este ámbito se encuentra la robótica socialmente asistencial (Socially Assistive Robotics, SAR), que utiliza la interacción con robots para proporcionar apoyo a personas sin que necesariamente exista contacto físico directo. Estos sistemas pueden emplearse en actividades educativas, de rehabilitación, acompañamiento y entrenamiento de determinadas habilidades.

### 4.1.2. Aplicación de la robótica social en el TEA

La utilización de robots sociales con niños con Trastorno del Espectro Autista (TEA) constituye una línea de investigación en crecimiento. Una de las motivaciones principales es explorar si las características de interacción de estos sistemas pueden facilitar la participación en actividades estructuradas y proporcionar situaciones de comunicación más predecibles.

Algunas investigaciones han estudiado el uso de robots para trabajar aspectos como:

- La atención compartida y la atención hacia determinados estímulos.
- La imitación de movimientos y acciones.
- La comunicación y la interacción social.
- El reconocimiento y la interpretación de situaciones sociales.
- La toma de turnos y la cooperación.
- La participación en juegos y actividades educativas.

Los robots permiten controlar determinados elementos de la interacción, como la duración de una actividad, la repetición de instrucciones, la velocidad de presentación de estímulos y la secuencia de acciones. Estas características pueden facilitar la adaptación de las tareas a las preferencias y necesidades de cada participante.

Sin embargo, la respuesta a una intervención mediada por robots no es necesariamente igual para todos los niños. La aceptación del robot, los intereses individuales, las características sensoriales y el contexto de aplicación pueden influir en la experiencia. Por ello, el diseño debe contemplar diferentes formas de participación y evitar imponer una única manera de interactuar.

### 4.1.3. Evidencia científica y limitaciones

Kouroupa et al. (2022) realizaron una revisión sistemática y metaanálisis sobre el uso de robots sociales con niños y jóvenes dentro del espectro autista. El estudio incluyó 12 ensayos controlados aleatorizados. La mayoría de las intervenciones utilizaban robots humanoides y se centraban principalmente en habilidades sociales y comunicativas.

Los resultados del metaanálisis mostraron un efecto positivo significativo de las intervenciones mediadas por robots sobre el funcionamiento social. No obstante, los autores también señalaron limitaciones relacionadas con el número de estudios, la diversidad de intervenciones y la necesidad de investigar su aplicación en contextos cotidianos.

Estos resultados permiten considerar la robótica social como un campo prometedor, pero no justifican asumir que cualquier robot o actividad produzca beneficios terapéuticos. Es necesario evaluar cada propuesta atendiendo a sus objetivos, población, contexto y metodología.

### 4.1.4. Tipologías de robots utilizados

En las investigaciones relacionadas con la interacción y el apoyo a niños con TEA se encuentran diferentes tipologías de robots:

**Robots humanoides:** presentan una apariencia inspirada en el cuerpo humano y pueden utilizar gestos, movimientos y expresiones simplificadas para facilitar determinadas interacciones. Algunos ejemplos son NAO, KASPAR y QTrobot.

**Robots zoomórficos:** reproducen características de animales y suelen utilizarse en experiencias de acompañamiento e interacción afectiva. PARO, un robot con apariencia de foca, es uno de los ejemplos más conocidos.

**Robots móviles:** se desplazan por el entorno y permiten incorporar capacidades de navegación, seguimiento, percepción y aproximación a las personas. Su diseño puede ser menos antropomórfico y está especialmente orientado a la interacción en espacios físicos.

**Robots de apariencia simplificada o lúdica:** presentan diseños sencillos que pueden utilizarse en actividades de juego, imitación, atención e interacción. En esta categoría pueden encontrarse plataformas como Keepon.

Cada tipología presenta ventajas y limitaciones diferentes. La elección depende de los objetivos de la intervención, las características de los usuarios, el entorno y las capacidades técnicas requeridas.

### 4.1.5. Relación con REHABOT KIDS

A partir de las investigaciones existentes, REHABOT KIDS plantea una aproximación basada en una plataforma móvil en lugar de diseñar un robot humanoide específico.

La elección de TurtleBot 4 permite centrar el desarrollo en la integración de capacidades de navegación autónoma, percepción del entorno e interacción persona-robot mediante ROS 2.

A diferencia de los robots sociales diseñados específicamente para la interacción terapéutica, TurtleBot 4 es una plataforma abierta de investigación y educación. Por tanto, las capacidades sociales y las actividades cognitivas de REHABOT KIDS deberán desarrollarse mediante software y mecanismos de interacción adicionales.

Esta elección permite explorar una arquitectura modular y ampliable, en la que el desplazamiento del robot se combina con actividades de memoria, atención, razonamiento, comunicación y autonomía.

## Referencias

- Kouroupa, A., Laws, K. R., Irvine, K., Mengoni, S. E., Baird, A., & Sharma, S. (2022). The use of social robots with children and young people on the autism spectrum: A systematic review and meta-analysis. *PLOS ONE, 17*(6), e0269800. https://doi.org/10.1371/journal.pone.0269800
- Open Robotics. (s. f.). *TurtleBot 4 User Manual*. https://turtlebot.github.io/turtlebot4-user-manual/
