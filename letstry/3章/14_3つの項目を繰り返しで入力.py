#BMIチェックに必要な名前、体重、身長を1つの塊り（リスト）にする
bmi_elements = ['', 0.0, 0.0]
bmi_messages = ['名前', '体重(kg)', '身長(m)']

#3つの項目を入力
num = 0
for entry in bmi_messages :
    bmi_elements[num] = input( entry + 'を入力してください：')
    num = num + 1

#入力された内容を確認のため表示
print('入力された内容を確認のため表示')
print(f'名前：{bmi_elements[0]}')
print(f'体重と身長：{bmi_elements[1:]}')
print('-----')

#入力された名前を使ってメッセージを作成
message = bmi_elements[0] + 'さんのBMIは、'

#入力された体重と身長は文字列なので計算できるよう浮動小数点に変換
my_weight = float(bmi_elements[1])
my_height = float(bmi_elements[2])

#BMI=体重[kg]÷(身長[m]×身長[m])
my_bmi = my_weight / (my_height * my_height)
print(f'{message}{my_bmi}です。')
