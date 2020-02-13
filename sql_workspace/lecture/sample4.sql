-- 20 Dec
-- 연산자 이어서 . . .


--INDEX : oracle index는 1부터 시작함 
-- 관계형 database 성질 : 집합과 같다. 
-- -- (1) 순서 보장 X
-- -- (2) 중복 불허 : 각 레코드마다 유니크한 기본키를 보유하고있으므로 중복은 없음. 

-- ORDER BY {column|표현식} [ASC|DESC]; 
-- --> 항상 가장 마지막에 수행됨
-- --> [ASC|DESC] : 생략가능한 정렬방식 지정(ascending/descending)


--1. 숫자 정렬
SELECT employee_id, last_name, job_id, salary
FROM employees
--ORDER BY salary; --> default : ASC(오름차순)
--ORDER BY salary ASC;
ORDER BY salary DESC;

-- 1.1 ORDER BY 절에 alias 사용
SELECT employee_id, last_name, job_id, salary+100 AS "월급"
FROM employees
ORDER BY 월급 DESC;
-- ORDER BY SALARY+100 DESC; --> 표현식일 경우 별칭을 써야하는 이유

-- 1.2 ORDER BY 절에 col index 사용
-- --> 불가피한거 아니면 비추. SELECT문 구성을 수정하면 인덱스가 변경되므로.
SELECT 
    employee_id,        --1 
    last_name,          --2
    job_id,             --3
    salary+100 AS "월급" --4
FROM employees
ORDER BY 4 DESC; 

-- 2.ORDER BY 절에 문자로 정렬
SELECT employee_id, last_name AS 이름, job_id, salary 
FROM employees
ORDER BY last_name ASC;

-- 3. 날짜 데이터 정렬
SELECT EMPLOYEE_ID, LAST_NAME, HIRE_DATE AS 입사일자
FROM EMPLOYEES
ORDER BY HIRE_DATE DESC;

-- 4. 다중 컬럼 정렬
SELECT EMPLOYEE_ID, LAST_NAME, salary ,HIRE_DATE AS 입사일자
FROM EMPLOYEES
ORDER BY 
    salary DESC,
    HIRE_DATE;

--5. NULL값 정렬
-- --> NULL값이 가장 큰 값으로 나옴.
SELECT  LAST_NAME, EMPLOYEE_ID, COMMISSION_PCT
FROM EMPLOYEES
ORder BY COMMISSION_PCT DESC; 

