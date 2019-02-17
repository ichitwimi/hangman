def game_load(answer,answer_half_way,hangman,hangman_half_way):
    clear_flag = 0
    fail_flag = 0

    if answer == answer_half_way:
        answer_display_word = "".join(answer_half_way)
        print("\n正解しました。\n回答は{0}です。\n\nあなたの勝ちです！！\nおめでとうございます！！！\n".format(answer_display_word))
        clear_flag = 1
    elif hangman == hangman_half_way:
        hangman_display_word = "\n".join(hangman_half_way)
        print("ハングマンが完成してしまいました。\n{0}\nあなたの負けです。\n\n次回の挑戦をお待ちしています。\n".format(hangman_display_word))
        fail_flag = 1
    else:
        print("ゲームは続きます！頑張ってください！！")

    return clear_flag,fail_flag
