# name = input('type your name: ').lower()
# f_index = name[0]
# s_index = name[1]
# if f_index >= s_index:
#     print(name[1:])
# else:
#     newname = name.replace(max(name),"")
#     print(newname)



# def solution(array, commands):
#     answer = []
#     for x in commands:
#         func = array[(x[0]-1):x[1]]
#         func.sort()
#         answer.append(func[x[2]-1])
#     return answer

# def solution(array, commands):
#     answer = []
#     for x in commands:
#         i,j,k = x
#         func = array[(i-1):j]
#         func.sort()
#         answer.append(func[k-1])
#     return answer






#1, 9번만 통과
# def solution(numbers):
#     answer = []
#     n = 0
#     for i in range(len(numbers)):
#         for j in range(n+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
            
#         n += 1

#     answer = list(set(answer))
#     answer.sort()

#     return answer

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(len(numbers)):
#             if i != j:
#                 answer.append(numbers[i] + numbers[j])
            
#     answer = list(set(answer))
#     answer.sort()

#     return answer
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


# import collections

# def solution(N, stages):
#     answer = []
#     fail_rate = {}
#     survivor = len(stages)
#     for i in range(1, N+1):
#         if survivor != 0:
#             fail_rate[i] = (collections.Counter(stages)[i] / survivor)
#             survivor -= stages.count(i)

#     fail_rate = sorted(fail_rate.items(), key=lambda x: x[1], reverse=True)
#     for j in fail_rate:
#         answer.append(j[0])

#     return answer





#인생..........
# import re

# new_id = new_id.lower()
# new_id = re.sub('[^-_.a-z0-9]', "", new_id)

# mdot_finder = re.search('[.]{2,}', new_id)
# result = mdot_finder.group()
# print(mdot_finder)
# while mdot_finder != None:
#     new_id.replace('[.]{2,}',".")
#     ...........???


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





# def solution(phone_number):
#     answer = list(phone_number)

#     for i in range(len(phone_number) - 4):
#         answer[i] = "*"
    
#     return ("".join(answer))





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



# s = "one4seveneight"

# a = {'zero': '0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
# for key,value in a.items():
#     s = s.replace(key, value)

# print(s)
    


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


##폰켓몬 최대로 얻기##
# nums = [3, 3, 3, 2, 2, 2]
# temp = set(nums)

# if len(temp) > (len(nums)/2):
#     answer = len(nums) / 2
# else:
#     answer = len(temp)

# print(answer)