import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction


class ActionPlayRPSLS(Action):
    def name(self) -> Text:
        return "action_play_rpsls"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        choices = ["rock", "paper", "scissors", "spock", "lizard"]
        computer_choice = random.choice(choices)

        user_choice = tracker.latest_message["text"]
        user_choice = user_choice.lower()

        if user_choice not in choices:
            dispatcher.utter_message(
                "Sorry, I didn't understand your choice. Please try again."
            )
            return []

        dispatcher.utter_message(f"You chose {user_choice.capitalize()}")
        dispatcher.utter_message(f"The computer chose {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            dispatcher.utter_message("It's a tie!")
        elif (
            (
                user_choice == "rock"
                and (computer_choice == "scissors" or computer_choice == "lizard")
            )
            or (
                user_choice == "paper"
                and (computer_choice == "rock" or computer_choice == "spock")
            )
            or (
                user_choice == "scissors"
                and (computer_choice == "paper" or computer_choice == "lizard")
            )
            or (
                user_choice == "spock"
                and (computer_choice == "rock" or computer_choice == "scissors")
            )
            or (
                user_choice == "lizard"
                and (computer_choice == "paper" or computer_choice == "spock")
            )
        ):
            win_message = f"Congratulations! {user_choice.capitalize()} {self.get_win_message(user_choice, computer_choice)}"
            dispatcher.utter_message(win_message)
        else:
            lose_message = f"Sorry, the computer wins! {computer_choice.capitalize()} {self.get_win_message(computer_choice, user_choice)}"
            dispatcher.utter_message(lose_message)

        return [FollowupAction("utter_play_again")]

    @staticmethod
    def get_win_message(winning_choice: Text, losing_choice: Text) -> Text:
        rules = {
            "rock": {"scissors": "crushes", "lizard": "crushes"},
            "paper": {"rock": "covers", "spock": "disproves"},
            "scissors": {"paper": "cuts", "lizard": "decapitates"},
            "spock": {"rock": "vaporizes", "scissors": "smashes"},
            "lizard": {"paper": "eats", "spock": "poisons"},
        }

        if winning_choice in rules and losing_choice in rules[winning_choice]:
            # return f"{winning_choice.capitalize()} {rules[winning_choice][losing_choice]} {losing_choice}."
            return f"{rules[winning_choice][losing_choice]} {losing_choice}."

        return ""
