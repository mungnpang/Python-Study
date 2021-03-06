#이름중 한글자를 지워 출석부 상 가장 앞쪽으로 갈 수 있게 만들어주기 feat.Zenon
# https://level.goorm.io/exam/49069/%EC%B6%9C%EC%84%9D%EB%B6%80/quiz/1

# name = input('type your name: ').lower()
# f_index = name[0]
# s_index = name[1]
# if f_index >= s_index:
#     print(name[1:])
# else:
#     newname = name.replace(max(name),"")
#     print(newname)



#배열 array의 i~j번째 숫자까지 자르고 정렬하여 k번째의 수를 구하기
# https://programmers.co.kr/learn/courses/30/lessons/42748

# A1)
# def solution(array, commands):
#     answer = []
#     for x in commands:
#         func = array[(x[0]-1):x[1]]
#         func.sort()
#         answer.append(func[x[2]-1])
#     return answer

# A2)
# def solution(array, commands):
#     answer = []
#     for x in commands:
#         i,j,k = x
#         func = array[(i-1):j]
#         func.sort()
#         answer.append(func[k-1])
#     return answer



#서로 다른 인덱스에 있는 두개의 수를 뽑아 만들 수 있는 모든 수를 오름차순으로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             if i != j:
#                 answer.append(numbers[i] + numbers[j])
            
#     answer = list(set(answer))
#     answer.sort()

#     return answer



#카카오게임 각 단계별 실패율 구하기
# https://programmers.co.kr/learn/courses/30/lessons/42889

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]

# def solution(N, stages):
#     answer = []
#     fail_rate = {}
#     survivor = len(stages)
#     for i in range(1, N+1):
#         if survivor != 0:
#             fail_rate[i] = (stages.count(i) / survivor)
#             survivor -= stages.count(i)
#         else:
#             fail_rate[i] = 0

#     fail_rate = sorted(fail_rate.items(), key=lambda x: x[1], reverse=True)
#     for j in fail_rate:
#         answer.append(j[0])

#     return answer



#정규표현식을 활용한 신규아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

# import re

# new_id = "=.="
# new_id = new_id.lower()
# new_id = re.sub('[^-_.a-z0-9]', "", new_id)
# new_id = re.sub('[.]{2,}', ".", new_id)
# if new_id.startswith("."):
#     new_id = new_id[1:]
# if new_id == "":
#     new_id = "a"
# if len(new_id) >= 16:
#     new_id = new_id[:15]
# if new_id.endswith("."):
#     new_id = new_id[:-1]
# if len(new_id) <= 2:
#     while len(new_id) < 3:
#         new_id += new_id[-1]

# print(new_id)



#전화번호 뒷4자리를 제외하고 모두 *로 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948

# def solution(phone_number):
#     answer = list(phone_number)

#     for i in range(len(phone_number) - 4):
#         answer[i] = "*"
    
#     return ("".join(answer))



#0~9 범위내에서 없는 숫자를 찾아 모두 더한수 구하기
# https://programmers.co.kr/learn/courses/30/lessons/86051

# def solution(numbers):
#     answer = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
#     return sum(answer - set(numbers))



#시저암호 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12926

# s = "z Z z"
# n = 4
# answer = ""

# for i in s:
#     if i != ' ':
#         x = ord(i)
#         if x <= ord('Z'):
#             if (x+n) <= ord('Z'):
#                 answer += chr(x+n)
#             else:
#                 answer += chr(x+n-26)
#         elif (x+n) <= ord('z'):
#             answer += chr(x+n)
#         else:
#             answer += chr(x+n-26)
#     else:
#         answer += ' '

# print(answer)



#네오와 프로도의 영단어 카드게임. 문자열로 표현된 숫자들을 정수 형태로 변환
# https://programmers.co.kr/learn/courses/30/lessons/81301

# A1)
# s = "123"
# s.lower()

# s = s.replace("zero","0")
# s = s.replace("one","1")
# s = s.replace("two","2")
# s = s.replace("three","3")
# s = s.replace("four","4")
# s = s.replace("five","5")
# s = s.replace("six","6")
# s = s.replace("seven","7")
# s = s.replace("eight","8")
# s = s.replace("nine","9")
# print(s)

# A2)
# s = "one4seveneight"

# a = {'zero': '0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
# for key,value in a.items():
#     s = s.replace(key, value)
# print(s)



#우선순위 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

# priorities = [2, 1, 4, 2, 3]
# location = 3
# answer = 0
# count = 0
# p = {}

# for i in range(len(priorities)):
#     p[i+1] = priorities[i]

# all_values = p.values()

# while p.get(location+1) != max(all_values):
#     for i in p.copy():
#         if p.get(i) >= max(all_values):
#             p.pop(i)
#             count += 1
#             break
#         else:
#             x = p.pop(i)
#             p.update({i:x})

# while list(p.keys())[0] != (location+1):
#     for i in p.copy():
#         if p.get(i) == p.get(location+1):
#             p.pop(i)
#             count += 1
#             break
#         else:
#             x = p.pop(i)
#             p.update({i:x})
#             break
# else:
#     answer = count + 1

# print(answer)



#124 나라의 이상한 숫자
#https://programmers.co.kr/learn/courses/30/lessons/12899

# n = 17
# temp = []
# answer = ""

# while n >= 3:
#     if (n % 3) == 0:
#         temp.append(4)
#         n = int(n / 3) - 1
#     else:
#         temp.append(n%3)
#         n = int((n / 3))

# if n != 0:
#     temp.append(n)

# temp.reverse()
# answer = "".join(map(str,temp))

# print(answer)



#폰켓몬 최대로 얻기
# https://programmers.co.kr/learn/courses/30/lessons/1845

# nums = [3, 3, 3, 2, 2, 2]
# temp = set(nums)

# if len(temp) > (len(nums)/2):
#     answer = len(nums) / 2
# else:
#     answer = len(temp)

# print(answer)



#임의의 3개 수의 합중 소수의 갯수 구하기
# https://programmers.co.kr/learn/courses/30/lessons/12977

# from itertools import combinations

# def solution(nums):
#     answer = 0
#     temp = list(combinations(nums, 3))

#     for i in range(len(temp)):
#         temp[i] = sum(temp[i])

#     for i in temp:
#         count = 0
#         for j in range(2, i):
#             if i % j == 0:
#                 count += 1
#                 break
#         if count == 0:
#             answer += 1

#     return answer



#하샤드 수 판별식
# https://programmers.co.kr/learn/courses/30/lessons/12947

# def solution(x):
#     x_list = list(map(int, str(x)))
#     sum = 0

#     for i in x_list:
#         sum += i

#     if x % sum == 0:
#         answer = True
#     else:
#         answer = False
    
#     return answer



#공백을 제외한 단어 단위별로 짝수번째 글자는 대문자 홀수번째는 소문자로 출력하기
# https://programmers.co.kr/learn/courses/30/lessons/12930

# def solution(s):
#     count = 0
#     temp = []
#     for i in s:
#         if i == " ":
#             temp.append(" ")
#             count = 0
#         elif count%2 == 0:
#             temp.append(i.upper())
#             count += 1
#         else:
#             temp.append(i.lower())
#             count += 1

#     answer = ("".join(temp))

#     return answer



# 1~9까지의 오름차순으로 정리된 N개의 원소를 9~1로 내림차순 정렬하기 
# N = 9
# n = []
# for i in range (1,N+1):
#     n.append(str(i))

# temp = int("".join(n))
# answer = temp*8 + N

# print(answer)



# 정해진 예산 안에서 최대한 많은 부서에 예산 분배하기
# https://programmers.co.kr/learn/courses/30/lessons/12982

# def solution(d, budget):
#     temp = []
#     answer = 0
#     d.sort()

#     for i in d:
#         if (sum(temp)+i) > budget:
#             break
#         else:
#             temp.append(i)

#     answer = len(temp)
    
#     return answer



#행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

# def solution(arr1, arr2):
#     answer = []
#     for i in range(len(arr1)):
#         temp = []
#         for j in range(len(arr1[0])):
#             temp.append(arr1[i][j]+arr2[i][j])
#         answer.append(temp)

#     return answer



#공백 없애기
# https://level.goorm.io/exam/43259/%EA%B3%B5%EB%B0%B1-%EC%97%86%EC%95%A0%EA%B8%B0/quiz/1#

# user_input = input()
# answer = user_input.replace(" ","")
# print(answer)



# n번째 분수 찾기
# https://www.acmicpc.net/problem/1193

# x = int(input())
# n = 0
# while True:
#     y = n*(n+1)/2
#     if y >= x:
#         n -= 1
#         break
#     n += 1

# y = n*(n+1)/2
# gap = int(x - y)
# div = int(n + 2 - gap)
# if n%2 == 0:
#     answer = f'{div}/{gap}'
# else:
#     answer = f'{gap}/{div}'

# print(answer)



# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

# def solution(numbers):
#     dict = {}
#     answer = ''
#     for i,j in enumerate(numbers):
#         j = str(j)
#         dict[i] = (j*3)

#     sdict = sorted(dict.items(), reverse=True, key=lambda x:x[1])

#     for k in sdict:
#         answer += str(int(numbers[k[0]]))

#     if answer.count('0') == len(answer):
#         answer = '0'
#     return(answer)



#음양 더하기
# https://programmers.co.kr/learn/courses/30/lessons/76501

# absolutes = [4,7,12]
# signs = [True,False,True]

# answer = 0
# for i,j in enumerate(absolutes):
#     if signs[i] == True:
#         answer += j
#     else:
#         answer -= j
        
# print(answer)



#약수 구하기
# https://level.goorm.io/exam/43255/%EC%95%BD%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

# user_input = int(input())
# answer = ''
# for i in range(1, int(user_input)+1):
#     if user_input % i == 0:
#         answer += str(i)+' '
# print(answer)



#집합으로 표현한 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

# def solution(s):
#     answer = []
#     ref = s[2:-2].split('},{')
#     ref.sort(key=lambda x:len(x))
#     for i in ref:
#         i = map(int,i.split(','))
#         for j in i:
#             if j not in answer:
#                 answer.append(j)
    
#     return answer



#H-Index
#https://programmers.co.kr/learn/courses/30/lessons/42747

# def solution(citations):
#     answer = 0
#     citations.sort()
#     for i,j in enumerate(citations):  
#         if j >= len(citations[i:]):
#             answer = len(citations[i:])
#             break

#     return answer



#수포자의 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

# def solution(answers):

# answers = [1,3,2,4,2]
# answer = []
# no1 = [1,2,3,4,5]
# no2 = [2,1,2,3,2,4,2,5]
# no3 = [3,3,1,1,2,2,4,4,5,5]
# score = {1:0, 2:0, 3:0}

# for i,j in enumerate(answers):
#     if no1[i%5] == j:
#         score[1] += 1
#     if no2[i%8] == j:
#         score[2] += 1
#     if no3[i%10] == j:
#         score[3] += 1

# score = sorted(score.items(), key=lambda x:x[1], reverse=True)
# answer.append(score[0][0])
# if score[0][1] == score[1][1]:
#     answer.append(score[1][0])
# if score[0][1] == score[2][1]:
#     answer.append(score[2][0])

# print(answer)



#신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# report = list(set(report))
# k = 2
# e_count = {}
# r_count = {}
# ban_list = []
# for id in id_list:
#     r_count[id] = 0
#     e_count[id] = 0

# for i in report:
#     r_count[i.split(' ')[1]] += 1

# for x,y in r_count.items():
#     if y >= k:
#         ban_list.append(x)

# for j in report:
#     if j.split(' ')[1] in ban_list:
#         e_count[j.split(' ')[0]] += 1

# print(list(e_count.values()))
    


#k개의 숫자를 제거하여 가장 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

# def solution(number, k):
#     temp = []
#     for i,j in enumerate(number):
#         while temp and temp[-1] < j and k > 0:
#             temp.pop()
#             k -= 1
#         if k == 0:
#             temp += number[i:]
#             break
#         temp.append(j)
        
#     if k > 0:
#         temp = temp[:-k]
        
#     answer = ''.join(temp)      
    
#     return answer



#조이스틱을 활용해 이름 완성시키기
# https://programmers.co.kr/learn/courses/30/lessons/42860

# name = 'JAZ'
# r_name = name[::-1]
# std = (len(name) - 1)
# rstop = 0
# lstop = 0
# answer = 0

# for i in name:
#     dif = ord(i) - ord('A')
#     if dif < 13:
#         answer += dif
#     else:
#         answer += (26-dif)


# for j in range(len(name)):
#     if name[j] != 'A' and name[j+1] == 'A':
#         rstop += (j+1)
#         break
        
# for k in range(len(r_name)):
#     if r_name[k] != 'A' and r_name[k+1] == 'A':
#         lstop += (k+1)
#         break

# ltor = (lstop * 2) + rstop
# rtol = (rstop * 2) + lstop
# answer += min(ltor,rtol,std)

# print(answer)



# 로또의 최고순위와 최저순위
# https://programmers.co.kr/learn/courses/30/lessons/77484

# def solution(lottos, win_nums):
#     answer = []
#     rank = [6,5,4,3,2,1]
#     max = 0
#     min = 0
#     for lotto in lottos:
#         if lotto in win_nums:
#             max += 1
#             min += 1
#         elif lotto == 0:
#             max += 1
            
#     if max == 0:
#         answer.append(6)
#     else:
#         answer.append(rank[max-1])
    
#     if min == 0:
#         answer.append(6)
#     else:
#         answer.append(rank[min-1])
        
#     return answer



#사칙 연산
# https://www.acmicpc.net/problem/10869

# input = input()
# A = int(input.split(' ')[0])
# B = int(input.split(' ')[-1])
# print(A+B)
# print(A-B)
# print(A*B)
# print(int(A/B))
# print(A%B)



#곱셈
# https://www.acmicpc.net/problem/2588

# A = int(input())
# B = str(input())
# third = A * int(B[2])
# fourth = A * int(B[1])
# fifth = A * int(B[0])
# result = fifth*100 + fourth*10 + third

# print(third)
# print(fourth)
# print(fifth)
# print(result)



# 알람시계
# https://www.acmicpc.net/problem/2884

# input = input()
# hour = int(input.split(' ')[0])
# min = int(input.split(' ')[-1])
# if min >= 45:
#     min -= 45
#     print(f'{hour} {min}')
# else:
#     min += 15
#     if (hour-1) < 0:
#         print(f'23 {min}')
#     else:
#         print(f'{hour-1} {min}')



#더하기 사이클
# https://www.acmicpc.net/problem/1110

# input = int(input())
# temp = input
# reps = 0
# while True:
#     a = temp//10
#     b = temp%10
#     c = (a+b)%10
#     temp = (b*10) + c
#     reps += 1
#     if input == temp:
#         break

# print(reps)



#평균은 넘겠지
# https://www.acmicpc.net/problem/4344

# num = int(input())

# for _ in range(num):
#     scores = list(map(int, input().split()))
#     avg = sum(scores[1:])/scores[0]
    
#     cnt = 0
#     for i in scores[1:]:
#         if i > avg:
#             cnt += 1
            
#     per = f'{((cnt/scores[0])*100):.3f}%'
#     print(per)



#셀프 넘버
# https://www.acmicpc.net/problem/4673

# nums = []
# for i in range(1,10000):
#     dn = i + sum(map(int,str(i)))
#     nums.append(dn)

# for j in range(1,10000):
#     if j not in nums:
#         print(j)



#단어 공부
# https://www.acmicpc.net/problem/1157

# input = input().upper()
# result = ''
# temp = 0
# for num in range(65,91):
#     cnt = input.count(chr(num))
#     if cnt > temp:
#         result = chr(num)
#         temp = cnt
#     elif cnt == temp:
#         result += chr(num)

# if len(result) > 1:
#     print('?')
# else:
#     print(result)

# A2)
# word = input()
# word = list(word.upper())
# result_dict = {chr(i):0 for i in range(65,91)}
# for i in word:
#     result_dict[i] += 1
# result = sorted(result_dict.items(),key=lambda x:x[1],reverse=True)
# if result[0][1] == result[1][1]:
#     print("?")
# else:
#     print(result[0][0])



#크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

# c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# input = input()
# for alpha in c_alpha:
#     input = input.replace(alpha, '@')

# print(len(input))



#그룹 단어 체커
# https://www.acmicpc.net/problem/1316

# num = int(input())
# cnt = 0
# for _ in range(num):
#     word = str(input())
#     temp = 1
#     fail = 0
#     for i in range(len(word)-1):
#         if word[i] == word[i+1]:
#             temp += 1
#         else:
#             if temp == word.count(word[i]):
#                 temp = 1
#             else:
#                 fail += 1
    
#     if fail == 0:
#         cnt+=1

# print(cnt)

# A2)
# N = int(input())
# result_count = 0
# for _ in range(N):
#     word = input()
#     flag = True
#     for i in word:
#         word_count = word.count(i)
#         if word_count >= 2 and str(i*word_count) not in word:
#             flag = False
#             break
#     if flag:
#         result_count+=1

# print(result_count)



#설탕 배달
# https://www.acmicpc.net/problem/2839

# input = int(input())
# cnt = 0
# while input >= 0:
#     if input % 5 == 0:
#         cnt += input//5
#         print(cnt)
#         break
#     input -= 3
#     cnt += 1
# else:
#     print(-1)



#베르트랑 공준
# https://www.acmicpc.net/problem/4948

##에라토스테네스의 해인지 뭔지 함수형으로 만들어서 써봄 근데 겁나 느림..ㅋㅋㅋ
# def count_prime(n):
#     a = [False,False] + [True]*(n-1)
#     primes=[]

#     for i in range(2,n+1):
#         if a[i]:
#             primes.append(i)
#             for j in range(2*i, n+1, i):
#                 a[j] = False

#     return len(primes)

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         print(count_prime(2*n)-count_prime(n))

# A2) #주어진 범위내에서 테이블을 미리 다 만들어놓고 탐색만 시키는게 훨씬 빠름..!
# max_num = 123456
# num_list = [False, False]+[True] * (2*max_num)
# m = int(2*max_num ** 0.5)
# for i in range(2, m+1):
#     if num_list[i]:
#         for j in range(i+i, 2*max_num+1, i):
#             num_list[j] = False

# while 1:
#     n = int(input())
#     if n == 0:
#         break
#     print(len([i for i in range(n+1, 2*n+1) if num_list[i] == True]))



#Fly me to Alpha Centauri
# https://www.acmicpc.net/problem/1011

# A1)
# cnt = int(input())

# for _ in range(cnt):
#     x, y = map(int,input().split(' '))
#     distance = y - x
#     count = 0  # 이동 횟수
#     move = 1  # count별 이동 가능한 거리
#     move_total = 0  # 이동한 거리의 합
#     while move_total < distance:
#         count += 1
#         move_total += move
#         if count % 2 == 0:
#             move += 1  
#     print(count)

# A2) 제곱근을 활용한 풀이, 겁나빠른데 생각하기 어려움
# n=int(input())
# def f(m):
#     k = int(m**(0.5))
#     kk = k**2
#     if m == kk:
#         return 2*k-1
#     elif m > kk+k:
#         return 2*k+1
#     else:
#         return 2*k

# for _ in range(n):
#     a,b = map(int, input().split())
#     print(f(b-a))



#약수
# https://www.acmicpc.net/problem/1037

# x=input()
# y=list(map(int,input().split()))
# print(max(y)*min(y))



#달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

# A, B, V = list(map(int, input().split()))
# x=(V-B)%(A-B)
# y=(V-B)//(A-B)
# if x == 0:
#     print(y)
# else:
#     print(y+1)



#영화감독 숌
# https://www.acmicpc.net/problem/1436

# N = int(input())
# num = 665
# cnt = 0
# while cnt != N:
#     num += 1
#     if '666' in str(num):
#         cnt += 1
    
# print(num)



#최대공약수 최소공배수
# https://www.acmicpc.net/problem/2609

# A, B = list(map(int, input().split()))
# n = 2
# x = 1
# while n < 10000:
#     if A%n == 0 and B%n == 0:
#         A /= n
#         B /= n
#         x *= n
#     else:
#         n += 1

# print(x)
# print(int(A*B*x))



# ACM 호텔
# https://www.acmicpc.net/problem/10250

# reps = int(input())
# for i in range(reps):
#     H, W, N = list(map(int, input().split()))
#     floor = N % H
#     room = N // H + 1
#     if floor == 0:
#         floor += H
#         room -= 1
    
#     if room < 10:
#         print(int(str(floor)+'0'+str(room)))
#     else:
#         print(int(str(floor)+str(room)))



# 소수 구하기
# https://www.acmicpc.net/problem/1929

# max_num = 1000000
# table = [False, False]+[True]*999999
# m = int(max_num ** 0.5)
# for i in range(2, m+1):
#     if table[i]:
#         for j in range(2*i, max_num+1, i):
#             table[j] = False

# a,b = list(map(int, input().split()))
# for i in range(a,b+1):
#     if table[i] == True:
#         print(i)



# 스택
# https://www.acmicpc.net/problem/10828

# 그냥 input으로 입력값받으면 시간초과됨.. 아래 방식을 기억해두자
# import sys
# input = sys.stdin.readline
# N = int(input())
# list = []
# for i in range(N):
#     cmd = input().split()
#     if cmd[0] == 'push':
#         list.append(int(cmd[1]))
#     elif cmd[0] == 'top':
#         if len(list) > 0:
#             print(list[-1])
#         else:
#             print(-1)
#     elif cmd[0] == 'pop':
#         if len(list) > 0:
#             print(list.pop())
#         else:
#             print(-1)
#     elif cmd[0] == 'size':
#         print(len(list))
#     elif cmd[0] == 'empty':
#         if len(list) == 0:
#             print(1)
#         else:
#             print(0)



# 제로
# https://www.acmicpc.net/problem/10773

# import sys
# input = sys.stdin.readline

# N = int(input())
# list = []
# for _ in range(N):
#     call = int(input())
#     if call == 0:
#         list.pop()
#     else:
#         list.append(call)
        
# print(sum(list))



# 괄호
# https://www.acmicpc.net/problem/9012

# N = int(input())
# for i in range(N):
#     s = input()
#     list = []
#     for j in s:
#         if j == '(':
#             list.append(j)
#         elif j == ')':
#             if len(list) != 0 and list[-1] == '(':
#                 list.pop()
#             else:
#                 list.append(')')
#                 break
#     if len(list) == 0:
#         print('YES')
#     else:
#         print('NO')



# 좌표 정렬하기2
# https://www.acmicpc.net/problem/11651

# import sys
# input = sys.stdin.readline

# N = int(input())
# list = []
# for _ in range(N):
#     x,y = map(int,input().split())
#     list.append([x,y])

# list.sort(key=lambda x:(x[1], x[0]))
# for i in list:
#     print(i[0], i[1])



#나무 자르기
# https://www.acmicpc.net/problem/2805

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# trees = list(map(int, input().split()))

# low = 0
# high = max(trees)

# while low <= high:
#     A = (low+high)//2
#     tot = 0
#     for i in trees:
#         if i > A:
#             tot += i - A
    
#     if tot >= M:
#         low = A + 1
#     else:
#         high = A - 1

# print(high)



# 최소공배수
# https://www.acmicpc.net/problem/1934

# import sys
# input = sys.stdin.readline

# def cal(n,m):
#     if m == 0:
#         return n
#     elif n % m == 0:
#         return m
#     return cal(m, n%m)

# N = int(input())
# for _ in range(N):
#     A,B = map(int, input().split())
#     if B > A:
#         A,B = B,A
#     print(int(A*B/cal(A,B)))
        


# 이항 계수 1
# https://www.acmicpc.net/problem/11050

# from sys import stdin

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# n, k = map(int, stdin.readline().split())
# print(factorial(n) // (factorial(k) * factorial(n - k)))



# 다리 놓기
# https://www.acmicpc.net/problem/1010

# from sys import stdin
# input = stdin.readline

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# k = int(input())

# for _ in range(k):
#     N, M = map(int, input().split())
#     print(factorial(M) // (factorial(N) * factorial(M - N)))



# 균형잡힌 세상
# https://www.acmicpc.net/problem/4949
        
# while True:
#     string = input()
#     stack = []
    
#     if string == '.':
#         break
    
#     for str in string:
#         if str == '(' or str == '[':
#             stack.append(str)
#         elif str == ']':
#             if len(stack) != 0 and stack[-1] == '[':
#                 stack.pop()
#             else:
#                 stack.append(']')
#                 break
#         elif str == ')':
#             if len(stack) != 0 and stack[-1] == '(':
#                 stack.pop()
#             else:
#                 stack.append(')')
#                 break
    
#     if len(stack) == 0:
#         print('yes')
#     else:
#         print('no')



# 스택 수열
# https://www.acmicpc.net/problem/1874

# import sys
# input = sys.stdin.readline

# N = int(input())
# stack = []
# answer = []
# flag = True
# cnt = 1
# for _ in range(N):
#     num = int(input())
#     while cnt <= num:
#         stack.append(cnt)
#         answer.append('+')
#         cnt += 1
    
#     if stack[-1] == num:
#         stack.pop()
#         answer.append('-')
#     else:
#         print('NO')
#         flag = False
#         break

# if flag == True:
#     for i in answer:
#         print(i)



# 회전하는 큐
# https://www.acmicpc.net/problem/1021

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# target = list(map(int, input().split()))
# queue = [i for i in range(1, N+1)]
# cnt = 0
# for i in range(M):
#     length = len(queue)
#     index = queue.index(target[i])
#     if index < (length - index):
#         while True:
#             if queue[0] == target[i]:
#                 del queue[0]
#                 break
#             else:
#                 queue.append(queue[0])
#                 del queue[0]
#                 cnt += 1
#     else:
#         while True:
#             if queue[0] == target[i]:
#                 del queue[0]
#                 break
#             else:
#                 queue.insert(0, queue[-1])
#                 del queue[-1]
#                 cnt += 1

# print(cnt)



# 큐2
# https://www.acmicpc.net/problem/18258

# import sys
# from collections import deque

# input = sys.stdin.readline

# N = int(input())
# q = deque([])

# for _ in range(N):
#     cmd = input().split()
#     if cmd[0] == 'push':
#         q.append(int(cmd[1]))
#     elif cmd[0] == 'front':
#         if len(q) > 0:
#             print(q[0])
#         else:
#             print(-1)
#     elif cmd[0] == 'back':
#         if len(q) > 0:
#             print(q[-1])
#         else:
#             print(-1)
#     elif cmd[0] == 'size':
#         print(len(q))
#     elif cmd[0] == 'empty':
#         if len(q) == 0:
#             print(1)
#         else:
#             print(0)
#     elif cmd[0] == 'pop':
#         if len(q) > 0:
#             print(q.popleft())
#         else:
#             print(-1)



# 통계학
# https://www.acmicpc.net/problem/2108

# import sys
# from collections import Counter

# n = int(sys.stdin.readline())
# temp = []

# for i in range(n):
#     temp.append(int(sys.stdin.readline()))

# temp.sort()
# frq = Counter(temp).most_common()

# print(round(sum(temp) / n))
# print(temp[n // 2])

# if len(frq) > 1:
#     if frq[0][1] == frq[1][1]:
#         print(frq[1][0])
#     else:
#         print(frq[0][0])
# else:
#     print(frq[0][0])
# print(temp[-1] - temp[0])



# 색종이 만들기
# https://www.acmicpc.net/problem/2630

# import sys
# input = sys.stdin.readline

# N = int(input())
# matrix = []
# result = []

# for _ in range(N):
#     line = list(map(int, input().split()))
#     matrix.append(line)
    
# def papercolor(x,y,N):
#     color = matrix[x][y]
#     for i in range(x, x+N):
#         for j in range(y, y+N):
#             if color != matrix[i][j]:
#                 papercolor(x, y, N//2)
#                 papercolor(x, y+N//2, N//2)
#                 papercolor(x+N//2, y, N//2)
#                 papercolor(x+N//2, y+N//2, N//2)
#                 return
#     if color == 0:
#         result.append(0)
#     else:
#         result.append(1)
        
# papercolor(0, 0, N)
# print(result.count(0))
# print(result.count(1))



# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

# def solution(n, lost, reserve):
#     list = [1] * n
#     for i in lost:
#         list[i-1] -= 1
#     for j in reserve:
#         list[j-1] += 1

#     for k in range(len(list)-1):
#         if list[k] == 2 and list[k+1] == 0:
#             list[k] -= 1
#             list[k+1] += 1
#         elif list[k] == 0 and list[k+1] == 2:
#             list[k] += 1
#             list[k+1] -= 1

#     return (len(list) - list.count(0))



# [카카오 인턴] 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

# npad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
# hand = 'right'
# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# cr_left = [3,0]
# cr_right = [3,2]
# answer = []

# for num in numbers:
#     cords = []
#     for i in npad:
#         if num in i:
#             cords.append(npad.index(i))
#             cords.append(i.index(num))
#             break
    
#     if num in [1, 4, 7]:
#         cr_left = cords
#         answer.append('L')
#     elif num in [3, 6, 9]:
#         cr_right = cords
#         answer.append('R')
#     else:
#         distance_l = abs(cords[0] - cr_left[0]) + abs(cords[1] - cr_left[1])
#         distance_r = abs(cords[0] - cr_right[0]) + abs(cords[1] - cr_right[1])

#         if distance_l > distance_r:
#             cr_right = cords
#             answer.append('R')
#         elif distance_l < distance_r:
#             cr_left = cords
#             answer.append('L')
#         else:
#             if hand == 'right':
#                 cr_right = cords
#                 answer.append('R')
#             elif hand == 'left':
#                 cr_left = cords
#                 answer.append('L')
                
# print(''.join(answer))



# 크레인 인형뽑기 게임
# https://programmers.co.kr/learn/courses/30/lessons/64061

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]
# basket = []
# result = 0
# for i in range(len(moves)):
#     for j in range(len(board)):
#         crane = moves[i]
#         target = board[j][crane-1]
#         if target == 0:
#             continue
#         else:
#             board[j][crane-1] = 0
#             if basket and basket[-1] == target:
#                 result += 2
#                 basket.pop()
#                 break
#             else:
#                 basket.append(target)
#                 break

# print(result)



# 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

# a = [1,2,3,4]
# b = [-3,-1,0,2]
# result = 0
# for i in range(len(a)):
#     result += a[i] * b[i]
    
# print(result)



# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# def solution(participant, completion):
#     participant.sort()
#     completion.sort()

#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
        
#     return participant[-1]



# 약수의 개수와 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/77884

# def div(num):
#     if num == 1:
#         return 1
#     else:
#         count = 0
#         for i in range(2,int(num/2)+1):
#             if num % i == 0:
#                 count += 1
#         return count

# def solution(left, right):
#     result = 0
#     for num in range(left, right+1):
#         temp = div(num)
#         if temp%2 == 0:
#             result += num
#         else:
#             result -= num
            
#     return result



# 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

# n = 45
# temp = ''
# answer = 0
# while n:
#     temp += str(n%3)
#     n //= 3
        
# for i in range(len(temp)):
#     answer += int(temp[i])*(3**(len(temp)-1-i))

# print(answer)



# 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

# a = 5
# b = 24
# days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# count = 0

# for i in range(a-1):
#     count += month[i]

# count = (count+(b-1))%7
# print(days[-2+count])



# 최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491

# sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
# arr_sizes = []
# for i in sizes:
#     if i[0] > i[1]:
#         arr_sizes.append([i[0], i[1]])
#     else:
#         arr_sizes.append([i[1], i[0]])
# x = sorted(arr_sizes)
# y = sorted(arr_sizes, key=lambda x:x[1])
# print(x[-1][0]*y[-1][1])



# 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389

# def solution(n):
#     for x in range(1,n):
#         if n%x == 1:
#             return x



# 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612

# price = 3
# money = 20
# count = 4
# n = 1
# total = 0
# while count:
#     total += price*n
#     n += 1
#     count -= 1

# if total > money:
#     print(total-money)
# else:
#     print(0)



# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# answer = []
# def notation(num, n):
#     result = ''
#     while num:
#         result = str(num%2) + result
#         num //= 2
    
#     if len(result) < n:
#         result = '0'*(n-len(result)) + result
    
#     return result

# for i in range(n):
#     x = notation(arr1[i], n)
#     y = notation(arr2[i], n)
#     temp = ''
#     for j in range(n):
#         if x[j] == '0' and y[j] == '0':
#             temp += ' '
#         else:
#             temp += '#'
#     answer.append(temp)

# print(answer)



# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

# def solution(s):
#     target = int(len(s)/2)
#     if len(s)%2 == 0:
#         return s[target-1:target+1]
#     else:
#         return s[target]



# [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

# dr = '1D#2S*3S'
# dr_list = []
# temp = 0
# for i in dr:
#     try:
#         if i != '0':
#             temp += int(i)
#         else:
#             temp *= 10
#     except:
#         if i in ['S', 'D', 'T']:
#             if i == 'D':
#                 temp **= 2
#             elif i == 'T':
#                 temp **= 3
#             dr_list.append(temp)
#             temp = 0
#         if i == '*':
#             if len(dr_list) == 1:
#                 dr_list[0] *= 2
#             else:
#                 dr_list[-2] *= 2
#                 dr_list[-1] *= 2
#         elif i == '#':
#             dr_list[-1] *= -1
        
# print(sum(dr_list))



# 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906

# arr = [1,1,3,3,0,1,1]
# answer = []
# for i in arr:
#     if len(answer) == 0:
#         answer.append(i)
#     else:
#         if i == answer[-1]:
#             continue
#         else:
#             answer.append(i)

# print(answer)



# 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

# arr = [5, 9, 7, 10]
# divisor = 5

# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i%divisor == 0:
#             answer.append(i)

#     if len(answer) == 0:
#         return -1
#     else:
#         answer.sort()
#         return answer

# print(solution([5, 9, 7, 10], 5))



# 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

# def solution(a, b):
#     answer = 0
#     if a > b:
#         a, b = b, a
#     elif a == b:
#         return a

#     for i in range(a, b+1):
#         answer += i
    
#     return answer



# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

# strings = ["abce", "abcd", "cdx"]
# n = 2
# strings.sort()
# answer = sorted(strings, key=lambda x:x[1])
# print(answer)



# 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916

# s = "Pyyp"
# if s.lower().count('p') == s.lower().count('y'):
#     print('true')
# else:
#     print('false')



# 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

# def solution(s):
#     return ''.join(sorted(s, reverse=True))



# 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

# s = "a234"
# def solution(s):
#     try:
#         int(s)
#     except:
#         return False
#     return len(s) == 4 or len(s) == 6

# print(solution(s))



# 서울에서 김서방 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12919

# seoul = ["Jane", "Kim"]
# target = seoul.index('Kim')
# print(f'김서방은 {target}에 있다')



# 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

# n = 12
# answer = 0
# for i in range(1, int(n/2)+1):
#     if n%i == 0:
#         answer += i
# print(answer+n)



# 문자열을 정수로 바꾸기
# https://programmers.co.kr/learn/courses/30/lessons/12925

# s = '-1234'
# print(int(s))



# 수박수박수박수박수박수?
# https://programmers.co.kr/learn/courses/30/lessons/12922

# A1)
# n = 4
# answer = ''
# for i in range(n):
#     if i%2 == 0:
#         answer += '수'
#     else:
#         answer += '박'
# print(answer)

# A2) #n의 제한조건이 10000이라는 점을 이용
# n = 4
# answer = '수박'*5000
# print(answer[:n])


# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

# max_num = 1000000
# table = [False, False]+[True]*999999
# m = int(max_num ** 0.5)
# for i in range(2, m+1):
#     if table[i]:
#         for j in range(2*i, max_num+1, i):
#             table[j] = False

# n = 5
# count = 0
# for i in range(2,n+1):
#     if table[i] == True:
#         count += 1

# print(count)



# 자릿수 더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931

# N = 987
# n = str(N)
# answer = 0
# for i in n:
#     answer += int(i)
# print(answer)



# 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932

# def solution(n):
#     return list(reversed(list(map(int, str(n)))))



# 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933

# def solution(n):
#     return int(''.join(sorted(str(n), reverse=True)))



# 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934

# def solution(n):
#     for i in range(1, int(n**0.5)+1):
#         if i*i == n:
#             return (i+1)**2
#     return -1



# 제일 작은 수 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12935

# def solution(arr):
#     arr.remove(min(arr))
#     if not arr:
#         arr.append(-1)
        
#     return arr



# 짝수와 홀수
# https://programmers.co.kr/learn/courses/30/lessons/12937

# def solution(num):
#     if num%2 == 0:
#         return 'Even'
#     else:
#         return 'Odd'



# 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

# def solution(n, m):
#     def gcd (a, b):
#         while b > 0:
#             a, b = b, a%b
#         return a

#     def lcm (a,b):
#         return a * b / gcd(a,b)
        
#     answer = []
#     answer.append(gcd(n,m))
#     answer.append(lcm(n,m))
    
#     return answer



# 콜라츠 추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

n = 6
cnt = 0
while n != 1:
    if n%2 == 0:
        n /= 2
    else:
        n = n*3 +1
    cnt += 1
print(cnt)