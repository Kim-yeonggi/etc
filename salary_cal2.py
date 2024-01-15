# 연봉계산기
# 사용자 입력
# 세액표는 천원단위, 이상 미만으로 구간 설정되어 있음
# 1.연봉(원단위)
# 2.비과세액(원단위)
# 3.부양가족수(본인포함), 최소 1
#
# 출력사항
# 1.국민연금(4.5%) np
# 2.건강보험금(3.545%) hi
# ㄴ3.요양보험:건강보험의 12.95%)ni
# 4.고용보험(0.9%)  ei
# 5.근로소득세(표참고)  e
# ㄴ6.지방소득세:근로소득세의 10%   lit
# 7.년 예상 실수령액 (원단위)
# 8.월 환산 실수령액 (원단위)
# * 모든 단계에서 1원단위는 절사 0으로 치환


import math

while True:
    try:
        inform = {'연봉':'', '비과세액':'','부양가족수':''}

        for i in list(inform.keys()):
            inform[i] = int(input(f"{i}을/를 입력하세요 : "))
        sal = inform[list(inform.keys())[0]]//12         # 월급
        cal = sal-inform[list(inform.keys())[1]]/12
    except:
        # 에러시 실행할 기본 값 입력
        print("입력중 에러 발생")
        inform = {'연봉': 36000000, '비과세액': 2400000, '부양가족수': 1}
        sal = inform[list(inform.keys())[0]]//12         # 월급
        cal = sal-inform[list(inform.keys())[1]]/12

    try:
        with open('2023_2.txt', 'r') as file:
            global e
            for line in file:       # file에서 한 라인씩 읽기 반복
                # chart_list = list(line.strip().split('\t'))
                chart_list = line.strip().split('\t')   # tab 기준으로 분리해서 리스트화
                for j in range(len(chart_list)):        # 리스트를 대상으로 13바퀴
                    chart_list[j] = chart_list[j].strip().replace(',', '')  # 한 라인 내부 모든 요소에 대한 쉼표 제거
                    if not chart_list[j].isdigit():     # 숫자로 변환 가능한 문자가 아니면
                        if '-' == chart_list[j]:        # 하이픈이라면 0으로 변경
                            chart_list[j] = 0
                        else:          # 하이픈이 아닐 때
                            for alpha in chart_list[j]:     # 한 문자씩 검사
                                if alpha not in '0123456789':       # 숫자가 아닌 문자가 포함된 경우
                                    chart_list[j] = chart_list[j].replace(alpha, '')
                    chart_list[j] = int(chart_list[j])
                chart_list[0] *= 1000
                chart_list[1] *= 1000

                temp1_list = chart_list[2:]     # 금액 이상 미만을 제외한 나머지 데이터 : 부양가족수 별 세액
                temp1_list = sorted(temp1_list)
                temp1_list.sort(reverse=True)   # 내림차순 정렬
                if chart_list[2:] != temp1_list:
                    if 0 in chart_list and chart_list.index(0) != len(chart_list)-1:        # 리스트 중간에 0이 발견됨
                        if chart_list[chart_list.index(0)+1] == 0:
                            gap1 = (chart_list[chart_list.index(0)-1]-chart_list[chart_list.index(0)+2])//3
                            chart_list[chart_list.index(0)] = chart_list[chart_list.index(0)-1] - gap1
                            chart_list[chart_list.index(0)] = chart_list[chart_list.index(0)-1] - gap1
                        else:
                            chart_list[chart_list.index(0)] = (chart_list[chart_list.index(0)-1] + chart_list[chart_list.index(0)+1])//2

                    for l in range(4, len(chart_list)):
                        if chart_list[l] >= chart_list[l-1]:    #앞의 요소보다 뒤의 요소가 더 클 경우
                            if l == len(chart_list)-1:      # 마지막 자리
                                gap2 = chart_list[l-2] - chart_list[l-1]
                                chart_list[l] = chart_list[l-1] - gap2
                            elif l > 4:                     # 첫번째와 마지막 제외한 나머지 자리
                                chart_list[l] = (chart_list[l-1] + chart_list[l+1])//2
                            else:       # 첫번째 자리
                                gap2 = chart_list[l+1] - chart_list[l+2]
                                chart_list[l] = chart_list[l+1] + gap2

                print(chart_list)

                if chart_list[0] <= cal < chart_list[1]:            # 근로소득세
                    e = chart_list[inform[list(inform.keys())[2]]+1]

        t = {'np':0.045, 'hi':0.03545, 'ni':0.1295, 'ei':0.009, 'lit':0.1}

        res = []
        for m in list(t.keys()):
            if m == 'ni':
                res.append(cal*t['hi']*t[m])
            elif m == 'lit':
                res.append(e*t[m])
            else:
                res.append(cal*t[m])
        res.insert(res.index(e*t['lit'])-1, e)

        for k in range(len(res)):
            t2 = res[k]*0.1
            res[k] = round(t2, 0)*10
            res[k] = int(str(res[k])[:str(res[k]).find('.')])

        g = sal
        for j in res:
            g -= j
        h = g * 12
        res += [g, h]

        print('#'*30,
              f'\n국민연금({t["np"]*100:.1f}%): {res[0]}원'
              f'\n건강보험({t["hi"]*100:.3f}%): {res[1]}원'
              f'\nㄴ요양보험({t["ni"]*100:.2f}%): {res[2]}원'
              f'\n고용보험({t["ei"]*100:.1f}%): {res[3]}원'
              f'\n근로소득세(간이세액): {res[4]}원'
              f'\nㄴ지방소득세({t["lit"]*100:.1f}%): {res[5]}원'
              f'\n{"-"*30}'
              f'\n년 예상 실수령금액: {res[7]:.0f}원'
              f'\nㄴ월 환산금액: {res[6]:.0f}원'
              f'\n{"#"*30}')
    except:
        print('연산 중 에러 발생')
