# 연봉계산기
# 사용자 입력
# 세액표는 천원단위, 이상 미만으로 구간 설정되어 있음
# 1.연봉(원단위)
# 2.비과세액(원단위)
# 3.부양가족수(본인포함), 최소 1
#
# 출력사항
# 1.국민연금(4.5%)
# 2.건강보험금(3.545%)
# 3.요양보험:건강보험의 12.95%)
# 4.고용보험(0.9%)
# 5.근로소득세(표참고)
# 6.지방소득세:근로소득세의 10%
# 7.년 예상 실수령액 (원단위)
# 8.월 환산 실수령액 (원단위)
# * 모든 단계에서 1원단위는 절사 0으로 치환


import math
inform = {'연봉':'', '비과세액':'','부양가족수':''}

while True:
    for i in list(inform.keys()):
        inform[i] = int(input(f"{i}을/를 입력하세요 : "))
    sal = inform[list(inform.keys())[0]]//12         # 월급
    cal = sal-inform[list(inform.keys())[1]]/12

    with open('2023noise.txt', 'r') as file:
        global e
        for line in file:
            chart_list = list(line.strip().split('\t'))
            for i in range(len(chart_list)):
                chart_list[i] = chart_list[i].strip().replace(',', '')
                if not chart_list[i].isdigit():
                    if '-' == chart_list[i]:
                        chart_list[i] = 0
                    else:
                        for alpha in chart_list[i]:
                            if alpha not in '0123456789':       # 숫자가 아닌 문자가 포함된 경우
                                chart_list[i] = chart_list[i].replace(alpha, '')
                chart_list[i] = int(chart_list[i])
            chart_list[0] *= 1000
            chart_list[1] *= 1000

            temp1_list = chart_list[2:]
            temp1_list = sorted(temp1_list)
            temp1_list.sort(reverse=True)
            if chart_list[2:] != temp1_list:
                if 0 in chart_list and chart_list.index(0) != len(chart_list)-1:
                    if chart_list[chart_list.index(0)+1] == 0:
                        gap = (chart_list[chart_list.index(0)-1]-chart_list[chart_list.index(0)+2])//3
                        chart_list[chart_list.index(0)] = chart_list[chart_list.index(0)-1] - gap
                        chart_list[chart_list.index(0)] = chart_list[chart_list.index(0)-1] - gap
                    else:
                        chart_list[chart_list.index(0)] = (chart_list[chart_list.index(0)-1] + chart_list[chart_list.index(0)+1])//2

            print(chart_list)

            if chart_list[0] <= cal < chart_list[1]:            # 근로소득세
                e = chart_list[inform[list(inform.keys())[2]]+1]

            # print(chart_list)
    a = cal * 0.045
    b = cal * 0.03545
    c = b * 0.1295
    d = cal*0.009

    f = e*0.1           # 지방소득세
    res = [a,b,c,d,e,f]
    g = cal
    for j in res:
        g -= j
    h = g * 12
    res += [g, h]
    for k in range(len(res)):
        if str(res[k]).find('.') != -1:
            res[k] = int(str(res[k])[:str(res[k]).find('.')])
        if int(str(res[k])[-1]) < 5:
            res[k] = math.floor(res[k])
        else:
            res[k] = math.ceil(res[k])
        if str(res[k])[-1] != '0':
            temp2 = int(str(res[k])[-1])
            res[k] -= temp2

    print('#'*30,
          f'\n국민연금(4.5%): {res[0]}원'
          f'\n건강보험(3.545%): {res[1]}원'
          f'\nㄴ요양보험(12.95%): {res[2]}원'
          f'\n고용보험(0.9%): {res[3]}원'
          f'\n근로소득세(간이세액): {res[4]}원'
          f'\nㄴ지방소득세(10%): {res[5]}원'
          f'\n{"-"*30}'
          f'\n년 예상 실수령금액: {res[7]}원'
          f'\nㄴ월 환산금액: {res[6]}원'
          f'\n{"#"*30}')
