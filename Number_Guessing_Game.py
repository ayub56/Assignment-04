{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP+TxkVb0jGHCbqZ69HfFMX",
   
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Mohsinraza23/Assignment-04/blob/main/Number_guessing(comp).ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "print(\"\\n ✨Welcome to the Number Guessing Game.✨ \\n\")\n",
        "print(\"\\n 💻 Computer Guess the Number. \\n\")\n",
        "\n",
        "low = 1\n",
        "high = 10\n",
        "\n",
        "print(\"🤔 Think of a number between 1 and 10, and 💻 will try to guess it!\")\n",
        "\n",
        "while low <= high:  # Loop to keep guessing until the correct number is found\n",
        "    guess = random.randint(low, high)\n",
        "    print(f\"🤖 Is your number {guess}?\")\n",
        "\n",
        "    feedback = input(\" 👉 Enter 'h' for too high, 'l' for too low, or 'c' for correct: \").lower()\n",
        "\n",
        "    if feedback == 'h':\n",
        "        high = guess - 1\n",
        "    elif feedback == 'l':\n",
        "        low = guess + 1\n",
        "    elif feedback == 'c':\n",
        "        print(f\"🎉 Yay! 💻 guessed {guess} correctly. 🎉\")\n",
        "        break  # Exit loop if guessed correctly\n",
        "    else:\n",
        "        print(\"⚠️ Invalid input. Please enter only 'h', 'l', or 'c'. 🚫\")\n",
        "\n",
        "if low > high:\n",
        "    print(\"😅 Hmm... It seems there was a misunderstanding. Let's try again! 🔄\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BadhAI2L_7cf",
        "outputId": "804e80ba-f7ec-4676-813b-944aa61fe5bf"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            " ✨Welcome to the Number Guessing Game.✨ \n",
            "\n",
            "\n",
            " 💻 Computer Guess the Number. \n",
            "\n",
            "🤔 Think of a number between 1 and 10, and 💻 will try to guess it!\n",
            "🤖 Is your number 10?\n",
            " 👉 Enter 'h' for too high, 'l' for too low, or 'c' for correct: 4\n",
            "⚠️ Invalid input. Please enter only 'h', 'l', or 'c'. 🚫\n",
            "🤖 Is your number 9?\n",
            " 👉 Enter 'h' for too high, 'l' for too low, or 'c' for correct: h\n",
            "🤖 Is your number 1?\n",
            " 👉 Enter 'h' for too high, 'l' for too low, or 'c' for correct: 9\n",
            "⚠️ Invalid input. Please enter only 'h', 'l', or 'c'. 🚫\n",
            "🤖 Is your number 7?\n",
            " 👉 Enter 'h' for too high, 'l' for too low, or 'c' for correct: c\n",
            "🎉 Yay! 💻 guessed 7 correctly. 🎉\n"
          ]
        }
      ]
    }
  ]
}
