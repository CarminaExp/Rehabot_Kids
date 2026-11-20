
import rclpy
from rclpy.node import Node

from hri_client.hri_client import HRIClient


class CognitiveGameNode(Node):

    def __init__(self):
        super().__init__('cognitive_game_node')

        self.hri = HRIClient(self)

        self.questions = [
            ("Los perros suelen tener cuatro patas.", "yes",
             "Piensa en las patas de un perro."),
            ("Los peces viven normalmente fuera del agua.", "no",
             "Los peces necesitan agua para vivir."),
            ("Una manzana es una fruta.", "yes",
             "Las manzanas crecen en los árboles."),
            ("El hielo está caliente.", "no",
             "El hielo está muy frío."),
            ("El autobús sirve para transportar personas.", "yes",
             "Muchas personas viajan en autobús.")
        ]

        self.index = 0
        self.score = 0
        self.state = 'GREETING'

        if not self.hri.wait_until_ready(5.0):
            self.get_logger().error('Los servicios HRI no están disponibles.')
            self.state = 'ERROR'

        self.timer = self.create_timer(0.1, self.control_cycle)

        self.get_logger().info('Juego cognitivo preparado.')

    def control_cycle(self):

        if self.state == 'GREETING':
            self.hri.start_speaking(
                '¡Hola! ¿Quieres jugar conmigo a un juego de preguntas?'
            )
            self.state = 'WAIT_GREETING'

        elif self.state == 'WAIT_GREETING':
            if self.hri.is_speaking_done():
                self.state = 'QUESTION'

        elif self.state == 'QUESTION':
            if self.index >= len(self.questions):
                self.state = 'FINAL'
                return

            statement = self.questions[self.index][0]

            self.hri.start_speaking(
                f'Pregunta {self.index + 1}. '
                f'¿Es verdad que {statement} Di sí o no.'
            )
            self.state = 'WAIT_QUESTION'

        elif self.state == 'WAIT_QUESTION':
            if self.hri.is_speaking_done():
                self.hri.start_listening(timeout_sec=10.0)
                self.state = 'WAIT_LISTEN'

        elif self.state == 'WAIT_LISTEN':
            if self.hri.is_listening_done():
                answer = self.hri.get_listened_text().lower()

                if any(word in answer for word in
                       ['parar', 'terminar', 'descansar', 'no quiero']):
                    self.state = 'FINAL'
                    return

                if not answer:
                    self.hri.start_speaking(
                        'No he podido escucharte. Pasamos a otra pregunta.'
                    )
                    self.state = 'WAIT_SKIP'
                    return

                self.hri.start_yesno(text=answer)
                self.state = 'WAIT_YESNO'

        elif self.state == 'WAIT_YESNO':
            if self.hri.is_yesno_done():
                result = self.hri.get_yesno_result()
                expected = self.questions[self.index][1]
                hint = self.questions[self.index][2]

                if result == expected:
                    self.score += 1
                    feedback = '¡Muy bien! Has acertado.'
                elif result in ['yes', 'no']:
                    feedback = f'No pasa nada. Una pista: {hint}'
                else:
                    feedback = 'No he entendido la respuesta. Seguimos.'

                self.hri.start_speaking(feedback)
                self.state = 'WAIT_FEEDBACK'

        elif self.state == 'WAIT_SKIP':
            if self.hri.is_speaking_done():
                self.index += 1
                self.state = 'QUESTION'

        elif self.state == 'WAIT_FEEDBACK':
            if self.hri.is_speaking_done():
                self.index += 1
                self.state = 'QUESTION'

        elif self.state == 'FINAL':
            self.hri.start_speaking(
                f'¡Juego terminado! Has acertado '
                f'{self.score} de {len(self.questions)} preguntas. '
                '¡Gracias por jugar conmigo!'
            )
            self.state = 'WAIT_FINAL'

        elif self.state == 'WAIT_FINAL':
            if self.hri.is_speaking_done():
                self.get_logger().info(
                    f'Juego finalizado. Puntuación: {self.score}'
                )
                self.state = 'DONE'

        elif self.state == 'ERROR':
            return


def main(args=None):
    rclpy.init(args=args)
    node = CognitiveGameNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
