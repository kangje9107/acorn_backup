-- 19 Dec

-- SQL: FROM 키워드는 생략불가. 
-- Oracle에서 ''와 "" 혼용 불가
-- -- ''는 literal(문자열)의 의미
-- -- ""는 AS <alias>의 공백삽입 등때 사용
-- SQL의 동등비교 연산자는 = 한개임.


-- **** SELECT 문법  ****
-- SELECT [DISTNCT] {*(all의 뜻) or column [AS Alias] , ...}
-- FROM <table>

-- **** SELECT 실행순서 ****
-- SELECT    (5) 
-- FROM      (1) - 생략불가
-- [WHERE]   (2) - 1st filtering 
-- [GROUP BY](3)
-- [HAVING]  (4) - 2nd 
-- [ORDER BY](6) - sorting results

-- HR.XE로 실행

SELECT *
FROM employees;

SELECT * 
FROM departments;

SELECT employee_id, last_name, hire_date, salary
FROM employees;

-- 1. 산술연산자  + SELECT문

SELECT salary, salary + 100 FROM employees;
SELECT salary, salary - 100 FROM employees;
SELECT salary, salary * 100 FROM employees;
SELECT salary, salary / 100 FROM employees;

-- 2. FROM <dummy table : SYS.DUAL> 
-- sys account 소속 계정
-- 연산만 할 때 사용 - SELELCT 문의 연산을 위해 daul 이라는 dummy table 제공

SELECT 245 * 567
FROM dual;

DESC sys.dual;
DESC dual;

-- 3. AS : 컬럼에 alias 만들기
-- SELECT <컬럼> [AS] <aslias> FROM <table> : AS 키워드 생략가능, 비추 
SELECT last_name AS 이름, salary 월급, salary *12 AS 연봉
FROM employees; 

-- 3-1. alias에 공백/특수문자 삽입하기 : "" 사용
SELECT last_name AS "사원 이름", salary "사원 월급", salary*12 AS "연 봉"
FROM employees;

-- 4. Missing Value(결측치) : NULL 
-- 값이 없다는 의미의 literal, 수학적으로는 무한대의 값을 가지므로 연산불가
SELECT employee_id, last_name, job_id, commission_pct 
FROM employees;

-- 4-2. NULL 연산 >> NULL이 됨
SELECT last_name 이름, salary 월급, commission_pct 수수료, 
        salary * 12 + salary * commission_pct AS 연봉
FROM employees;

-- 5. 결측치 처리 = NULL 처리 
-- 함수 : NVL(NULL 포함 컬럼, 선정 defaultVAlue) 
SELECT last_name 이름, salary 월급, commission_pct 수수료, 
        salary * 12 + NVL(commission_pct, 0) AS 연봉
FROM employees;

-- 6. || : concatenation operator
SELECT last_name || salary AS "이름 월급"
FROM employees;

SELECT
    last_name ||
    ' 의 직업은 ' ||
    job_id 
    AS "직원별 직급"
FROM 
    employees
WHERE  
    last_name = 'Smith'; 

-- 7. 중복값 제거 : DISTINCT 
-- DISTINCT <col, col..> 2개 이상의 컬럼이면, 모든 컬럼의 값이 같아야 서로 중복값으로 인식함. 
SELECT DISTINCT 
    last_name, first_name
FROM
    employees;

