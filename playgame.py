from PyInquirer import prompt, style_from_dict


question = [
    {
        "type": "list",
        "name": "game",
        "message": "What would you like to play?",
        "choices": [
            "Dragon Realm",
            "Rock Paper Scissor",
            "Number Guess",
            "Tic Tac Toe",
            "Hangman",
            "Minesweeper"
        ],
    }
]

answer = prompt(question).get("game")
if answer == "Dragon Realm":
    from src.dragon_realm import main
    main()

elif answer == "Rock Paper Scissor":
    from src.RockPaperScissor import main
    main()

elif answer == "Number Guess":
    from src.guess_the_number import main
    main()

elif answer == "Tic Tac Toe":
    from src.tictactoe import main
    main()

elif answer == "Minesweeper":
    from src.minesweeper import main
    main()
else:
    from src.hangman import main
    main()
