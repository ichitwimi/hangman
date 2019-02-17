import word
import fail
import check

fail.hangman_game_start()

answer,answer_half_way = word.word_select()
# answerには正解となる単語を、answer_half_wayには回答状況を格納します。
hangman,hangman_half_way = fail.hangman_select()
# hangmanにはハングマンの完成形を、hangman_half_wayには現在のハングマン作成状況を格納します。

while True:
    word.word_display(answer_half_way)
    fail.hangman_display(hangman_half_way)

    input_word = word.word_input()
    answer_half_way,miss_flag = word.word_check(input_word,answer,answer_half_way)

    # 入力した文字が一致しなかった場合のみ、ハングマンを更新する関数を呼び出します。
    if miss_flag == 1:
        hangman_half_way = fail.hangman_check(hangman,hangman_half_way)

    # 勝利条件、敗北条件を確認します。
    clear_flag,fail_flag = check.game_load(answer,answer_half_way,hangman,hangman_half_way)

    if clear_flag == 1:
        break
    elif fail_flag == 1:
        break
    else:
        continue
