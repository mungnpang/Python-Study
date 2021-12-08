# @@@01.파이썬 시작하기@@@
# no.1 화면에 Hello World 문자열을 출력하세요.
# print ("Hello World")


# no.2 화면에 Mary's cosmetics 를 출력하세요. (중간에 '가 있음에 주의)
# print("Mary's cosmetics")
# print('Mary\'s cosmetics')


# no.3 화면에 아래 문장을 출력하세요. (중간에 ""가 있음에 주의)
#     신씨가 소리질렀다. "도둑이야".
# print('신씨가 소리질렀다."도둑이야".')
# <백슬래시를 활용한 답안>
# print("신씨가 소리질렀다. \"도둑이야\"")


# no.4 화면에 "C:\Windows"를 출력하세요.
# print('"C:\Windows"')
# 굳이 ""를 쓰지않아도 된다면 모든 문자열을 입력값 그대로 쓰기위해 큰따옴표3개(""" """) 를 써도 무방
# print("""C:\Windows""")


# no.5 다음 코드를 실행해보고 \t와 \n의 역할을 설명해 보세요.
# print("안녕하세요.\n만나서\t\t반갑습니다.")
# -> \n은 줄바꿈 \t는 탭키의 역할을 수행


# no.6 print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해 봅시다.
# print ("오늘은", "일요일")
# -> " ", " " 각각의 문자열을 한 줄로 출력하되 사이에 공백 한칸을 부여


# no.7 print()함수를 사용하여 다음과 같이 출력하세요.
#     naver;kakao;sk;samsung
# print('naver;kakao;sk;samsung')
# <sep 을 활용하는 방법>
# print('naver','kakao','sk','samsung', sep=(";"))


# no.8 print() 함수를 사용하여 다음과 같이 출력하세요.
#     naver/kakao/sk/samsung
# print('naver/kakao/sk/samsung')
# <sep 을 활용하는 방법>
# print('naver','kakao','sk','samsung', sep=("/"))


# no.9 다음 코드를 수정하여 줄바꿈 없이 출력하세요. (힌트: end='') print 함수는 두번 사용해야 하고, 세미콜론(;)은 한줄에 여러개의 명령을 작성하기 위해 사용합니다.
# print("first", end=" ");print("second")
# <end="" 에 임의의 값을 넣은 경우>
# print("first", end=" -> ");print("second")


# no.10 5/3의 결과를 화면에 출력하세요
# print(5/3)





# @@@02.파이썬 변수@@@
# ??바인딩 = 시각별로 자료를 구체적 정의해주는것??

# no.11 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
# SamsungElectronics = 50000
# myStock = 10
# myTEA = SamsungElectronics*myStock        #Total Evaluation Amount: 총 평가금액
# print(myTEA)


# no.12 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER등을 바인딩해보세요.
#     항목    |   값  
#   시가 총액    298조
#    현재 가    50,000원
#      PER       15.79
# MC = 298000000000000      #Market Capitalization: 시가총액
# CP = 50000                #Current Price: 현재가격
# PER = 15.79               #Price Earning Ratio: 주가/주당 순이익 을 나타내는 수익성 지표
# print(MC, type(MC))
# print(CP, type(CP))
# print(PER, type(PER))


# no.13 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
# s = "hello"
# t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# ex) hello! python

# <첫번째 멍청한 시도>
# print('s! '+'t')
# 결과값: s! t
# ... 조금 생각해보니 당연한 결과

# <두번쨰 시도>
# print(s+'! '+t)
# 결과값: hello! python
# Ez


# no.14 아래 코드의 실행 결과를 예상해보세요.
# print(2+2*3)
# 단순 연산만 놓고보면 8 아님? 응 맞네 ㅋ


# no.15 type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128숫자가 바인딩돼 있어 type함수가 int(정수)형 임을 알려줍니다.
# ex) a = 128
#     print(type(a))
#     <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
# a = "132"
# print(type(a))

# <예상>
# 문자열 형식(" ")으로 바인딩 되었으니 str 같은거 나오지 않을까?
# -> 아직까진 very EZ


# no.16 문자열 '720'을 정수형으로 변환해보세요.
# num_str = "720"

# <My answer>
# a = int(num_str)
# print(a)

# 답지에는 정수형 변환 인증도 하라고하는군요..그렇다면
# print(a, type(a))


# no.17 정수 100을 문자열 '100'으로 변환해보세요.
# num = 100

# a = str(num)
# print(a)
# 이렇게만 하니 100은 나오는데 이게 문자열인지 알수가없어서 16번처럼 함
# print(a, type(a))


# no.18 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
# a = "15.79"
# b = float(a)
# print(b, type(b))


# no.19 year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환 한 후 최근 3년의 연도를 화면에 출력해보세요.
# year = "2020"
# a = int(year)

# print(a-3)
# print(a-2)
# print(a-1)
# 사실 최근 3년의 연도라는말이 잘 이해가 안되서 답지를 아주 잠시 참조했습니다.. ㅈㅅ;;


# no.20 에어컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액을 계산한 후 이를 화면에 출력해보세요.
# monthly = 48584
# IP = 36  #Installment Period: 할부기간
# Total = monthly * IP
# print(Total)





# @@@03.파이썬 문자열@@@
# no.21 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# letters = 'python'
# 실행 예: p t
# print(letters[0], letters[2])


# no.22 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요
# license_plate = "24가 2210"
# 실행 예: 2210
# print(license_plate.split()[1])


# no.23 아래의 문자열에서 '홀'만 출력하세요
# string = "홀짝홀짝홀짝"
# 실행 예: 홀홀홀
# print(string[::2])


# no.24 문자열을 거꾸로 뒤집어 출력하세요.
# string = "PYTHON"
# 실행 예: NOHTYP
# 리스트 형식이었다면 reverse를 쓸 수도있었겠으나 단순 문자열인경우 아래와 같이 사용
# print(string[::-1])


# no.25 아래의 전화번호에서 하이푼('-')을 제거하고 출력하세요.
# phone_number = "010-1111-2222"
# 실행 예: 010 1111 2222
# print(phone_number.replace("-"," "))


# no.26 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요
# 실행 예: 01011112222
# #이딴 문제를 왜낸거지..
# print(phone_number.replace("-",""))


# no.27 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# url = "http://sharebook.kr"
# 실행 예: kr
# print(url.split('.')[1])


# no.28 아래 코드의 실행 결과를 예상해보세요.
# lang = 'python'
# lang[0] = 'P'
# print(lang)

# <예상>
# 처음엔 아무생각없이 p가 대문자 P로 바뀌어 출력될 거라 생각했으나 답지보고 아차 함..

# <결과>
# 당연히도 문자열은 수정이 안되므로 에러발생


# no.29 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요
# string = 'abcdfe2a354a32a'
# 실행 예: Abcdfe2A354A32A

# print(string.replace("a","A"))


# no.30 아래 코드의 실행 결과를 예상해보세요
# string = 'abcd'
# string.replace('b', 'B')
# print(string)

# <예상>
# string.replace를 담은 변수가 따로 없으니, 이대로면 문자열을 변경해달란 소리가 되므로 어림X

# <결과>
# 역시나 그대로 abcd 출력


# no.31 아래 코드의 실행 결과를 예상해보세요
# a = "3"
# b = "4"
# print(a+b)
# <예상>
# 34 나오지않을까
# <결과>
#당연하지 뭘..


# no.32 아래 코드의 실행 결과를 예상해보세요
# print("Hi" * 3)
# <예상>
# HiHiHi
# <결과>
#이것도 뭐..ㅋㅋ


# no.33 화면에 '-'를 80개 출력하세요.
# print('-' * 80)


# no.34 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# t1 = 'python'
# t2 = 'java'

# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예: python java python java python java python java

# print((t1 + " " + t2 + " ")*4)


# no.35 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요

# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# 실행 예:
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

# print("이름: %s 나이: %d" % (name1, age1))
# print("이름: %s 나이: %d" % (name2, age2))


# no.36 문자열의 format() 메서드를 사용해서 35번 문제를 다시 풀어보세요
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13

# 실행 예:
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))


# no.37 파이썬 3.6부터 지원하는 f-string을 사용해서 35번 문제를 다시 풀어보세요

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")


# no.38 삼성전자의 상장 주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요
# 상장주식수 = "5,969,782,550"
# 상장주식수 = int(상장주식수.replace(",",""))
# print(상장주식수, type(상장주식수))


# no.39 다음과 같은 문자열에서 '2020/03'만 출력하세요
# 분기 = "2020/03(E) (IFRS연결)"

# print(분기[:7])


# no.40 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
# data = "   삼성전자   "

# print(data.strip())


# no.41 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요
# ticker = "btc_krw"

# print(ticker.upper())


# no.42 다음과 같은 문자열이 있을 때 이를 소문자 brc_krw로 변경하세요
# ticker = "BTC_KRW"

# print(ticker.lower())


# no.43 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요
# a = 'hello'
# print(a.replace("h","H"))


# no.44 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요
# file_name = "보고서.xlsx"
# print(file_name.split('.')[1])
# print(file_name.endswith("xlsx"))


# no.45 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요
# file_name = "보고서.xlsx"
# print(file_name.endswith(("xlsx","xls")))


# no.46 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'으로 시작하는지 확인해보세요
# file_name = "2020_보고서.xlsx"

# print(file_name.startswith("2020"))


# no.47 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요
# a = "hello world"

# print(a.split())


# no.48 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요
# ticker = "btc_krw"

# print(ticker.split('_'))


# no.49 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요
# date = "2020-05-01"

# print(date.split('-'))


# no.50 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요
# data = "     039490"
# print(data.strip())



# @@@04.파이썬 리스트@@@
# no.51 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요 (순위 정보는 저장하지 않습니다)
#   순위  |  영화
#   1        닥터 스트레인지
#   2        스플릿
#   3        럭키

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']


# no.52 051의 movie_rank 리스트에 "배트맨"을 추가하라
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie_rank.append('배트맨')
# print(movie_rank)


# no.53 movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, '슈퍼맨')
# print(movie_rank)


# no.54 movie_rank 리스트에서 '럭키'를 삭제하라
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove('럭키') or del movie_rank[3]
# print(movie_rank)


# no.55 movie_rank 리스트에서 '스플릿'과 '배트맨'을 삭제하라
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2:]
# print(movie_rank)

# #예시 답안은 del movie_rank[2]를 두번 써주는 방법을 썼다
# #del 메서드는 하나의 인자를 삭제하고 다시 리스트에 담아주기 때문에
# #del movie_rank[2] -> del movie_rank[3]을 하면 마지막 값이 지워지지 않는다.
# #차라리 마지막요소부터 거꾸로 삭제하는 방법이 나음


# no.56 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고있는 langs 리스트를 만들어라
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# langs = lang1 + lang2
# print(langs)


# no.57 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
# nums = [1, 2, 3, 4, 5, 6, 7]

# print("max: ", max(nums))
# print("min: ", min(nums))


# no.58 다음 리스트의 합을 출력하라
# nums = [1, 2, 3, 4, 5]
# sum = 0
# for i in nums:
#     sum += i

# print(sum)

# #이딴짓 하지말고 그냥 print(sum(nums)) 를 쓰라고 합니다..낄


# no.59 다음 리스트에 저장된 데이터의 개수를 화면에 구하라
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

# print(len(cook))
# #처음에 cook.count() 같은걸 이용하는건가 생각하다 정신차림


# no.60 다음 리스트의 평균을 출력하라
# nums = [1, 2, 3, 4, 5]

# print(sum(nums) / len(nums))


# no.61 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
# price = ['20180728', 100, 130, 140, 150, 160, 170]

# print(price[1:])


# no.62 슬라이싱을 사용해서 홀수만 출력하라
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(nums[::2])


# no.63 슬라이싱을 사용해서 짝수만 출력하라
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(nums[1::2])


# no.64 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라
# nums = [1, 2, 3, 4, 5]

# print(nums[::-1])


# no.65 interest 리스트에는 아래의 데이터가 바인딩되어 있다
# interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라

# 출력 예시:
# 삼성전자 Naver

# print(interest[::2])
# print(interest[0], interest[2])


# no.66 interest 리스트에는 아래의 데이터가 바인딩되어 있다
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라

# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우

# print(" ".join(interest))


# no.67 interest 리스트에는 아래의 데이터가 바인딩되어 있다
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라

# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

# print("/".join(interest))


# no.68 interest 리스트에는 아래의 데이터가 바인딩되어 있다
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우

# print("\n".join(interest))


# no.69 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다
# string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라

# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']

# interest = string.split("/")
# print(interest)


# no.70 리스트에 있는 값을 오름차순으로 정렬하세요
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)
# print(sorted(data))





# @@@05.파이썬 튜플@@@
# no.71 my_variable 이름의 비어있는 튜플을 만들어라
# my_variable = ()

# print(type(my_variable))


# no.72 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라 (순위 정보는 저장하지 않는다)
# movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

# print(movie_rank)


# no.73 숫자 1 이 저장된 튜플을 생성하라
# a = (1,)

# #단순히 a = (1) 이라고 저장하면 정수형 타입으로 인식, 튜플로 저장하기 위해선 자료값이 하나이더라도 반드시 (1, )처럼 ,를 써줘야함
# print(type(a))


# no.74 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라
# t = (1, 2, 3)
# t[0] = 'a'

## 튜플은 선언된 변수 내부의 자료값을 변경할 수 없음


# no.75 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4

# print(type(t))
# #원칙적으로 튜플은 () 괄호를 써야 하지만 사용자 편의를 위해 ()를 생략하고 선언할 수 있다고 함


# no.76 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라
# t = ('a', 'b', 'c')
#튜플은 내부 자료값을 변경 할 수 없기때문에 위와 같은 경우 변수를 새로 설정해줘야만 한다. 이 때 기존 튜플 자료들은 자동 삭제
# t = ('A', 'B', 'c')
# print(t)


# no.77 다음 튜플을 리스트로 변환하라
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# a = list(interest)
# print(a)


# no.78 다음 리스트를 튜플로 변경하라
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# a = tuple(interest)
# print(a)


# no.79 다음 코드의 실행 결과를 예상하라
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
#예상한대로


# no.80 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라
# a = tuple(range(2, 100, 2))
# print(a)






# @@@06. 파이썬 딕셔너리@@@
# no.81 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, x, y = scores
# print(valid_score)


# no.82 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
# x, y, *valid_score = scores
# print(valid_score)


# no.83 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
# x, *valid_score, y = scores
# print(valid_score)


# no.84 temp 이름의 비어있는 딕셔너리를 만들어라
# temp = {}


# no.85 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
# icecream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}


# no.86 85번 문제의의 딕셔너리에 아래 아이스크림 가격정보를 추가하라
#   이름  |  희망 가격
#  죠스바      1200
#  월드콘      1500
# icecream['죠스바'] = 1200
# icecream['월드콘'] = 1500
# print(icecream)


# no.87 다음 딕셔너리를 사용하여 메로나 가격을 출력하라
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# print("메로나 가격:", ice['메로나'])


# no.88 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# ice['메로나'] = 1300
# print(ice)


# no.89 다음 딕셔너리에서 메로나를 삭제하라
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# del ice['메로나']
# print(ice)


# no.90 다음 코드에서 에러가 발생한 원인을 설명하라.
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500}
# >> icecream['누가바']
# #누가바 라는 키값이 딕셔너리 안에 없는데 참조를 요청했기 때문. icecream.get('누가바')를 썻으면 에러가 아닌 None값 반환
# print(icecream.get('메로나'))


# no.91 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다
#   이름  |  가격  |  재고
#  메로나    300      20
#  비비빅    400       3
#  죠스바    250      100

# inventory = {'메로나': (300, 20), '비비빅': (400, 3), '죠스바': (250, 100)}
# print(inventory)


# no.92 inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# print(inventory['메로나'][0],"원")


# no.93 inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# print(inventory['메로나'][1],"개")


# no.94 inventory 딕셔너리에 아래 데이터를 추가하라.
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
#   이름  |  가격  |  재고
#  월드콘    500       7

# inventory['월드콘'] = [500, 7]
# print(inventory)


# no.95 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# keys = list(icecream.keys())
# print(keys)


# no.96 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# value_list = list(icecream.values())
# print(value_list)


# no.97 icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# value_list = icecream.values()
# total = sum(value_list)
# print(total)


# no.98 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)


# no.99 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys, vals))
# print(result)


# no.100 date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# close_table = dict(zip(date, close_price))
# print(close_table)