from .books_db import BooksDB

from typing import Any, Dict, List, Text
import random

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted, FollowupAction, SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher

class ActionTwoStageFallback(Action):
  def name(self) -> Text:
    return "action_two_stage_fallback"

  def run(
    self,
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any],
  ) -> List[Dict[Text, Any]]:
    nlu_data = tracker.latest_message.get('parse_data', {})
    ranked_intents = nlu_data.get('intent_ranking', [])
    if len(ranked_intents) > 1:
      next_intent = ranked_intents[1].get('name')

      dispatcher.utter_message(template="utter_ask_rephrase")
      dispatcher.utter_message(text=f"¿Acaso quisiste decir '{next_intent}'?")
      return [FollowupAction(name="action_default_ask_affirmation")]
    else:
      dispatcher.utter_message(response="utter_default")
      return [UserUtteranceReverted()]

class ActionRecommendBook(Action):
  def name(self) -> Text:
    return "action_recommend_book"

  def run(
    self,
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any]
  ) -> List[Dict[Text, Any]]:
    book_genre = tracker.get_slot("book_genre")

    if not book_genre:
      dispatcher.utter_message(text="No entendí tu género favorito. ¿Puedes especificar qué género de libro te gustaría?")
      return []

    books_of_genre = BooksDB.find_books_by_genre_fuzzy(book_genre)
    if len(books_of_genre) > 0:
      book_recommendation = random.choice(books_of_genre)
      dispatcher.utter_message(text=f"De '{book_genre}' te recomiendo leer '{book_recommendation['title']}' del autor {book_recommendation['author']}.")
    else:
      dispatcher.utter_message(text="Vaya lo siento mucho, no tengo recomendaciones para ese género.")

    return []
