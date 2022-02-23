# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Dict, Text, Any, List, Union, Optional, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.types import DomainDict

class ActionUserInfo(FormAction):
    """ Form action to fill all user details required for purchase """
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "user_info_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["user_name", "email_id", "devices_list"]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""

        return {
            "user_name": self.from_entity(entity="user_name"),
            "email_id": self.from_entity(entity="email_id"),
            "devices_list": self.from_entity(entity="devices_list"),
        }

    def validate_user_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate user_name value."""

        return {"user_name": slot_value}

    def validate_email_id(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate email_id value."""

        return {"email_id": slot_value}

    def validate_devices_list(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate devices_list value."""

        return {"devices_list": slot_value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_added_to_cart", tracker)
        return []

    

class ActionSuggestions(FormAction):
    """ Form action to fill all user details required for purchase """
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "suggestions_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["budget", "camera"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""

        return {
            "budget": self.from_entity(entity="budget"),
            "camera": self.from_entity(entity="camera"),
        }

    def validate_budget(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate budget value."""

        return {"budget": slot_value}

    def validate_camera(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate camera value."""

        return {"camera": slot_value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template("utter_show_recs", tracker)
        return []