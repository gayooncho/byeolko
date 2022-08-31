# 01 숫자의 합 구하기

# 백준 11720

# 숫자의 합 구하기

# 숫자 받기
n = input()
num = input()

# 자르기
num_list = list(num)

# int형으로 변경
num_list_int = list(map(int, num_list))

# 리스트 합
sum_num = sum(num_list_int)

print(sum_num)

# ------------------------------------------------

# 백준 1546

# 평균구하기

# 과목개수
n = int(input())
# 각 과목의 시험 성적
scores = input()

# 자르기
scores_list = list(scores.split( ))

# 정수형으로 변경
scores_list_int = list(map(int, scores_list))

scores_list_int.sort()

# 최대값 구하기
max = scores_list_int[-1]

# 새로운 점수 구하기
new_scores = []
for i in scores_list_int:
    act_score = i
    new_score = i/max * 100
    new_scores.append(new_score)

# 
score_avg = (sum(new_scores))/n

print((score_avg))


#----------------------------------------------

