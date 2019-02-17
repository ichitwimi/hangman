import csv
import random

def word_select():
    # 答えとなる単語と途中経過を1要素1スペルのリストにしてreturnする。
    csv_file_name = "selectwords.csv"

    with open(csv_file_name,"r") as file:
        reader = csv.reader(file)
        readarray = list(reader)

        row = len(readarray)-1  # csvファイルに含まれる行数を取得（0スタート）
        col = [len(v) for v in readarray]   # csvファイルに含まれる行ごとの要素数（リスト）

        row_value = random.randint(0,row)

        col_len = len(readarray[row_value]) - 1
        col_value = random.randint(0,col_len)

        list_word = list(readarray[row_value][col_value])
        list_word_half_way = ["_"] * len(readarray[row_value][col_value])

        return list_word,list_word_half_way


def word_input():
    while True:
        print("---------------------------------")
        input_word = input("アルファベットを1文字入力してください。\n")

        if len(input_word) == 1:
            break
        else:
            print("入力できる文字数は、アルファベット1文字だけです。もう一度入力してください。\n")

    return input_word


def word_check(input_word,answer,answer_half_way):
    miss = 1
    for index in range(0,len(answer)):
        if answer_half_way[index] == "_":
            if answer[index] == input_word:
                answer_half_way[index] = input_word
                print("\n入力したアルファベット {0} が一致しました。".format(input_word))
                miss = 0
                break

    if miss != 0:
        print("\n入力した文字 {0} は一致しませんでした。".format(input_word))

    return answer_half_way,miss


def word_display(answer_half_way):
    string_half_way = " ".join(answer_half_way)
    print("\n")
    print("現在の回答状況は {0} です。".format(string_half_way))
