word_list = ['게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', '멍게', '박쥐', '본네트', '빨대', '살구', '양심', '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글']


print('<시작>끝말잇기를 하자. 내가 먼저 말할게.')
while True:
    temp_com = '기차'
    print("기차")
    word_list.remove('기차')

    temp = input("")

    if temp[0] == temp_com[-1]:
        for item in word_list:
            pass
