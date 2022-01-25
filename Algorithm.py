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