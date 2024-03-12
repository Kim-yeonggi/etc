/*
데이터 변경을 위한 SQL 문
조회는 SELECT로 시작했고
데이터의 입력/수정/삭제 기능 중
입력은 INSERT
수정은 UPDATE
삭제는 DELETE
INSERT INTO 테이블 (열 열 열 열 ) VALUES (값 값 값 값);


AUTO_INCREMENT : 자동 증가 속성
AUTO_INCREMENT 는 열을 정의할 때 1부터 증가하는 값을 입력해준다.
AUTO_INCREMENT로 지정된 열은 데이터를 입력하는 INSERT 단계에서 해당 열이 없다고 생각하고 입력하면 되고, AUTO_INCREMENT는 항상 PK여야 한다.
INT 타입으로 지정

[열이름 INT AUTO_INCREMENT PRIMARY KEY] 형식



USE market_db;
-- CREATE TABLE testTable(test_id INT, test_name CHAR (4), age INT);
-- INSERT INTO testTable VALUES(1, "테스트", 27);

-- CREATE TABLE testtable2(test_id INT AUTO_INCREMENT PRIMARY KEY, test_name char(4), age INT);
INSERT INTO testtable2 VALUES(NULL, 't1', 24);
INSERT INTO testtable2 VALUES(NULL, 't2', 25);
INSERT INTO testtable2 VALUES(NULL, 't3', 26);
select * from testtable2;


-- SELECT last_insert_id()

USE market_db;
CREATE TABLE city_popul (city_name CHAR(35), population INT);
INSERT INTO city_popul SELECT Name, Population FROM world.city;
-- 타 데이터베이스에 접근시 데이터베이스명.테이블명 으로 접근 가능

*/

/*
-- UPDATE : 데이터의 수정
-- 데이터가 변경되는 경우 UPDATE를 사용한다.
-- UPDATE 테이블명 SET 열1=값1, 열2=값2 ... WHERE 조건;   형태로 사용한다.

USE market_db;
UPDATE city_popul SET city_name = '런던' WHERE city_name = 'LONDON';
SELECT * FROM city_popul WHERE city_name = '런던';

select * from city_popul;


USE market_db;
UPDATE city_popul SET population = population/100;
select * from city_popul limit 5;
*/


/*
데이터 삭제 : delete
테이블의 행 데이터를 삭제해야하는 경우 사용
delete from 테이블 where 조건;  형태로 사용


delete from city_popul where city_name like 'New%';

1. delete : 행을 삭제
2. drop : 테이블 삭제
3. truncate : delete와 동일하지만 속도가 빠른 편 : 구조만 남는다. : delete와 다르게 where(조건식) 사용 불가

*/

/* 
# SQL 데이터 타입
# 정수형 타입
1. TINYINT : 1 byte		-128 ~ 127 : 2의 8제곱 : 256
	1-1 : TINYINT UNSIGNED : 0 ~ 255
2. SAMLLINT : 2 byte	
3. INT : 4 byte
4. BIGINT : 8 byte

# 문자형
CHAR(n) : n 자리 문자 : 고정형 길이
VARCHAR(n) : n자리 문자 : 가변형 길이

CHAR(10)에 ABC배치해도 10자리 차지			 : 최대 설정 가능 길이 255
VARCHAR(10 ABC배치하면 가변적으로 3자리 차지	 : 최대 설정 가능 길이 : 16383

CHAR() 타입이 기본 구동 속도가 빠르다.

# TEXT
char 타입으로 저장 불가능한 매우 긴 텍스트 저장 용도
1~65535 글자까지 저장 가능

# LONGTEXT
1~4294967295 글자까지 저장 가능

# BLOB : Binary Long OBject
이진데이터를 저장하는 용도 (영상, 이미지)
1~65535 까지 가능

LONGTEXT, LONGLBLOB 은 용량으로 4GB 까지 저장 가능


# 실수형
DATE 3바이트 : 날짜만 저장 	yyyy-mm-dd 형식
TIME 3바이트 : 시간만 저장 	HH:MM:SS 형식
DATETIME 8바이트 : 날짜와 시간 저장 	YYYY-MM-DD HH:MM:SS 형식

# JOIN 조인
# 두 테이블을 서로 묶어서 하나의 결과를 만들어 내는 것
# 마켓 db의 buy테이블과 member 테이블을 연결하는 것 : 조건을 활용

두 테이블을 조인하기 위해 일대다(1:n) 관계가 형성되는데,
market 데이터 베이스의 member 테이블의 아이디를 기본키로 지정.
buy테이블의 아이디는 기본키가 아닌 외래키(FK)로 지정.



# 조인 문법 기본 형태
SELECT 열 FROM 1번테이블 JOIN 2번테이블 ON 조인조건 WHERE 검색 조건


USE market_db;
SELECT * FROM buy Join member ON buy.mem_id = member.mem_id WHERE buy.mem_id = "BLK";
SELECT * FROM buy Join member ON buy.mem_id = member.mem_id;

*/

SELECT DISTINCT buy.mem_id, prod_name, addr, CONCAT(phone1, phone2) "연락처" FROM buy JOIN member ON buy.mem_id = member.mem_id;



























