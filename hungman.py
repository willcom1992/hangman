def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|    ",
             "|       /     ",
             "|               "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")

    while wrong < len(stages) - 1:
        print('\n')
        char = input('一文字を予想してね')
        if char in rletters :
            cind = rletters.index(char)#入力された文字が何番目にあるか
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        
        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print('あなたの勝ち')
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print('貴方の負け！正解は {}'.format(word))


hangman("cat")