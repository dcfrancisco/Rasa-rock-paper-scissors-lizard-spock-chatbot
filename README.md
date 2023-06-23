# Rock, Paper, Scissors, Lizard, Spock Chatbot

This repository contains the codebase for a Rasa chatbot that plays a game of Rock, Paper, Scissors, Lizard, Spock. The game was popularized by the TV show "The Big Bang Theory" but it was originally invented by Software Engineer Sam Kass in 1998. It's an expansion of the classic game of Rock, Paper, Scissors, adding two new options to increase complexity and fun.

This project is based on the [Rock, Paper, Scissors Chatbot](https://github.com/rctatman/Rasa-3.0-rock-paper-scissors-chatbot) by Rebecca Tatman.

## Game Rules

Each player chooses a hand shape (rock, paper, scissors, lizard, or Spock). The winner is determined by the rules of the game:

- Scissors cuts Paper
- Paper covers Rock
- Rock crushes Lizard
- Lizard poisons Spock
- Spock smashes Scissors
- Scissors decapitates Lizard
- Lizard eats Paper
- Paper disproves Spock
- Spock vaporizes Rock
- Rock crushes Scissors

These rules create a game that is balanced and fun to play, as each choice wins against two others and loses to two others.

## Project Structure

The project uses Rasa, an open-source machine learning framework for building conversational AI. It comprises of several files and directories:

- `actions.py`: Contains custom action for the bot to execute, including determining the game's outcome.
- `nlu.yml`: Holds examples of user inputs for training the NLU model.
- `stories.yml`: Provides sample conversational paths to train the dialogue model.
- `domain.yml`: Defines the chatbot's universe, including intents, entities, responses, and actions.
- `config.yml`: Sets the pipeline and policies for NLU and dialogue management.

## How to Use

1. Install the necessary dependencies, primarily Rasa and Rasa SDK.
2. Train the Rasa model using the command `rasa train`.
3. Start the action server in a separate terminal window with `rasa run actions`.
4. In another terminal, start the chatbot with `rasa shell`.
5. Enjoy playing the game with the bot!

This project provides a good starting point for exploring Rasa capabilities and building more sophisticated conversational AI agents. You can extend the bot functionality by adding more intents, responses, and custom actions based on your requirements.

**Note:** The chatbot is designed to be simple and illustrative; it doesn't handle every possible type of user input. Some level of conversational AI understanding and customization might be needed to adapt the chatbot to more complex dialogues.

## License

This project is licensed under the [MIT License](LICENSE).