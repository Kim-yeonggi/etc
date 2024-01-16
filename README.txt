# 사용법
function(length=1, reverse=False, decimal_point=2, *not_used_args)

length는 float 형 / reverse는 bool 형 / decimal_point는 int 형을 입력


# 매개변수
length : 변환 시킬 길이값 (미입력시 1로 할당)
reverse : 변환 단위 설정
	기본(False) : 앞 단위 -> 뒤 단위 변환
	ex) meter2yard(1) : meter를 yard 단위로 변환

	True 라면 뒤 단위를 앞 단위로 변환
	ex) meter2yard(1, True) : yard를 meter 단위로 변환

decimal_point : 출력할 값의 소수점 자리수 설정(미입력시 소수점 두번째 자리까지 출력)

not_used_args : 사용되지 않는 매개변수(오류 방지용)


# 함수 종류
centimeter2inch(length, reverse, decimal_point)  # 센티미터 단위와 인치 단위를 상호 변환하는 함수

meter2yard(length, reverse, decimal_point)  # 미터와 야드 단위를 상호 변환하는 함수

meter2feet(length, reverse, decimal_point)  # 미터와 피트 단위를 상호 변환하는 함수

feet2yard(length, reverse, decimal_point)  # 피트와 야드 단위를 상호 변환하는 함수

inch2feet(length, reverse, decimal_point)  # 피트와 인치 단위를 상호 변환하는 함수

kilometer2mile(length, reverse, decimal_point)  # 킬로미터와 마일 단위를 상호 변환하는 함수

yard2mile(length, reverse, decimal_point)  # 야드와 마일 단위를 상호 변환하는 함수