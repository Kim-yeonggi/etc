# 맥도날드 키오스크

dict_category = {1:"추천메뉴", 2:"버거메뉴",3:"음료메뉴",4:"사이드메뉴",5:"디저트메뉴",6:"해피밀"}
dict_burger_rec = {7:["빅맥", 4500],8:["1955버거",5000],9:["맥스파이시상하이버거",4500],10:["맥치킨버거",3500]}

# 버거 모음
dict_burger_menu = {7:"시그니처 버거",8:"비프 버거",9:"치킨&쉬림프 버거",10:"불고기&기타 버거"}
dict_burger_sig = {1:["그릴드머쉬룸버거",8000],2:["골든에그치즈버거",7800],3:["트리플어니언버거",7900]}
dict_burger_beef = {1:["빅맥",4500],2:["치즈버거",3500],3:["쿼터파운드버거",5000],4:["더블쿼터파운드 치즈버거", 6000]}
dict_burger_chi = {1:["맥스파이시상하이버거",4500],2:["맥치킨버거",3500],3:["맥크리스피디럭스버거",4300]}
dict_burger_bul = {1:["더블불고기버거",4000],2:["슈비버거",4500]}

# 버거 세트 - 사이드 음료
dict_set_side = {1:['감자튀김', 0], 2:['감자튀김+치즈스틱 2조각', 1500], 3:['치즈스틱',500]}
dict_set_drink = {1:['코카콜라'], 2:['스프라이트'], 3:['환타']}

# 음료 모음
dict_drink_menu = {7:"커피",8:"탄산음료",9:"과일음료",10:"쉐이크"}
dict_drink_cof = {1:["바닐라라떼",3000],2:["아메리카노",2000],3:["카페라떼",2500],4:['카푸치노',2500],5:['드립커피',1800]}
dict_drink_soft = {1:['코카콜라',1500],2:['환타',1500],3:['스프라이트',1500]}
dict_drink_jui = {1:['골드 맥피즈',2000],2:['자두천도복숭아 칠러',2500],3:['제주한라봉 칠러',2500]}
dict_drink_sha = {1:['초코쉐이크',2500],2:['바닐라쉐이크',2500],3:['딸기쉐이크',2500]}

# 사이드 모음
dict_side_menu = {7:'스낵랩', 8:'코울슬로', 9:'치즈스틱', 10:'맥너겟', 11:'치킨텐더', 12:'감자튀김', 13:'소스'}
dict_side_sw = {1:['토마토 치킨 스낵랩', 2000], 2:['상하이 치킨 스낵랩',2000]}
dict_side_col = {1:['코울슬로', 1500]}
dict_side_mcn = {1:['4조각', 3000], 2:['6조각', 4000]}
dict_side_cktd = {1:['2조각', 3500]}
dict_side_pot = {1:['S', 1000], 2:['M', 1300], 3:['L', 1500]}
dict_side_sau = {1:['디핑소스 스위트 앤 사워', 500], 2:['디핑소스 스위트 칠리', 500], 3:['디핑소스 케이준', 500]}
dict_side_chst = {1:['2조각', 1800] ,2:['4조각', 3000]}

# 디저트 모음
dict_disert_menu = {7:'라즈베리크림치즈파이', 8:'맥플러리'}
dict_disert_raspie = {1:['라즈베리크림치즈파이', 1500]}
dict_disert_mcf = {1:['오레오 맥플러리', 3000], 2:['초코오레오 맥플러리', 3000], 3:['딸기오레오 맥플러리', 3000]}

# 해피밀 모음
dict_hm = {7:['맥너겟 4조각 해피밀', 3500], 8:['햄버거 해피밀', 3500], 9:['불고기버거 해피밀', 3800]}

def print_menu(dict1):       # 번호 선택 및 메뉴 나열
    while True:
        for i in range(list(dict1.keys())[0], list(dict1.keys())[-1]+1):
            if type(dict1[i]) != list:
                print(f"{i}. {dict1[i]}")
            elif type(dict1[i]) == list and len(dict1[i]) >= 2:
                print(f"{i}. {dict1[i][0]} : {dict1[i][1]}원")
            else:       # 세트메뉴
                print((f"{i}. {dict1[i][0]}"))
        choice = int(input("선택 : "))
        print("*"*30)
        if choice not in list(dict1.keys()) and str(choice) not in "123456":
            continue
        else:
            break
    return choice

def component(burger_inform_list):    # 버거 메뉴 구성 선택
    while True:
        choice = int(input("1.단품  2.일반세트  3.라지세트\n선택 : "))
        # print(burger_inform_list)
        print("*"*30)
        check_burger = {}
        if choice == 1:     # 단품
            check_burger[1] = burger_inform_list[0]
            check_burger[2] = burger_inform_list[1]
            return check_burger
        elif choice == 2 or choice == 3:
            side = print_menu(dict_set_side)
            drink = print_menu(dict_set_drink)
            if choice == 2:     # 일반 세트
                check_burger[1] = burger_inform_list[0]     # 버거 이름
                check_burger[2] = dict_set_side[side][0]
                check_burger[3] = dict_set_drink[drink][0]
                check_burger[4] = burger_inform_list[1] + 2000 + dict_set_side[side][1]
            elif choice == 3:   # 라지 세트
                check_burger[1] = burger_inform_list[0]     # 버거 이름
                check_burger[2] = dict_set_side[side][0] + 'L'
                check_burger[3] = dict_set_drink[drink][0] + 'L'
                check_burger[4] = burger_inform_list[1] + 2500 + dict_set_side[side][1]
            return check_burger
        else:
            continue

def check(check_list):
    choice = 0
    while choice != 3:
        total = check_list[-2] * check_list[-1]
        for i in check_list[:-2]:
            print(f"{i}", end=" ")
        print(f"{check_list[-2]}원 {check_list[-1]}개 \n합계 금액 : {total}원")
        choice = int(input("1. 수량+ 2. 수량- 3.장바구니 담기\n선택 : "))
        print('*'*30)
        if choice == 1 and check_list[-1] < 9:
            check_list[-1] += 1
        elif choice == 2 and check_list[-1] > 1:
            check_list[-1] -= 1
        else:
            continue
    check_list.append(total)
    # print(check_list)
    return check_list

def print_category(n = dict_category):
    for i in range(1, len(dict_category.keys()) + 1):
        print(f"{i}. {dict_category[i]}")
    print("-"*30)

def wish_list(selected_list):
    # check_menu = list(selected_list.values())
    selected_list.append(1)
    check(selected_list)
    return selected_list

def total_list(selected_dict):
    total = 0
    p = True
    while p:
        print(f"{'#' * 11} 주문 내역 {'#' * 11}")
        for i in list(selected_dict.keys()):
            total += selected_dict[i][-1]
            print(f"{i}. {selected_dict[i][:-3]} {selected_dict[i][-3]}원 x{selected_dict[i][-2]}  합 : {selected_dict[i][-1]}원")

        print(f"총 결제 금액 : {total}원")
        print("-"*30)
        pay = int(input("1.수량변경  2.추가주문  3.품목삭제  4.완료\n선택 : "))
        if pay == 1:
            change = int(input("수량 변경할 메뉴를 선택 : "))
            while True:
                print(f"{selected_dict[change][:-3]}  {selected_dict[change][-3]}원  {selected_dict[change][-2]}개")
                num = int(input("1.+  2.-  3.완료\n선택 : "))
                if num == 1 and selected_dict[change][-2] < 9:
                    selected_dict[change][-2] += 1
                elif num == 2 and selected_dict[change][-2] > 1:
                    selected_dict[change][-2] -= 1
                elif num == 3:
                    selected_dict[change][-1] = selected_dict[change][-2] * selected_dict[change][-3]
                    break

        elif pay == 2:
            break
        elif pay == 3:
            pass
        elif pay == 4:
            p = False
            return p, selected_dict





# 키오스크 작동
while True:
    # 포장 매장 선택
    a = int(input("1.매장식사  2.포장 : "))
    print('*'*30)
    selected = {}
    p = True            # while문 조건으로 사용
    category = 1
    total = 0
    # 카테고리 출력
    # while True:
    while p:
        # print(category, "첫라인")
        if category == 1:
            print_category()
            for i in list(dict_burger_rec.keys()):
                print(f"{i}. {dict_burger_rec[i][0]} : {dict_burger_rec[i][1]}원")
            category = int(input("선택: "))
            print('*'*30)
        # 버거 메뉴
        if category == 2:
            # check_burger = []
            # while True:
            while p:
                print_category()
                burger_menu = print_menu(dict_burger_menu)
                # if burger_menu == 0:
                #     continue
                if burger_menu != 2 and burger_menu in dict_category.keys():
                    category = burger_menu
                    break
                elif burger_menu == 7:
                    burger = print_menu(dict_burger_sig)
                    check_burger = component(dict_burger_sig[burger])
                elif burger_menu == 8:
                    burger = print_menu(dict_burger_beef)
                    check_burger = component(dict_burger_beef[burger])
                elif burger_menu == 9:
                    burger = print_menu(dict_burger_chi)
                    check_burger = component(dict_burger_chi[burger])
                elif burger_menu == 10:
                    burger = print_menu(dict_burger_bul)
                    check_burger = component(dict_burger_bul[burger])
                else:
                    continue

                check_burger = list(check_burger.values())
                selected[len(selected)+1] = wish_list(check_burger)

                p, selected = total_list(selected)
                # while True:
                # while p:
                #     print(f"{'#'*11} 주문 내역 {'#'*11}")
                #     for i in list(selected.keys()):
                #         total += selected[i][-1]
                #         # if len(selected[i]) > 4:        # 세트 메뉴
                #         print(f"{i}. {selected[i][:-3]} {selected[i][-3]}원 x{selected[i][-2]}  합 : {selected[i][-1]}원")
                #
                #     print(f"총 결제 금액 : {total}원")
                #     pay = int(input("1.수량변경  2.추가주문  3.품목삭제  4.완료"))
                #     if pay == 4:
                #         p = False




        # 드링크 메뉴
        if category == 3:
            # while True:
            while p:
                print_category()
                drink_menu = print_menu(dict_drink_menu)
                # check_drink = []
                if drink_menu != 3 and drink_menu in dict_category.keys():
                    category = drink_menu
                    break
                elif drink_menu == 7:         # 커피
                    drink = print_menu(dict_drink_cof)
                    check_drink = dict_drink_cof[drink]
                    # 수량 확인
                    # 장바구니 추가
                elif drink_menu == 8:       # 탄산
                    drink = print_menu(dict_drink_soft)
                    check_drink = dict_drink_soft[drink]
                    # 수량 확인
                    # 장바구니 추가
                elif drink_menu == 9:       # 주스
                    drink = print_menu(dict_drink_jui)
                    check_drink = dict_drink_jui[drink]
                    # 수량 확인
                    # 장바구니 추가
                elif drink_menu == 10:       # 쉐이크
                    drink = print_menu(dict_drink_sha)
                    check_drink = dict_drink_sha[drink]
                    # 수량 확인
                    # 장바구니 추가
                else:
                    continue

                selected[len(selected)+1] = wish_list(check_drink)
                print(selected)

                p, selected = total_list(selected)

        # 사이드 메뉴
        if category == 4:
            # while True:
            while p:
                print_category()
                side_menu = print_menu(dict_side_menu)
                if side_menu != 4 and side_menu in dict_category.keys():
                    category = side_menu
                    break
                elif side_menu == 7:
                    side = print_menu(dict_side_sw)
                    check_side = dict_side_sw[side]
                elif side_menu == 8:
                    side = print_menu(dict_side_col)
                    check_side = dict_side_col[side]
                elif side_menu == 9:
                    side = print_menu(dict_side_chst)
                    check_side = dict_side_chst[side]
                elif side_menu == 10:
                    side = print_menu(dict_side_mcn)
                    check_side = dict_side_mcn[side]
                elif side_menu == 11:
                    side = print_menu(dict_side_cktd)
                    check_side = dict_side_cktd[side]
                elif side_menu == 12:
                    side = print_menu(dict_side_pot)
                    check_side = dict_side_pot[side]
                elif side_menu == 13:
                    side = print_menu(dict_side_sau)
                    check_side = dict_side_sau[side]
                else:
                    continue

                selected[len(selected)+1] = wish_list(check_side)
                print(selected)

                p, selected = total_list(selected)

        # 디저트 메뉴
        if category == 5:
            # while True:
            while p:
                print_category()
                disert_menu = print_menu(dict_disert_menu)
                if disert_menu != 5 and disert_menu in dict_category.keys():
                    category = disert_menu
                    break
                elif disert_menu == 7:
                    disert = print_menu(dict_disert_raspie)
                    check_disert = dict_disert_raspie[disert]
                elif disert_menu == 8:
                    disert = print_menu(dict_disert_mcf)
                    check_disert = dict_disert_mcf[disert]
                else:
                    continue

                selected[len(selected)+1] = wish_list(check_disert)
                print(selected)

                p, selected = total_list(selected)

        # 해피밀
        if category == 6:
            # while True:
            while p:
                print_category()
                hm_menu = print_menu(dict_hm)
                # dict_hm = {7: ['맥너겟 4조각 해피밀', 3500], 8: ['햄버거 해피밀', 3500], 9: ['불고기버거 해피밀', 3800]}
                if hm_menu != 6 and hm_menu in dict_category.keys():
                    category = hm_menu
                    break
                elif hm_menu in dict_hm.keys():
                    check_hm = dict_hm[hm_menu]
                else:
                    continue

                selected[len(selected)+1] = wish_list(check_hm)
                print(selected)

                p, selected = total_list(selected)

        # 추천메뉴
        if category in list(dict_burger_rec.keys()):
            while p:
                check_burger = component(dict_burger_rec[category])
                check_burger = list(check_burger.values())
                selected[len(selected)+1] = wish_list(check_burger)
                print(selected)
                print('*'*30)
                category = 1

                p, selected = total_list(selected)
                continue

        if category not in list(dict_burger_rec.keys()):
            category = 1
            continue
