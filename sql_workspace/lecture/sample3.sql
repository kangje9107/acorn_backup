-- 19 Dec
-- HR.XE


-- 함수를 적용하면 해당 col에 index 사용불가

-- **** 연산자 실행순서 ****
-- 괄호() >> 비교 >> NOT >> AND >> OR 
SELECT last_name, job_id, salary, commission_pct
FROM employees
WHERE
    (job_id = 'AD_MGR' OR job_id = 'MK_REP')
    AND commission_pct IS NULL
--    AND salary >= 4000 AND salary <= 9000;
    AND salary BETWEEN 4000 AND 9000; 


-- 1. comparison operator
-- -- 1. a = b: 동등비교연산자 
-- -- 2. a != b 
--       a <> b (비추)
--       a ^= b (비추)


-- 2. date format in ORACLE
-- to_date() : 날짜로 바꿔주는 함수  
SELECT DISTINCT 
    first_name, hire_date
FROM
    employees
WHERE 
    hire_date >= to_date('07/12/31', 'RR/MM/DD');
--  hire_date >= '07/12/31'; --> SQL Developer에서 가능 : 디벨로퍼가 한번 처리해줌


-- 3. BETWEEN  AND
-- start <= X <= end (범위도 포함!!)

SELECT 
    employee_id, 
    last_name, 
    salary, hire_date
FROM 
    employees
WHERE 
    salary  
        BETWEEN 
            7000 
            AND 8000;

SELECT 
    employee_id, 
    last_name, 
    hire_date
FROM 
    employees
WHERE
    hire_date 
        BETWEEN 
            to_date('07/12/31', 'RR/MM/DD') 
            AND to_date('08/12/31', 'RR/MM/DD');

-- 4. IN operator : 집합연산자 (= OR문과 같음)
-- WHERE <col> IN (value1, value2, ...) : 해당 컬럼에서 (집합) 원소에 해당하는 값이 있는 컬럼

SELECT employee_id, last_name, salary, hire_date
FROM employees
WHERE employee_id IN (100, 300, 200);

SELECT 
    employee_id, 
    last_name, 
    salary, 
    hire_date
FROM 
    employees
WHERE 
    hire_date IN (
        to_date('01/01/13', 'RR/MM/DD'), 
        to_date('07/02/07', 'RR/MM/DD')
    );

-- 5. OR, NOT, AND : 논리연산자
-- 같은 조건이라면 short-curcuiting 발생하므로, IN 집합연산자 사용이 효율적
SELECT 
    employee_id, 
    last_name, 
    salary, 
    hire_date
FROM 
    employees
WHERE 
    employee_id = 100
    OR employee_id = 200
    OR employee_id = 300;

-- 5-1. AND/OR/NOT 논리연산자 활용
SELECT 
    last_name, 
    job_id, 
    SALARY
FROM 
    employees 
WHERE 
    (job_id = 'IT_PROG') 
    AND (salary >= 5000);

-- 5-2. NOT 활용 
SELECT 
    last_name, 
    job_id, 
    SALARY
FROM 
    employees 
WHERE 
    NOT (salary < 20000);

-- 5-3. NOT IN ( ) <--> OR의 반대 (IN = OR )
SELECT count(*) 
FROM employees
WHERE salary NOT IN (9000, 8000, 6000);
--WHERE NOT (salary IN (9000, 8000, 6000)); 
-- 이 두가지 식은 optimizser상 같게 처리됨

-- 5-4. NOT LIKE 
SELECT count(*)
FROM employees 
WHERE last_name NOT LIKE 'J%';
--WHERE NOT last_name LIKE 'J%';

-- 5-5. NOT BETWEEN







-- 5-6. IS NULL 연산 ****** : NULL은 논리연산 불가
-- nvl()함수도 null을 다룰 수있으나 사용 X, 컬럼은 한번 조작하면 인덱스를 사용불가하므로. 
SELECT 
    last_name, 
    job_id, 
    commission_pct
FROM employees 
-- WHERE commission_pct = NULL; --> 오류발생:  NULL값은 비교 가능한 연산자가 아님 
WHERE commission_pct IS NULL; 
--WHERE nvl(commission_pct, -1) = -1;--> 매우비추 : INDEX 사용불가. 

SELECT 
    last_name, 
    job_id, 
    manager_id
FROM employees 
WHERE manager_id IS NOT NULL;

--5-7. IS NOT NULL 연산자



-- 6. LIKE operator : 패턴 매칭 연산자
-- : 여러 레코드에 다 해당하는 조건일 때 사용
-- -- 패턴문자열을 wildcard (x = wildcard 자리에 해당하는 문자갯수) 
-- -- (1) %     : x = 0 or x >= 0 (문자가 없을수도있고 몇개 있을수도있고)
-- -- (2) _     : x == 1  (단 한문자를 의미 )
-- -- (3) ? 
SELECT 
    employee_id, 
    last_name, 
    salary
FROM 
    employees
WHERE last_name LIKE '_'; -- 이름중에 _ 포함한 것 
--WHERE last_name LIKE '_____d'; -- 총 6자고 5번째 글자가 d인 이름
--WHERE last_name LIKE '%_%'; --1문자 이상인 모든 이름 
--WHERE last_name LIKE '%%'; -- 0개이상의 모든문자열 
--WHERE last_name LIKE '%'; -- 위랑 같음 

-- 7. ESCAPE 문
-- ESCAPE문자를 직접 지정 가능
-- ESCAPE 문자 바로 뒤의 한개의 wildcard만 탈출시킨다. 
SELECT 
    employee_id, 
    last_name, 
    job_id
FROM 
    employees
WHERE job_id LIKE '%E___' ESCAPE 'E';




