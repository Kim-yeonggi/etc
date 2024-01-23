# 1.서버(운영) - 각 클래스 중계
# - tick 개념 포함
# - tick 기준으로 각 클래스 정보 취합 후 갱신
#
# 2. user
# 3.
# 4. 맵 ; 전체 맵 구조, 시설물 배치 등 -> 시설물 클래스와 연동

# 문제) 추상화
# 클래스 구조로
# 콘솔에서 진행되는 게임
# 1. 오브젝트 클래스 / 2. user 클래스 / 3. npc 클래스  / 4. map 클래스 / 5. 운영(서버, 상태 데이터) mng 클래스
# 맵과 각 셀의 형태가 사각형, 이동은 좌/우/위/아래 직선 이동 형태 / 대각 이동 없음
# 마우스를 이용하지 않는 키보드 방향키 외 키 입력을 통한 형태
# 1인 플레이    npc 자동 움직임 가능
# 조 마다 2개씩 제안
# 크래픽 요소는 전부 콘솔에 표기
# 2차원 배열 형태로 맵 표기


import random
class ai:
    x = 13
    y = 13
    next_x = 0
    next_y = 0
    fw = random.random()
    def __init__(self, now_loc_x, now_loc_y, p):        # 후에 입력받을 값으로 대체
        self.now_loc_x = now_loc_x
        self.now_loc_y = now_loc_y
        self.p = p

    # 위치 저장
    def save_location(self):         # 현재 ai 좌표() 리턴 받기 map[x][y]
        if self.x != self.now_loc_x or self.y != self.now_loc_y:    # 이동을 했다면
            self.x = self.now_loc_x         # 현재 좌표 갱신
            self.y = self.now_loc_y
            return self.now_loc_x, self.now_loc_x

    # 이동
    def move(self):
        try:
            if self.p:
                if self.fw < 0.25:
                    self.next_x = self.x - 1
                elif self.fw < 0.5:
                    self.next_y -= 1
                elif self.fw < 0.75:
                    self.next_x += 1
                else:
                    self.next_y += 1
                print(self.next_x, self.next_y)
            else:
                pass
            return
        except:
            pass
        finally:
            pass

'''
    # 주위에 폭탄이나 아이템이 있을 경우 이동
    def bomb_item(self):
        try:
            if map[self.x][self.y] == 10:   # 현재 ai 좌표에 폭탄이 있을 경우
                if map[self.x][self.y+1] == 10:
                    pass
                elif map[self.x][self.y-1] == 10:
                    pass
                elif 상하가 폭탄 범위일 경우:
                폭탄 반대 방향으로 이동
            elif map[self.x+1] in "56789" or map[self.x-1] in "56789" or map[self.y+1] in "56789" or map[self.y-1] in "56789":
                아이템 방향으로 이동
            else:
                self.move()
        except:
            pass

'''


    # def total(self):




ai(13, 13,True)
