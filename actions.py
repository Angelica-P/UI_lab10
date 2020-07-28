# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
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


from rasa_sdk.forms import FormAction

class BookAppointment(FormAction):

	def name(self):
		return "book_appointment"

	@staticmethod
	def required_slots(tracker):
		return [
			"first_name",
			"last_name",
			"email",
			"phone_number",
			"appointment_type",
			"appointment_with",
			"date",
			"time",
			"credit_card"
		]

	def submit(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> List[Dict]:
		dispatcher.utter_message("Your appointment has been booked. Wicked Hair thanks you.")
		return []

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
		return {"first_name": self.from_text(intent="inform"),
				"last_name": self.from_text(intent="inform"),
				"email": self.from_text(intent="inform"),
				"phone_number": self.from_text(intent="inform"),
				"appointment_type": self.from_text(intent="inform"),
				"appointment_with": self.from_text(intent="inform"),
				"date": self.from_text(intent="inform"),
				"time": self.from_text(intent="inform"),
				"credit_card": self.from_text(intent="inform")
				}