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
