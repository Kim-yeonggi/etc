# 맥도날드 키오스크

dict_category = {1:"추천메뉴", 2:"버거메뉴",3:"음료메뉴",4:"사이드메뉴",5:"디저트메뉴",6:"해피밀",7:["빅맥", 4500],8:["1955버거",5000],9:["맥스파이시상하이버거",4500],10:["맥치킨버거",3500]}
# dict_recommen = {7:["빅맥", 4500],8:["1955버거",5000],9:["맥스파이시상하이버거",4500],10:["맥치킨버거",3500]}

# 버거 모음
dict_burger_menu = {1:"시그니처 버거",2:"비프 버거",3:"치킨&쉬림프 버거",4:"불고기&기타 버거"}
dict_burger_sig = {1:["그릴드머쉬룸버거",8000],2:["골든에그치즈버거",7800],3:["트리플어니언버거",7900]}
dict_burger_beef = {1:["빅맥",4500],2:["치즈버거",3500],3:["쿼터파운드버거",5000],4:["더블쿼터파운드 치즈버거", 6000]}
dict_burger_chi = {1:["맥스파이시상하이버거",4500],2:["맥치킨버거",3500],3:["맥크리스피디럭스버거",4300]}
dict_burger_bul = {1:["더블불고기버거",4000],2:["슈비버거",4500]}

# 버거 세트 - 사이드 음료
dict_set_side = {1:['감자튀김', 0], 2:['감자튀김 + 치즈스틱 2조각', 1500], 3:['치즈스틱',500]}
dict_set_drink = {1:['코카콜라'], 2:['스프라이트'], 3:['환타']}

# 음료 모음
dict_drink_menu = {1:"커피",2:"탄산음료",3:"과일음료",4:"쉐이크"}
dict_drink_cof = {1:["바닐라라떼",3000],2:["아메리카노",2000],3:["카페라떼",2500],4:['카푸치노',2500],5:['드립커피',1800]}
dict_drink_soft = {1:['코카콜라',1500],2:['환타',1500],3:['스프라이트',1500]}
dict_drink_jui = {1:['골드 맥피즈',2000],2:['자두천도복숭아 칠러',2500],3:['제주한라봉 칠러',2500]}
dict_drink_sha = {1:['초코쉐이크',2500],2:['바닐라쉐이크',2500],3:['딸기쉐이크',2500]}

# 사이드 모음
dict_side_menu = {1:'스낵랩', 2:'코울슬로', 3:'치즈스틱', 4:'맥너겟', 5:'치킨텐더', 6:'감자튀김', 7:'소스'}
dict_side_sw = {1:['토마토 치킨 스낵랩', 2000], 2:['상하이 치킨 스낵랩',2000]}
dict_side_col = {1:['코울슬로', 1500]}
dict_side_mcn = {1:['4조각', 3000], 2:['6조각', 4000]}
dict_side_ct = {1:['2조각', 3500]}
dict_side_pot = {1:['S', 1000], 2:['M', 1300], 3:['L', 1500]}
dict_side_sau = {1:['디핑소스 스위트 앤 사워', 500], 2:['디핑소스 스위트 칠리', 500], 3:['디핑소스 케이준', 500]}

# 디저트 모음
dict_disert_menu = {1:'라즈베리크림치즈파이', 2:'맥플러리'}
dict_disert_raspie = {1:['라즈베리크림치즈파이', 1500]}
dict_disert_mcf = {1:['오레오 맥플러리', 3000], 2:['초코오레오 맥플러리', 3000], 3:['딸기오레오 맥플러리', 3000]}

# 해피밀 모음
dict_hm = {1:['맥너겟 4조각 해피밀', 3500], 2:['햄버거 해피밀', 3500], 3:['불고기버거 해피밀', 3800]}

def print_menu(dict):       # 번호 선택 및 메뉴 나열
    for i in range(1, len(dict.keys())+1):
        if type(dict[i]) != list:
            print(f"{i}. {dict[i]} ")
        elif type(dict[i]) == list and len(dict[i]) >= 2:
            print(f"{i}. {dict[i][0]} : {dict[i][1]}원")
        else:       # 세트메뉴
            print((f"{i}. {dict[i][0]}"))
    choice = int(input("선택 : "))
    print("-"*30)
    return choice


def component(burger_inform_list):    # 버거 메뉴 구성 선택
    choice = int(input("1.단품 2.일반세트 3. 라지세트\n선택 : "))
    print(burger_inform_list)
    print("-"*30)
    check_burger = {}
    if choice == 1:     # 단품
        check_burger[1] = burger_inform_list[0]
        check_burger[2] = burger_inform_list[1]
        return check_burger
    else:
        side = print_menu(dict_set_side)
        drink = print_menu(dict_set_drink)
        if choice == 2:     # 일반 세트
            check_burger[1] = burger_inform_list[0]     # 버거 이름
            check_burger[2] = dict_set_side[side][0]
            check_burger[3] = dict_set_drink[drink][0]
            check_burger[4] = burger_inform_list[1] + 2000 + dict_set_side[side][1]
        elif choice == 3:
            check_burger[1] = burger_inform_list[0]     # 버거 이름
            check_burger[2] = dict_set_side[side][0] + 'L'
            check_burger[3] = dict_set_drink[drink][0] + 'L'
            check_burger[4] = burger_inform_list[1] + 2500 + dict_set_side[side][1]
        return check_burger


def check(check_list):
    while True:
        total = check_list[-2] * check_list[-1]
        for i in check_list[:-2]:
            print(f"{i}", end=" ")
        print(f"{check_list[-2]}원 {check_list[-1]}개 \n합계 금액 : {total}원")
        choice = int(input("1. 수량+ 2. 수량- 3.장바구니 담기\n선택 : "))
        if choice == 1 and check_list[-1] < 9:
            check_list[-1] += 1
        elif choice == 2 and check_list[-1] >1:
            check_list[-1] -= 1
        elif choice == 3:
            break
    print(check_list, total)
    return check_list



def wish_list(component_list):            # 장바구니 담기
    price = 0
    menu = component_list[0]
    price += component_list[1]


# 키오스크 작동
while True:
    # 포장 매장 선택
    # a = int(input("1.매장식사 2.포장 : "))
    a = 1

    # 카테고리 출력
    while True:
        # print(f"{dict_category}\n{list(dict_recommen.values())}")
        category = print_menu(dict_category)
        # category = int(input("선택: "))
        if category == 1:
            continue
        # 버거 메뉴
        elif category == 2:
            burger_menu = print_menu(dict_burger_menu)
            check_burger = []
            if burger_menu == 1:
                burger = print_menu(dict_burger_sig)
                check_burger = component(dict_burger_sig[burger])
            elif burger_menu == 2:
                burger = print_menu(dict_burger_beef)
                check_burger = component(dict_burger_beef[burger])
            elif burger_menu == 3:
                burger = print_menu(dict_burger_chi)
                check_burger = component(dict_burger_chi[burger])
            elif burger_menu == 4:
                burger = print_menu(dict_burger_bul)
                check_burger = component(dict_burger_bul[burger])

            check_burger = list(check_burger.values())
            check_burger.append(1)  # 기본 수량 1
            check(check_burger)     # 고른 버거 메뉴 저장
        # 드링크 메뉴
        elif category == 3:
            drink_menu = print_menu(dict_drink_menu)
            check_drink = []
            if drink_menu == 1:         # 커피
                drink = print_menu(dict_drink_cof)
                check_drink = dict_drink_cof[drink]
                # 수량 확인
                # 장바구니 추가
            elif drink_menu == 2:       # 탄산
                drink = print_menu(dict_drink_soft)
                check_drink.append(dict_drink_soft[drink])
                # 수량 확인
                # 장바구니 추가
            elif drink_menu == 3:       # 주스
                drink = print_menu(dict_drink_jui)
                check_drink.append(dict_drink_jui[drink])
                # 수량 확인
                # 장바구니 추가
            elif drink_menu == 4:       # 쉐이크
                drink = print_menu(dict_drink_sha)
                check_drink.append(dict_drink_sha[drink])
                # 수량 확인
                # 장바구니 추가

            check_drink.append(1)       # 기본 수량 1
            check(check_drink)          # 고른 음료 메뉴 저장

        # 사이드 메뉴
        elif category == 4:
            side_menu = print_menu(dict_side_menu)
            pass
        # 디저트 메뉴
        elif category == 5:
            disert_menu = print_menu(dict_disert_menu)
            pass
        # 해피밀
        elif category == 6:
            hm_menu = print_menu(dict_hm)
            pass
