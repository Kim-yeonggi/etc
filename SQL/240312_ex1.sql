/*
학생의 이름 / 나이 / 키 / 연락처가 담긴 학생 테이블을 만들고
학생의 이름: PK, NN


1. 학생의 이름순으로 정렬
2. 학생의 나이 대비 키가 큰 순으로 정렬
3. 학생의 총 인원 수 출력
4. 나이가 가장 어린 학생 2명 출력
*/

drop database if exists students;
create database students;

USE students;
create table student
(	stu_name	char(8) not null primary key,
	stu_age 	int,
    stu_height	int,
    stu_pn		char(11)
);
insert into student values('김ㅇㅇ', 22, 160, '01012345678');
insert into student values('이ㅇㅇ', 24, 175, '01012345678');
insert into student values('박ㅇㅇ', 21, 164, '01012345678');
insert into student values('최ㅇㅇ', 21, 181, '01012345678');
insert into student values('나ㅇㅇ', 24, 173, '01012345678');
insert into student values('장ㅇㅇ', 20, 157, '01012345678');
insert into student values('강ㅇㅇ', 27, 166, '01012345678');
insert into student values('진ㅇㅇ', 21, 178, '01012345678');



select * from student order by stu_name;
select stu_name, stu_age, stu_height, stu_pn, (stu_height/stu_age) from student order by (stu_height/stu_age);
select count(stu_name) '총 인원 수' from student;
select * from student order by stu_age limit 2;