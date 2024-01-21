# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


class ActionChiste(Action):
    chistes = [
        "¿Qué le dice un gusano a otro gusano?\nMe voy a dar una vuelta a la manzana.",
        "¿Qué planeta va después de Marte?\nMiércole",
        "¿Por qué algunos niños ponen azúcar debajo de la almohada?\nPara tener dulces sueños",
        "Mamá, mamá, en el máster me llaman mentiroso\nPero hijo, ¡Tú no vas al máster!",
        "Papá, ¿qué se siente tener un hijo tan guapo?\nNo los sé hijo, pregúntale a tu abuelo"
    ]

    def name(self) -> Text:
        return "action_elige_chiste"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=random.choice(self.chistes))
        return []