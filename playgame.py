from PyInquirer import prompt, style_from_dict


question = [
    {
        'type': 'list',
        'name': 'game',
        'message': 'What would you like to play?',
        'choices': [
            'Dragon Realm',
            'Rock Paper Scissor',
            'Number Guess',
            'Tic Tac Toe',
            'Hangman'
        ]
    }
]

answer = prompt(question).get('game')
if answer == 'Dragon Realm':
    from dragon_realm import main
    main()
elif answer == 'Rock Paper Scissor':
    from RockPaperScissor import main
    main()
elif answer == 'Number Guess':
    from guess_the_number import main
    main()
elif answer == 'Tic Tac Toe':
    from tictactoe import main
    main()
else:
    from hangman import main
    main()