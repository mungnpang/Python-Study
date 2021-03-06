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





# @@@07.파이썬 분기문@@@
# no.101 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# -> bool


# no.102 아래 코드의 출력 결과를 예상하라
# print(3 == 5)
# -> False


# no.103 아래 코드의 출력 결과를 예상하라
# print(3 < 5)
# -> True


# no.104 아래 코드의 결과를 예상하라.
# x = 4
# print(1 < x < 5)
# -> True


# no.105 아래 코드의 결과를 예상하라.
# print ((3 == 3) and (4 != 3))
# -> True


# no.106 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# print(3 => 4)
# -> 얼핏보면 단순히 수식이 잘못되어서라고 볼수있겠지만 그런경우라면 False가 뜨지 에러가 뜨지않는다
#     => 연산자는 존재하지 않는 형태로서 >= 로 사용해야함


# no.107 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#     print("Hello World")
# -> 조건문의 결과가 False 기 때문에 어떤 결과값도 출력되지 않는다


# no.108 아래 코드의 출력 결과를 예상하라
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
# 조건문부가 False 기 때문에 else 구문에 있는 Hi, there만 출력


# no.109 아래 코드의 출력 결과를 예상하라
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")

# 예상 결과값)
# 1
# 2
# 4


# no.110 아래 코드의 출력 결과를 예상하라
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")

# 예상 결과값)
# 3
# 5


# no.111 사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.
# >> 안녕하세요
# 안녕하세요안녕하세요

# comment = input("인사를 남겨주세요:")
# print(comment*2)


# no.112 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
# >> 숫자를 입력하세요: 30
# 40

# count = int(input("숫자를 입력하세요:"))
# print(count + 10)


# no.113 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
# >> 30
# 짝수

# disc = int(input("숫자를 입력해주세요:"))
# if disc%2 == 0:
#     print("짝수")
# else:
#     print("홀수")


# no.114 사용자로부터 값을 입력받은 후 해당 값에 20을 더한 값을 출력하라. 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우 255를 출력해야 한다.
# >> 입력값: 200
# 출력값: 220
# >> 입력값: 240
# 출력값: 255

# num = int(input("숫자를 입력해주세요:"))
# add = 20
# if (num+add) > 255:
#     print("출력값:",255)
# else:
#     print("출력값:", num+add)


# no.115 사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 단 출력 값의 범위는 0~255이다.
# 예를 들어 결괏값이 0보다 작은 값이되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
# >> 입력값: 200
# 출력값: 180
# >> 입력값: 15
# 출력값: 0

# num = int(input("숫자를 입력해주세요:"))
# dif = 20
# if (num-dif) <= 0:
#     print("출력값:", 0)
# elif (num-dif) > 255:
#     print("출력값:", 255)
# else:
#     print("출력값:", num-dif)


# no.116 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# >> 현재시간:02:00
# 정각 입니다.
# >> 현재시간:03:10
# 정각이 아닙니다

# time = input("현재 시간을 입력해주세요:")
# disc = time.split(":")[1]
# if disc == "00":
#     print("정각 입니다")
# else:
#     print("정각이 아닙니다")


# no.117 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라.
#        포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = ["사과", "포도", "홍시"]
# >> 좋아하는 과일은? 사과
# 정답입니다.

# q = input("제가 좋아하는 과일은 뭘까요?:")
# if q in fruit:
#     print("정답입니다")
# else:
#     print("오답입니다")


# no.118 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면
#        '투자 경고 종목입니다' 를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# invest = input("어떤종목을 관리중이신가요?:")
# if invest in warn_investment_list:
#     print('투자 경고 종목입니다')
# else:
#     print("투자 경고 종목이 아닙니다")


# no.119 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리
#        키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 제가좋아하는계절은: 봄
# 정답입니다.

# q = input("제가 좋아하는 계절은?:")
# if q in fruit.keys():
#     print("정답입니다")
# else:
#     print("오답입니다")


# no.120 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리
#        값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 좋아하는과일은? 한라봉
# 오답입니다.

# q = input("제가 좋아하는 과일은?:")
# if q in fruit.values():
#     print("정답입니다")
# else:
#     print("오답입니다")


# no.121 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로,
#        대문자 일 경우, 소문자로 변경해서 출력하라.
# >> a
# A

# f = input("알파벳을 하나 입력해주세요:")
# if f.islower():
#     f = f.upper()
# else:
#     f = f.lower()

# print(f)


# no.122 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
#        사용자로부터 score를 입력받아 학점을 출력하라.

# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E

# score = int(input("당신의 점수는?:"))
# if 0 <= score <= 20:
#     print("grade is E")
# elif 20 < score <= 40:
#     print("grade is D")
# elif 40 < score <= 60:
#     print("grade is C")
# elif 60 < score <= 80:
#     print("grade is B")
# elif 80 < score <= 100:
#     print("grade is A")
# else:
#     print("잘못입력하셨습니다")


# no.123 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다.
#        사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

# 통화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171

# currency = input("입력:")
# c = currency.split(" ")
# if c[1] == "달러":
#     print(float(c[0])*1167,"원")
# elif c[1] == "엔":
#     print(float(c[0])*1.096,"원")
# elif c[1] == "유로":
#     print(float(c[0])*1268,"원")
# elif c[1] == "위안":
#     print(float(c[0])*171,"원")


# no.124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20

# num1 = int(input("input number1:"))
# num2 = int(input("input number2:"))
# num3 = int(input("input number3:"))
# print(max(num1,num2,num3))


# no.125 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터
#        휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.

# 번호	통신사
# 011 	SKT
# 016	    KT
# 019 	LGU
# 010	    알수없음

# dic = {'011':'SKT', '016':'KT', '019':'LGU', '010:':'알수없음'}
# phone_num = input("휴대전화 번호 입력:")
# tel = phone_num.split('-')[0]
# print("당신은 %s 사용자입니다." %(dic[tel]))


# no.126 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다.
#        예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.

# -	0	    1	    2	    3	    4	    5	    6	    7	    8	    9
# 01	강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구

# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라

# >> 우편번호: 01400
# 도봉구

# gangbuk = ['010', '011', '012']
# dobong = ['013', '014', '015']
# nowon = ['016', '017', '018', '019']

# post_num = list(input("우편번호:"))[:3]
# f = "".join(post_num)

# if f in gangbuk:
#     print("강북구")
# elif f in dobong:
#     print("도봉구")
# elif f in nowon:
#     print("노원구")


# no.127 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은
#        남자 2, 4는 여자를 의미한다. 사용자로부터 13자리의 주민등록번호를 입력
#        받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

# >> 주민등록번호: 821010-1635210
# 남자

# id = input("주민등록번호:")
# disc = id.split('-')[1][0]

# if disc == 1 or 3:
#     print("남자")
# elif disc == 2 or 4:
#     print("여자")
# else:
#     print("잘못입력하셨습니다")


# no.128 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
#        주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라

# 지역코드	출생지
# 00 ~ 08	    서울
# 09 ~ 12 	부산

# id = input("주민등록번호:")
# disc = id.split('-')[1][1:3]

# seoul = ['00', '01', '02', '03', '04', '05', '06', '07', '08']
# busan = ['09', '10', '11', '12']

# if disc in seoul:
#     print("서울")
# elif disc in busan:
#     print("부산")
# else:
#     print("잘못입력하셨습니다")


# no.129 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
#        먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다.
#        연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

#   8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5 
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4

# 위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다.
# 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.

# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.

# >> 주민등록번호: 821010-1635210
# 유효하지 않은 주민등록번호입니다. 

# id = input("주민등록번호:")
# disc = id.split('-')
# arr = "".join(disc)
# sup = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
# result = []

# for i in range(len(arr)-1):
#     result.append(int(arr[i])*sup[i])

# if (11-(sum(result)%11)) == arr[-1]:
#     print("유효한 주민등록번호 입니다")
# else:
#     print("유효하지 않은 주민등록번호 입니다")


# no.130 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.

# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저가의 차이를 변동폭으로 정의할 때
# (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

# Key Name	    Description
# opening_price	최근 24시간 내 시작 거래금액
# closing_price	최근 24시간 내 마지막 거래금액
# min_price	    최근 24시간 내 최저 거래금액
# max_price	    최근 24시간 내 최고 거래금액

# opn = float(btc['opening_price'])
# dif = float(btc['max_price'])-float(btc['min_price'])
# max = float(btc['max_price'])

# if (opn+dif) > max:
#     print("상승장")
# else:
#     print("하락장")





# @@@08.파이썬 반복문@@@
# no.131 or문의 실행결과를 예측하라.

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)

# 예상 답안)
# 사과
# 귤
# 수박


# no.132 for문의 실행결과를 예측하라.

# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print("#####")

# 예상답안)
#####
#####
#####


# no.133 다음 for 문과 동일한 기능을 수행하는 코드를 작성하세요.
# for 변수 in ["A", "B", "C"]:
#     print(변수)

# list = ["A", "B", "C"]
# for 변수 in list
#     print(변수)


# no.134 for문을 풀어서 동일한 동작을하는 코드를 작성하라.

# for 변수 in ["A", "B", "C"]:
#     print("출력:", 변수)

# ex)
# print("출력:", "A")
# print("출력:", "B")
# print("출력:", "C")


# no.135 for문을 풀어서 동일한 동작을 하는 코드를 작성하라.

# for 변수 in ["A", "B", "C"]:
#     b = 변수.lower()
#     print("변환:", b)

# print("변환:", "a")
# print("변환:", "b")
# print("변환:", "c")


# no.136 다음 코드를 for문으로 작성하라.
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)

# for i in range(1,4):
#     print(10*i)


# no.137 다음 코드를 for문으로 작성하라.
# print(10)
# print(20)
# print(30)

# for i in range(1,4):
#     print(10*i)


# no.138 다음 코드를 for문으로 작성하라.
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")

# for i in range(1,4):
#     print(10*i)
#     print("-------")


# no.139 다음 코드를 for문으로 작성하라.
# print("++++")
# print(10)
# print(20)
# print(30)

# print("++++")
# for i in range(1,4):
#     print(10*i)


# no.140 다음 코드를 for문으로 작성하라.
# print("-------")
# print("-------")
# print("-------")
# print("-------")

# for i in range(4):
#     print("-------")


# no.141 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된
# 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.

# 리스트 = [100, 200, 300]
# 110
# 210
# 310

# for i in 리스트:
#     print(i+10)


# no.142 for 문을 사용해서 리스트에 저장된 값을 다음과 같이 출력하라.

# 리스트 = ["김밥", "라면", "튀김"]
# 오늘의 메뉴: 김밥
# 오늘의 메뉴: 라면
# 오늘의 메뉴: 튀김

# text = "오늘의 메뉴:"

# for i in 리스트:
#     print(text, i)


# no.143 리스트에 주식 종목이름이 저장돼 있다.

# 리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
# 저장된 문자열의 길이를 다음과 같이 출력하라.
# 6
# 4
# 4

# for i in 리스트:
#     print(len(i))


# no.144 리스트에는 동물이름이 문자열로 저장돼 있다.

# 리스트 = ['dog', 'cat', 'parrot']
# 동물 이름과 글자수를 다음과 같이 출력하라.
# dog 3
# cat 3
# parrot 6

# for i in 리스트:
#     print(i, len(i))


# no.145 리스트에 동물 이름 저장돼 있다.

# 리스트 = ['dog', 'cat', 'parrot']
# for문을 사용해서 동물 이름의 첫 글자만 출력하라.
# d
# c
# p

# for i in 리스트:
#     print(i[0])


# no.146 리스트에는 세 개의 숫자가 바인딩돼 있다.

# 리스트 = [1, 2, 3]
# for문을 사용해서 다음과 같이 출력하라.
# 3 x 1
# 3 x 2
# 3 x 3

# default = "3 x"
# for i in 리스트:
#     print(default, i)


# no.147 리스트에는 세 개의 숫자가 바인딩돼 있다.
# 리스트 = [1, 2, 3]
# for문을 사용해서 다음과 같이 출력하라.
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9

# a = 3
# for i in 리스트:
#     print(a,"x",i,"=",(a*i))


# no.148 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 나
# 다
# 라

# a = 리스트[1:]
# for i in a:
#     print(i)


# no.149 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 가
# 다

# a = 리스트[::2]
# for i in a:
#     print(i)


# no.150 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.
# 라
# 다
# 나
# 가

# for i in 리스트[::-1]:
#     print(i)


# no.151 리스트에는 네 개의 정수가 저장돼 있다.
# 리스트 = [3, -20, -3, 44]

# for문을 사용해서 리스트의 음수를 출력하라.
# -20
# -3

# for i in 리스트:
#     if i < 0:
#         print(i)


# no.152 for문을 사용해서 3의 배수만을 출력하라.
# 리스트 = [3, 100, 23, 44]
#>>> 3

# for i in 리스트:
#     if i%3 == 0:
#         print(i)


# no.153 리스트에서 20 보다 작은 3의 배수를 출력하라
# 리스트 = [13, 21, 12, 14, 30, 18]
# 12
# 18

# for i in 리스트:
#     if i < 20 and i%3 == 0:
#         print(i)


# no.154 리스트에서 세 글자 이상의 문자를 화면에 출력하라
# 리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language

# for i in 리스트:
#     if len(i) >= 3:
#         print(i)


# no.155 리스트에서 대문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
# A
# D

# for i in 리스트:
#     if i.isupper():
#         print(i)


# no.156 리스트에서 소문자만 화면에 출력하라.
# 리스트 = ["A", "b", "c", "D"]
# b
# c

# for i in 리스트:
#     if i.islower():
#         print(i)


# no.157 이름의 첫 글자를 대문자로 변경해서 출력하라.
# 리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot

# for i in 리스트:
#     print(i.capitalize())


# no.158 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro

# for i in 리스트:
#     print(i.split('.')[0])


# no.159 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h

# for i in 리스트:
#     if i.split('.')[1] == 'h':
#         print(i)


# no.160 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
# define.h

# for i in 리스트:
#     if i.split('.')[1] == 'h' or i.split('.')[1] == 'c':
#         print(i)


# no.161 for문과 range 구문을 사용해서 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램을 작성하라.
# for i in range(100):
#     print(i)


# no.162 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
# 2002
# 2006
# 2010
# ...
# 2042
# 2046
# 2050

# for year in range(2002, 2051, 4):
#     print(year)


# no.163 1부터 30까지의 숫자 중 3의 배수를 출력하라.
# 3 
# 6 
# 9 
# 12 
# 15 
# 18 
# 21 
# 24 
# 27 
# 30

# for i in range(3,31,3):
#     print(i)


# no.164 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.
# for i in range(99,0,-1):
#     print(i)


# no.165 for문을 사용해서 아래와 같이 출력하라.
# 0.0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# ...
# 0.9

# for i in range(10):
#     print(float(i/10))


# no.166 구구단 3단을 출력하라.
# 3x1 = 3
# 3x2 = 6
# 3x3 = 9
# 3x4 = 12
# 3x5 = 15
# 3x6 = 18
# 3x7 = 21
# 3x8 = 24
# 3x9 = 27

# base = "3 x"

# for i in range(1,10):
#     print(base,i,"=",3*i)


# no.167 구구단 3단을 출력하라. 단 홀수 번째만 출력한다.
# 3x1 = 3
# 3x3 = 9
# 3x5 = 15
# 3x7 = 21
# 3x9 = 27

# base = "3 x"

# for i in range(1,10, 2):
#     print(base,i,"=",3*i)


# no.168 1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# 합 : 55

# sum = 0
# for i in range(1,11):
#     sum += i

# print(sum)


# no.169 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# 합: 25

# sum = 0
# for i in range(1,11,2):
#     sum += i

# print(sum)


# no.170 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.
# result = 1
# for i in range(1,11):
#     result *= i

# print(result)


# no.171 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 32100
# 32150
# 32000
# 32500

# for i in range(len(price_list)):
#     print(price_list[i])


# no.172 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500

# for i in range(len(price_list)):
#     print(i, price_list[i])


# no.173 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 3 32100
# 2 32150
# 1 32000
# 0 32500

# for i in range(len(price_list)):
#     print((3-i), price_list[i])


# no.174 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500

# for i in range(1,len(price_list)):
#     print((90+10*i), price_list[i])


# no.175 my_list를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라"]
# 가 나
# 나 다
# 다 라

# for i in range(len(my_list)-1):
#     print(my_list[i], my_list[i+1])


# no.176 리스트를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라", "마"]
# 가 나 다
# 나 다 라
# 다 라 마

# for i in range(len(my_list)-2):
#     print(my_list[i],my_list[i+1],my_list[i+2])


# no.177 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가

# for i in range(len(my_list)-1,0,-1):
#     print(my_list[i], my_list[i-1])


# no.178 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
# my_list = [100, 200, 400, 800]
# 예를들어 100을 기준으로 우측에 위치한 200과의 차분 값를 화면에 출력하고, 200을 기준으로 우측에 위치한 400과의 차분값을 화면에 출력한다. 이어서 400을 기준으로 우측에 위치한 800과의 차분값을 화면에 출력한다.
# 100
# 200
# 400

# for i in range(len(my_list)-1):
#     print(my_list[i+1] - my_list[i])


# no.179 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
# my_list = [100, 200, 400, 800, 1000, 1300]
# 첫 번째 줄에는 100, 200, 400의 평균값이 출력된다. 두 번째 줄에는 200, 400, 800의 평균값이 출력된다. 같은 방식으로 나머지 데이터의 평균을 출력한다.
# 233.33333333333334
# 466.6666666666667
# 733.3333333333334
# 1033.3333333333333

# for i in range(len(my_list)-2):
#     print((my_list[i]+my_list[i+1]+my_list[i+2])/3)


# no.180 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]

# volatility = []
# for i in range(len(high_prices)):
#     volatility.append(high_prices[i]-low_prices[i])

# print(volatility)


# no.181 아래 표에서 하나의 행을 하나의 리스트로, 총 3개의 리스트를 갖는 이차원 리스트 apart를 정의하라.
# 101호	102호
# 201호	202호
# 301호	302호

# apart = [['101호', '102호'], ['201호', '202호'], ['301호', '302호']]


# no.182 아래 표에서 하나의 열을 하나의 리스트로, 총 2개의 리스트를 갖는 이차원 리스트 stock을 정의하라.
# 시가	종가
# 100 	80
# 200	    210
# 300 	330

# stock = [['시가',100,200,300], ['종가',80,210,330]]


# no.183 아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.
# 시가	종가
# 100 	80
# 200	    210
# 300	    330

# stock = {'시가':[100,200,300], '종가':[80,210,330]}


# no.184 아래 표를 stock 이라는 이름의 딕셔너리로 표현하라. 날짜를 key로 저장하고, 나머지 같은 행의 데이터를 리스트로 저장해서 value로 저장한다. 첫 열이 날짜이다.
# 10/10	80	110	70	90
# 10/11	210	230	190	200

# stock = {'10/10':[80,110,70,90], '10/11':[210,230,190,200]}


# no.185 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호

# for i in apart:
#     for j in i:
#         print(j,"호")


# no.186 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 301 호
# 302 호
# 201 호
# 202 호
# 101 호
# 102 호

# A1)
# for i in apart[::-1]:
#     for j in i:
#         print(j,"호")

# A2)
# for i in range((len(apart)-1),-1,-1):
#     for j in apart[i]:
#         print(j,"호")


# no.187 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 302 호
# 301 호
# 202 호
# 201 호
# 102 호
# 101 호

# for i in apart[::-1]:
#     for j in i[::-1]:
#         print(j,"호")


# no.188 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# -----
# 102 호
# -----
# 201 호
# -----
# 202 호
# -----
# 301 호
# -----
# 302 호
# -----

# for i in apart:
#     for j in i:
#         print(j,"호")
#         print('-'*5)


# no.189 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# -----
# 201 호
# 202 호
# -----
# 301 호
# 302 호
# -----

# for i in apart:
#     for j in i:
#         print(j,"호")
#     print('-'*5)


# no.190 리스트에 저장된 데이터를 아래와 같이 출력하라.
# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# -----

# for i in apart:
#     for j in i:
#         print(j,"호")

# print('-'*5)


# no.191 data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.

# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]

# 수수료를 0.014 %로 가정할 때, 각 가격에 수수료를 포함한 가격을 한라인에 하나씩 출력하라.
# 2000.28
# 3050.427
# 2050.2870000000003
# ...

# for i in data:
#     for j in i:
#         print(j*1.00014)


# no.192 191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.
# 2000.28
# 3050.427
# 2050.2870000000003
# 1980.2772
# ----
# 7501.05
# 2050.2870000000003
# 2050.2870000000003
# 1980.2772
# ----
# 15452.163
# 15052.107
# 15552.177
# 14902.086000000001
# ----

# for i in data:
#     for j in i:
#         print(j*1.00014)
#     print('-'*4)


# no.193 192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.
# >> print(result)
# [2000.28, 3050.427, 2050.2870000000003, 1980.2772, 7501.05, 2050.2870000000003, 2050.2870000000003, ...]

# result = []
# for i in data:
#     for j in i:
#         result.append(j*1.00014)

# print(result)


# no.194 191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.
# >> print(result)
# [
#  [2000.28, 3050.427, 2050.2870000000003, 1980.2772],
#  [7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772],
#  [15452.163, 15052.107, 15552.177, 14902.086000000001]
# ]

# result = []
# for i in data:
#     temp = []
#     for j in i:
#         temp.append(j*1.00014)
#     result.append(temp)

# print(result)


# no.195 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 화면에 종가데이터를 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 100
# 190
# 310

# for i in ohlc[1:]:
#     print(i[-1])


# no.196 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 150원보다 큰경우에만 종가를 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 190
# 310

# for i in ohlc[1:]:
#     if i[-1] >= 150:
#         print(i[-1])


# no.197 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 종가가 시가 보다 크거나 같은 경우에만 종가를 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 100
# 310

# for i in ohlc[1:]:
#     if i[-1] >= i[0]:
#         print(i[-1])


# no.198 ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장돼 있다. 고가와 저가의 차이를 변동폭으로 정의할 때 변동폭을 volatility 이름의 리스트에 저장하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# >> print(volatility)
# [40, 30, 10]

# volatility = []
# for i in ohlc[1:]:
#     volatility.append(i[1]-i[2])

# print(volatility)


# no.199 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 종가가 시가보다 높은 날의 변동성 (고가 - 저가)을 화면에 출력하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 종가가 시가보다 높은 거래일의 OHLC는 [300, 310, 300, 310] 이다. 따라서 이 거래일의 변동성은 10 (310 - 300)이다.
# 10

# for i in ohlc[1:]:
#     if i[-1] > i[0]:
#         print(i[1]-i[-2])


# no.200 리스트에는 3일 간의 ohlc 데이터가 저장돼 있다. 시가에 매수해서 종가에 매도 했을 경우 총 수익금을 계산하라.
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# 1일차 수익 0원 (100 - 100), 2일차 수익 -10원 (190 - 200), 3일차 수익 10원 (310 - 300) 이다.
#>>> 0
# profit = 0
# for i in ohlc[1:]:
#     profit += (i[-1]-i[0])

# print(profit)





# @@@09.파이썬 함수@@@
# no.201 "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
# def print_coin():
#     print("비트코인")


# no.202 201번에서 정의한 함수를 호출하라.
# print_coin()


# no.203 201번에서 정의한 print_coin 함수를 100번호출하라.
# for i in range(100):
#     print_coin()


# no.204 "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
# def print_coins():
#     for i in range(100):
#         print("비트코인")


# no.205 아래의 에러가 발생하는 이유에 대해 설명하라.
# hello()
# def hello():
#     print("Hi")

# >>> 기본적으로 모든코드는 위에서부터 순차적으로 번역/이해되는데
#     함수 선언보다 호출이 먼저작성 되었으므로 오류 발생


# no.206 아래 코드의 실행 결과를 예측하라.
# def message():
#     print("A")
#     print("B")

# message()
# print("C")
# message()

# A
# B
# C
# A
# B


# no.207 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")

# def message() :
#     print("B")

# print("C")
# message()

# A
# C
# B


# no.208 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()

# A
# C
# B
# E
# D


# no.209 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")

# def message2():
#     print("B")
#     message1()

# message2()

# B
# A
#message2 함수 안에 message1의 호출을 담아놨으므로 message2를 호출하면 BA 순으로 출력


# no.210 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")

# def message2():
#     print("B")

# def message3():
#     for i in range (3):
#         message2()
#         print("C")
#     message1()

# message3()

# B
# C
# B
# C
# B
# C
# A


# no.211 함수의 호출 결과를 예측하라.
# def 함수(문자열):
#     print(문자열)

# 함수("안녕")
# 함수("Hi")

# >>>
# "안녕"
# "Hi"


# no.212 함수의 호출 결과를 예측하라.
# def 함수(a, b):
#     print(a + b)

# 함수(3, 4)
# 함수(7, 8)

# >>>
# 7
# 15


# no.213 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(문자열):
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'

# >>> 함수 정의 상 ()안에 어떤 문자열이 입력되어야 실행이 가능한데
#     아무런 값을 넣어주지않아 에러 발생


# no.214 아래와 같은 에러가 발생하는 원인을 설명하라.

# def 함수(a, b):
#     print(a + b)

# 함수("안녕", 3)
# TypeError: must be str, not int

# >>> 함수를 정의할 때 가변인자 간의 합연산을 지시했는데 각 인자의
#     자료형이 달라서 연산이 불가능하다 (둘 다 숫자 or 둘 다 문자여야함)


# no.215 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# def print_with_smile (str):
#     print (str + ":D")


# no.216 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
# >>> print_with_smile("안녕하세요")


# no.217 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
# def print_upper_price(crt_price):
#     print(crt_price * 1.3)


# no.218 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
# def print_sum(a,b):
#     print(a + b)


# no.219 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75

# def print_arithmetic_operation(a, b):
#     print(a,'+',b,'=',a+b)
#     print(a,'-',b,'=',a-b)
#     print(a,'*',b,'=',a*b)
#     print(a,'/',b,'=',a/b)


# no.220 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
# def print_max(a,b,c):
#     if a >= b:
#         if a >= c:
#             print(a)
#         else:
#             print(c)
#     else:
#         if b >= c:
#             print(b)
#         else:
#             print(c)


# no.221 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# print_reverse("python")
# nohtyp

# def print_reverse(string):
#     print(string[::-1])

# print_reverse('python')


# no.222 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# print_score ([1, 2, 3])
# 2.0

# def print_score(list):
#     print(sum(list)/len(list))

# print_score([1, 2, 3])


# no.223 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12

# def print_even(list):
#     for i in list:
#         if i%2 == 0:
#             print(i)


# no.224 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별

# def print_keys(dict):
#     for i in dict.keys():
#         print(i)

# print_keys ({"이름":"김말똥", "나이":30, "성별":0})


# no.225 my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.

# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]

# def print_value_by_key(my_dict, key):
#     print(my_dict[key])

# print_value_by_key  (my_dict, "10/26")


# no.226 print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸

# def print_5xn(string):
#     line_num = int(len(string)/5)
#     for i in range(line_num + 1):
#         print(string[(i*5):(i*5)+5])

# print_5xn("아이엠어보이유알어걸")


# no.227 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸

# def print_mxn(string, num):
#     line_num = int(len(string) / num)
#     for i in range(line_num + 1) :
#         print(string[(i*num):(i*num)+num])

# print_mxn("아이엠어보이유알어걸", 3)


# no.228 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)
# 1000000

# def calc_monthly_salary(amount):
#     print(int(amount/12))

# calc_monthly_salary(12000000)


# no.229 아래 코드의 실행 결과를 예측하라.
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(a=100, b=200)

# >>>
# 왼쪽: 100
# 오른쪽: 200


# no.230 아래 코드의 실행 결과를 예측하라.
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(b=100, a=200)

# >>>
# 왼쪽: 200
# 오른쪽: 100


# no.231 아래 코드를 실행한 결과를 예상하라.
# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result)

# >>> 처음에는 당연히 4가 나오지라고 생각했는데 답지를 보고 아차 싶었다
#     변수 result를 함수 외에서는 정의하지 않았으므로 에러가 뜨는것...
#     result를 함수밖에서 별도로 정의해주거나 return형식으로 값을 출력해야한다


# no.232 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com

# def make_url(domain):
#     url = f'www.{domain}.com'
#     print(url)

# make_url("naver")


# no.233 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']

# def make_list(string):
#     list = []
#     for i in range(len(string)):
#         list.append(string[i])

#     return print(list)

# make_list('abcd')

#다 풀고나서 답지를 봤는데,, 좀 허무했다 ㅎㅎ.. return list(string) 한줄이면 될것을 난 왜...


# no.234 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]

# def pickup_even(list):
#     even_list = []
#     for i in list:
#         if i % 2 == 0:
#             even_list.append(i)

#     return print(even_list)


# no.235 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# convert_int("1,234,567")
# 1234567

# def convert_int(digit):
#     return print(int(digit.replace(',','')))

# convert_int("1,234,567")


# no.236 아래 코드의 실행 결과를 예측하라.
# def 함수(num):
#     return num + 4

# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# >>> a부터 차례대로 정수형 input, 정수형 output이 나오므로 크게 오류가 날것 같지는 않다
#     한줄씩 차례대로 결과값을 대입해 나가면 c에는 최종적으로 22가 바인딩 될것이다


# no.237 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4

# c = 함수(함수(함수(10)))
# print(c)

# >>> 매개 변수들을 쓰지 않았을 뿐 236번 문제와 같은 결과가 나올것이다


# no.238 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     return num * 10

# a = 함수1(10)
# c = 함수2(a)
# print(c)

# >>> 음.. 사실 계산이 어려운 문제는 사실상 없고 함수 진행 과정중에 오류가 날 
#     구석이 있는지를 찾는 과정인것 같다ㅋㅋㅋ 이대로면 c에는 140이 바인딩 될 것이다


# no.239 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)

# c = 함수2(10)
# print(c)

# >>> 조금 복잡해 보일 수 있어도 집중하면 간단하다. 함수2에서 10을 넣었을때의 결과를
#     다시 함수1에 넣어 돌리기만 하면되므로 사실상 함수1(12)와 같다. 결과는 16일듯


# no.240 아래 코드의 실행 결과를 예측하라.
# def 함수0(num) :
#     return num * 2

# def 함수1(num) :
#     return 함수0(num + 2)

# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)

# c = 함수2(2)
# print(c)

# >>> 이전 문제들과 마찬가지로 각 함수를 연쇄적으로 사용할 뿐 천천히만 생각하면 쉽다
#     함수2(2) -> 함수1(12) -> 함수0(14) -> c = 28 으로 바인딩 될것이다





# @@@10.파이썬 모듈@@@
# no.241 datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.

# import datetime

# now = datetime.datetime.now()
# print(now)


# no.242 datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.

# import datetime

# now = datetime.datetime.now()
# print(type(now))


# no.243 datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.

# import datetime

# now = datetime.datetime.now()

# for day in range(5, 0, -1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)


# no.244 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# ex) 18:35:01 

# import datetime

# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))


# no.245 datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.

# import datetime

# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))


# no.246 time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.

# import time
# import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)


# no.247 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.

# 1. import 모듈명
# -> 가장 기본적인 import 방식

# 2. from 모듈명 import 함수명
# -> 특정 모듈에서 일부 함수만을 가져오고 싶을 때 사용

# 3. from 모듈명 import *
# -> 특정 모듈에 있는 모든 함수를 가져올 때 사용

# 4. import 모듈명 as 내가 사용할 이름
# -> 가져온 모듈을 내가 사용하기 편한 이름으로 바꿔 쓰고 싶을때 사용
# ex) import combinations as C


# no.248 os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.

# import os
# ret = os.getcwd()
# print(ret, type(ret))


# no.249 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.

# import os
# os.rename("C:\\Users\\User\\Desktop\\sparta.txt", "C:\\Users\\User\\Desktop\\codingclub.txt")
# >>> 잘 모르겠당...


# no.250 numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.

# import numpy

# for i in numpy.arange(0, 5, 0.1):
#     print(i)





# @@@11.파이썬 클래스@@@
# no.251 클래스, 객체, 인스턴스에 대해 설명해봅시다.
# 클래스: 어떠한 객체를 정의하고 만들기위한 변수+메서드의 집합 / 틀에 비유
# 객체: 틀에 의해서 만들어진 하나의 와플 
# 인스턴스: 특정 객체가 어떤 클래스의 객체인지 관계를 중점으로 표현할때 사용, 부모-자식 / 클래스 - 인스턴스


# no.252 비어있는 사람 (Human) 클래스를 "정의" 해보세요.

# class Human():
#     pass


# no.253 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.

# class Human():
#     pass

# areum = Human()


# no.254 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.

# class Human():
#     def __init__(self):
#         print('응애응애')

# areum = Human()


# no.255 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("아름", 25, "여자")
# print(areum.name, areum.age, areum.sex)


# no.256 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.

# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("조아름", 25, "여자")
# print(f'이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}')


# no.257 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def who(self):
#         print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')

# areum = Human('조아름', 25, '여자')
# areum.who()


# no.258 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.

# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def who(self):
#         print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')

#     def setInfo(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human('모름', 25, '모름')
# areum.who()

# areum.setInfo('조아름', 25, '여자')
# areum.who()


# no.259 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.

# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def __del__(self):
#         print("나의 죽음을 알리지마라")

#     def who(self):
#         print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("아름", 25, "여자")
# del(areum)
# areum.who()


# no.260 아래와 같은 에러가 발생한 원인에 대해 설명하세요.

# class OMG:
#     def print():
#         print("Oh my god")

# mystock = OMG()
# mystock.print()    # OMG.print(mystock)

# >>>
# 클래스로 호출되어 불려갔을때 파라미터로 사용될 값이 없기때문에 문제 발생
# def print(self)로 바꿔주면 정상적으로 작동


# no.261 주식 종목에 대한 정보를 저장하는 Stock 클래스를 정의해보세요. 클래스는 속성과 메서드를 갖고 있지 않습니다.

# class Stock:
#     pass


# no.262 Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.

# class Stock():
#     def __init__(self,name,code):
#         self.name = name
#         self.code = code

# samsung = Stock('삼성전자', '005930')
# print (samsung.name, samsung.code)


# no.263 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.

# class Stock():
#     def __init__(self,name,code):
#         self.name = name
#         self.code = code

#     def set_name(self,name):
#         self.name = name

# a = Stock(None,None)
# print(a.name,a.code)
# a.set_name('삼성전자')
# print(a.name)


# no.264 객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.

# class Stock():
#     def __init__(self,name,code):
#         self.name = name
#         self.code = code

#     def set_name(self,name):
#         self.name = name

#     def set_code(self,code):
#         self.code = code

# a = Stock(None, None)
# a.set_code("005930")
# print(a.code)


# no.265 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.

# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def get_name(self):
#         return self.name

#     def get_code(self):
#         return self.code

# 삼성 = Stock("삼성전자", "005930")
# print(삼성.get_name(), 삼성.get_code())


# no.266 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입입니다.

# class Stock:
#     def __init__(self, name, code, PER, PBR, 배당수익률):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.배당수익률 = 배당수익률

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def get_name(self):
#         return self.name

#     def get_code(self):
#         return self.code


# no.267 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.

# class Stock:
#     def __init__(self, name, code, PER, PBR, 배당수익률):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.배당수익률 = 배당수익률

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def get_name(self):
#         return self.name

#     def get_code(self):
#         return self.code

# samsung = Stock('삼성전자','005930',15.79,1.33,2.83)
# print(samsung.name, samsung.code, samsung.PER, samsung.PBR, samsung.배당수익률)


# no.268 PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.

# class Stock:
#     def __init__(self, name, code, PER, PBR, dividend):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.dividend = dividend

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def set_PER(self, PER):
#         self.PER = PER

#     def set_PBR(self, PBR):
#         self.PBR = PBR

#     def set_dividend(self, dividend):
#         self.dividend = dividend


# no.269 267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.

# class Stock:
#     def __init__(self, name, code, PER, PBR, dividend):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.dividend = dividend

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def set_PER(self, PER):
#         self.PER = PER

#     def set_PBR(self, PBR):
#         self.PBR = PBR

#     def set_dividend(self, dividend):
#         self.dividend = dividend

# samsung = Stock('삼성전자','005930',15.79,1.33,2.83)
# print(samsung.PER)
# samsung.set_PER(12.75)
# print(samsung.PER)


# no.270 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요.
#        파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.

# class Stock:
#     def __init__(self, name, code, PER, PBR, dividend):
#         self.name = name
#         self.code = code
#         self.PER = PER
#         self.PBR = PBR
#         self.dividend = dividend

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def set_PER(self, PER):
#         self.PER = PER

#     def set_PBR(self, PBR):
#         self.PBR = PBR

#     def set_dividend(self, dividend):
#         self.dividend = dividend

# Samsung = Stock('삼성전자','005930',15.79,1.33,2.83)
# Hyundai = Stock('현대차','005380',8.70,0.35,4.27)
# LG = Stock('LG전자','066570',317.34,0.69,1.37)

# companies = [Samsung, Hyundai, LG]

# for company in companies:
#     print(company.code, company.PER)


# no.271 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다.
#        Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다.
#        은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.

# import random

# class Account():
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"
#         num1 = random.randint(0,999)
#         num2 = random.randint(0,99)
#         num3 = random.randint(0,999999)

#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        # self.account_number = f'{num1}-{num2}-{num3}'  # 001-01-000001

# jacob = Account("김재명", '10000원')
# print(jacob.name, jacob.balance, jacob.bank, jacob.account_number)


# no.272 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.

# import random

# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        # self.account_number = f'{num1}-{num2}-{num3}'  # 001-01-000001

#         Account.account_count += 1


# kim = Account("김민수", 100)
# print(Account.account_count)
# lee = Account("이민수", 100)
# print(Account.account_count)
# jacob = Account("김재명", '10000원')
# print(Account.account_count)


# no.273 Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.

# import random

# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = f'{num1}-{num2}-{num3}'  # 001-01-000001

#         Account.account_count += 1


#     def get_account_num(cls):
#         print(cls.account_count)


# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# jacob = Account("김재명", '10000원')
# jacob.get_account_num()


# no.274 Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.

# import random

# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = int(balance)
#         self.bank = "SC은행"

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = f'{num1}-{num2}-{num3}'  # 001-01-000001

#         Account.account_count += 1


#     def get_account_num(cls):
#         print(cls.account_count)

#     def deposit(self,balance):
#         if balance >= 1:
#             self.balance += int(balance)

# jacob = Account('재명','10000')
# jacob.deposit(50000)
# print(jacob.balance)


# no.275 Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.

# import random

# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = int(balance)
#         self.bank = "SC은행"

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
#         self.account_number = f'{num1}-{num2}-{num3}'  # 001-01-000001

#         Account.account_count += 1


#     def get_account_num(cls):
#         print(cls.account_count)

#     def deposit(self,balance):
#         if balance >= 1:
#             self.balance += int(balance)

#     def withdraw(self,amount):
#         if self.balance - amount >= 0:
#             self.balance -= amount
#         else:
#             print('한도 초과입니다')

# jacob = Account('재명','50000')
# jacob.withdraw(60000)
# print(jacob.balance)


# no.276 Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.

# 은행이름: SC은행
# 예금주: 파이썬
# 계좌번호: 111-11-111111
# 잔고: 10,000원

# import random


# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = f'{num1}-{num2}-{num3}'  # 001-01-000001
#         Account.account_count += 1

#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count

#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount

#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount
#         else:
#             print('한도 초과입니다')

#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)


# jacob = Account("재명", 10000)
# jacob.display_info()


# no.277 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.

# import random


# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.deposit_count = 0

#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1

#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count

#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount

#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)


#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount

#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)

# jacob = Account("재명", 10000)
# jacob.deposit(10000)
# jacob.deposit(10000)
# jacob.deposit(10000)
# jacob.deposit(5000)
# jacob.deposit(5000)
# print(jacob.balance)


# no.278 Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.

# import random

# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.deposit_count = 0
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1

#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count

#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount

#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)


#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount

#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)

# jacob = Account("재명", 50000)
# jin = Account("우진",100000)
# jun = Account("준", 70000)

# Accounts = [jacob,jin,jun]

# for account in Accounts:
#     account.display_info()


# no.279 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.

# import random


# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.deposit_count = 0

#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1

#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count

#     def deposit(self, amount):
#         if amount >= 1:
#             self.balance += amount

#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)


#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount

#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)

# jacob = Account("재명", 900000)
# jin = Account("우진",1000000)
# jun = Account("준", 7000000)

# Accounts = [jacob,jin,jun]

# for account in Accounts:
#     if account.balance >= 1000000:
#         account.display_info()


# no.280 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

# import random


# class Account:
#     # class variable
#     account_count = 0

#     def __init__(self, name, balance):
#         self.deposit_count = 0
#         self.deposit_log = []
#         self.withdraw_log = []

#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         # 3-2-6
#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
#         num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
#         num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
#         self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
#         Account.account_count += 1

#     @classmethod
#     def get_account_num(cls):
#         print(cls.account_count)  # Account.account_count

#     def deposit(self, amount):
#         if amount >= 1:
#             self.deposit_log.append(amount)
#             self.balance += amount

#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:         # 5, 10, 15
#                 # 이자 지금
#                 self.balance = (self.balance * 1.01)


#     def withdraw(self, amount):
#         if self.balance > amount:
#             self.withdraw_log.append(amount)
#             self.balance -= amount

#     def display_info(self):
#         print("은행이름: ", self.bank)
#         print("예금주: ", self.name)
#         print("계좌번호: ", self.account_number)
#         print("잔고: ", self.balance)

#     def withdraw_history(self):
#         for amount in self.withdraw_log:
#             print(f'출금내역: -{amount}')

#     def deposit_history(self):
#         for amount in self.deposit_log:
#             print(f'입금내역: +{amount}')


# jacob = Account("재명", 10000)

# jacob.deposit(10000)
# jacob.deposit(20000)
# jacob.deposit(30000)
# jacob.deposit_history()

# jacob.withdraw(10000)
# jacob.withdraw(20000)
# jacob.withdraw_history()


# no.281 다음 코드가 동작하도록 차 클래스를 정의하세요.
# >> car = 차(2, 1000)
# >> car.바퀴
# 2
# >> car.가격
# 1000

# class 차():
#         def __init__(self,바퀴,가격):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격

# car = 차(2, 1000)
# print(car.바퀴)
# print(car.가격)


# no.282 차 클래스를 상속받은 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.

# >> bicycle = 자전차(2, 100)
# >> bicycle.가격
# 100

# class 차():
#         def __init__(self,바퀴,가격):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격

# class 자전차(차):
#         def __init__(self,바퀴,가격):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격

# bicycle = 자전차(2, 100)
# print(bicycle.가격)


# no.284. 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.

# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.구동계
# 시마노

# class 차():
#         def __init__(self,바퀴,가격):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격

# class 자전차(차):
#         def __init__(self,바퀴,가격,구동계):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격
#                 self.구동계 = 구동계

# bicycle = 자전차(2, 100, '시마노')
# print(bicycle.구동계)


# no.285 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.

# >> car = 자동차(4, 1000)
# >> car.정보()
# 바퀴수 4
# 가격 1000

# class 차():
#         def __init__(self,바퀴,가격):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격

# class 자전차(차):
#         def __init__(self,바퀴,가격):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격

# class 자동차(차):
#         def __init__(self,바퀴,가격):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격

#         def 정보(self):
#                 print(f'바퀴수 {self.바퀴}')
#                 print(f'가격 {self.가격}')

# car = 자동차(4, 1000)
# car.정보()


# no.286 다음 코드가 동작하도록 자전차 클래스를 수정하세요.

# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100

# class 차():
#         def __init__(self,바퀴,가격,구동계):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격
#                 self.구동계 = 구동계

# class 자전차(차):
#         def __init__(self,바퀴,가격,구동계):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격
#                 self.구동계 = 구동계

#         def 정보(self):
#                 print(f'바퀴수 {self.바퀴}')
#                 print(f'가격 {self.가격}')

# bicycle = 자전차(2, 100, '시마노')
# bicycle.정보()


# no.287 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.

# >> bicycle = 자전차(2, 100, "시마노")
# >> bicycle.정보()
# 바퀴수 2
# 가격 100
# 구동계 시마노

# class 차():
#         def __init__(self,바퀴,가격,구동계):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격
#                 self.구동계 = 구동계

# class 자전차(차):
#         def __init__(self,바퀴,가격,구동계):
#                 self.바퀴= 바퀴
#                 self.가격 = 가격
#                 self.구동계 = 구동계

#         def 정보(self):
#                 print(f'바퀴수 {self.바퀴}')
#                 print(f'가격 {self.가격}')
#                 print(f'구동계 {self.구동계}')

# bicycle = 자전차(2, 100, '시마노')
# bicycle.정보()


# no.288 다음 코드의 실행 결과를 예상해보세요.

# class 부모:
#         def 호출(self):
#                 print("부모호출")

# class 자식(부모):
#         def 호출(self):
#                 print("자식호출")
        
# 나 = 자식()
# 나.호출()

# >>> '자식호출'이 출력될 것이다


# no.289 다음 코드의 실행 결과를 예상해보세요.

# class 부모:
#         def __init__(self):
#                 print("부모생성")

# class 자식(부모):
#         def __init__(self):
#                 print("자식생성")

# 나 = 자식()

# >>> '자식생성'이 호출될 것이다


# no.290 다음 코드의 실행 결과를 예상해보세요.

# class 부모:
#         def __init__(self):
#                 print("부모생성")

# class 자식(부모):
#         def __init__(self):
#                 print("자식생성")
#                 super().__init__()

# 나 = 자식()

# >>> '자식생성' 호출이후 super().__init__() <부모의 __init__ 함수>를 호출했으므로
#     '부모생성'을 마저 출력할 것이다


# no.291 바탕화면에 '매수종목1.txt' 파일을 생성한 후 다음과 같이 종목코드를 파일에 써보세요.

# 005930
# 005380
# 035420

# f = open("C:/Users/user/Desktop/매수종목1.txt", mode="wt", encoding="utf-8")
# f.write("005930\n")
# f.write("005380\n")
# f.write("035420")
# f.close()


# no.292 바탕화면에 '매수종목2.txt' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요.

# 005930 삼성전자
# 005380 현대차
# 035420 NAVER

# f = open("C:/Users/user/Desktop/매수종목2.txt", mode="wt", encoding="utf-8")
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER")
# f.close()


# no.293 바탕화면에 '매수종목.csv' 파일을 생성한 후 다음과 같이 종목코드와 종목명을 파일에 써보세요. 인코딩은 'cp949'를 사용해야합니다.

# >>> 내 답
# f = open("C:/Users/user/Desktop/매수종목.csv", mode="wt", encoding="cp949")
# f.write("종목명\t""종목코드\t""PER\n")
# f.write("삼성전자\t""005930\t""15.79\n")
# f.write("NAVER\t""035420\t""55.82")
# f.close()

# >>> 답안지
# import csv

# f = open("C:/Users/user/Desktop/매수종목.csv", mode="wt", encoding="cp949", newline='')
# writer = csv.writer(f)
# writer.writerow(["종목명", "종목코드", "PER"])
# writer.writerow(["삼성전자", "005930", 15.59])
# writer.writerow(["NAVER", "035420", 55.82])
# f.close()


# no.294 바탕화면에 생성한 '매수종목1.txt' 파일을 읽은 후 종목코드를 리스트에 저장해보세요.

# 005930
# 005380
# 035420

# f = open("C:/Users/user/Desktop/매수종목1.txt", encoding="utf-8")
# lines = f.readlines()   # python list

# codes = []
# for line in lines:
#     code = line.strip()  #'\n'
#     codes.append(code)

# print(codes)

# f.close()


# no.295 바탕화면에 생성한 '매수종목2.txt' 파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장해보세요. 종목명을 key로 종목명을 value로 저장합니다.

# 005930 삼성전자
# 005380 현대차
# 035420 NAVER

# f = open("C:/Users/user/Desktop/매수종목2.txt", encoding="utf-8")
# lines = f.readlines()

# data = {}
# for line in lines:
#     line = line.strip()     # '\n' 제거
#     k, v = line.split()
#     #print(k, v)
#     data[k] = v

# print(data)
# f.close()


# no.296 문자열 PER (Price to Earning Ratio) 값을 실수로 변환할 때 에러가 발생합니다. 예외처리를 통해 에러가 발생하는 PER은 0으로 출력하세요.

# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print(0)


# no.297 문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장해보세요.

# per = ["10.31", "", "8.00"]
# new_per = []
# for i in per:
#     try:
#         new_per.append(float(i))
#     except:
#         new_per.append(0)


# no.298 어떤 값을 0으로 나누면 ZeroDivisionError 에러가 발생합니다. try ~ except로 모든 에러에 대해 예외처리하지 말고 ZeroDivisionError 에러만 예외처리해보세요.

# try:
#     a = 7 / 0
# except ZeroDivisionError:
#     print("0으로 나누면 안되요")


# no.299 다음과 같은 코드 구조를 사용하면 예외 발생 시 에러 메시지를 변수로 바인딩할 수 있습니다.

# try:
#     실행코드
# except 예외 as 변수:
#     예외처리코드 

# 리스트의 인덱싱에 대해 에러를 출력해보세요.

# data = [1, 2, 3]
# for i in range(5)
#     print(data[i])

# data = [1, 2, 3]
# for i in range(5):
#     try:
#         print(data[i])
#     except IndexError as e:
#         print(e)


# no.300 파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.

# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드 


# 아래의 코드에 대해서 예외처리를 사용하고 try, except, else, finally
# 에 적당한 코드를 작성해봅시다. else와 finally는 적당한 문구를 print하시면 됩니다.

# per = ["10.31", "", "8.00"]

# for i in per:
#     print(float(per))

# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print(0)
#     else:
#         print("clean data")
#     finally:
#         print("변환 완료")

