def hangman_game_start():
    print("アクセスありがとうございます。\n\nゲーム【ハングマン】を開始いたします。\n"\
    "このゲームは、ハングマンが完成する前に、答えを探し当てるゲームです。\n"\
    "正解を目指して頑張ってください。")

def hangman_select():
    hangman = []
    hangman.append("_________")
    hangman.append("    |    ")
    hangman.append("    O    ")
    hangman.append("   -|-   ")
    hangman.append("   | |   ")
    hangman.append("         ")
    hangman.append("_________")

    hangman_half_way = []

    return hangman,hangman_half_way


def hangman_check(hangman,hangman_half_way):
    miss_count = len(hangman_half_way)
    hangman_half_way.append(hangman[miss_count])

    return hangman_half_way


def hangman_display(hangman_half_way):
    string_half_way = "\n".join(hangman_half_way)

    if string_half_way == "":
        print("\nハングマンはまだ作成が開始されていません。\n")
    else:
        print("\nハングマンは\n {0} \nです。\n".format(string_half_way))
