select addr, debut_date, mem_name from member;
select addr 주소, debut_date "데뷔 일자", mem_name 그룹명 from member;

select * from member where mem_name = "트와이스";
select * from member where mem_number <= 5;

/*
select mem_id, mem_name, height from member where height >= 165 and mem_number >= 5;
select mem_id, mem_name, height from member where height between 163 and 165;
select mem_name, addr from member where addr = '경기' or addr = '전남' or addr = '경남';
select mem_name, addr from member where addr in ('경기', '전남', '경남');
SELECT * from member where addr like '서%';		-- 특정 문자열 포함 / % : 무엇이든 허용, 가장 앞글자는 '서'롤 시작
select * From member;
select * from member where addr like '_울';	-- 뒷 글자가 '울'로 끝남
*/

select height from member where mem_name = '에이핑크';	-- 164 출력
select mem_name, height from member where height > (select height from member where mem_name = '에이핑크');

-- 서브쿼리 select 안에 또 다른 select가 들어가는 구조 

-- select문과 조합 예약어
-- 결과 정렬을 위한 order by
-- 결과 개수 제한하는 limit
-- 중복 데이터 제거 distinct
-- group by 집계 기능
-- 를 조합하여 사용가능하다.

-- select 열 이름 from 테이블이름 where 조건식 group by 열이름 having 조건식 order by 열이름 limit 숫자 형태 조합 가능

-- 1. order by
-- 오더 바이 짧은 결과의 값이나 개수에 대해서는 영향을 미치지 않지만, 결과가 출력되는 순서를 조절한다.

select mem_id, mem_name, debut_date from member order by debut_date;
-- mem_id, mem_name, debut_date를 출력하되 debut_date 가 빠른 순서대로 출력된다.
-- 출력 순서를 거꾸로 뒤집으려면 asc를 desc로 변경 (기본정렬 값이 asc[오름차순]로 지정되어 있음)
select mem_id, mem_name, debut_date from member order by debut_date desc;
-- desc로 지정하면 내림차순 정렬


-- order by절은 where 절과 함계 사용할 수 있다.
-- ex) 평균 키가 164이상인 회원 출력
select mem_id, mem_name, height from member where height >= 164 order by height desc;

select mem_id, mem_name, debut_date, height from member where height >= 164 order by height desc, debut_date asc;
-- 164 이상회원의 정보를 키가 큰 순으로 정렬 & 데뷔일자가 빠른 순으로 정렬
-- 두가지 정렬 방식 동시 사용
-- 키가 동일한 167인 두 회원의 정렬에 데뷔일자 순 정렬이 적용되었음

select * from member limit 3;

-- limit 은 출력 수 제한으로 limit 3 설정시 3행까지만 출력
-- limit 은 보통 특정 정렬을 한 후 적용하는 경우가 대부분
-- limit 3 : 3행 표현
-- limit 0,3 : 0번째 행부터 3개 표현
-- limit 3,4 : 3번째 행부터 4개 표현

select mem_name, debut_date from member order by debut_date limit 3;
-- 데뷔일로 정렬 후 상위 3개 출력
select mem_name, debut_date, height from member order by height desc limit 3,2;
-- 키가 큰 순으로 정렬한 3번째부터 2개 출력

-- select addr from member;
-- 멤버 테이블의 모든 행에 대한 addr 출력
-- select distinct addr from member;
-- 중복제거 distinct 사용


-- select amount from buy order by mem_id;

-- group by 와 함계 사용되는 집계함수
-- sum() 합
-- avg() 평균
-- min() 최소
-- max() 최대
-- count() 행의 수
-- count(distinct) 행의 수 (중복 제외)

select mem_id "회원명", sum(amount) '총 구매 수량' from buy group by mem_id;


select mem_id, sum(price*amount) from buy group by mem_id;
-- sum 집계 함수 내 price*amount 식으로 총 비용 계산 집계

select avg(amount) from buy;

select mem_id, avg(amount) from buy group by mem_id;


select count(*) from member;

-- 회원 테이블에서 연락처가 있는 회원 수 카운트
select count(phone1) "연락처가 있는 회원" from member;

select mem_id, sum(price*amount) from buy group by mem_id;

-- select mem_id, sum(price*amount0) from buy where sum(price*amount) > 1000 group by mem_id;		-- 오류
-- 그룹 바이로 묶어 집계처리 결과에 대한 조건식은 where 사용 X

select mem_id, sum(price*amount) from buy group by mem_id having sum(price*amount) > 1000 order by sum(price*amount) desc;
-- having 절로 조건을 지정 가능하고 having은 group by 뒤에 위치
-- 집계 함수에 대한 조건은 where가 아닌 having을 사용한다.































