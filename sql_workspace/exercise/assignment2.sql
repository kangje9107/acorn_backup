--1 
-- Select rows from a Table

--1. HR부서에서, 예산편성 문제로, 급여정보 보고서를 작성하려고 한다.    
--   사원정보에서, 급여가 $7,000~$10,000 범위 이외인 사람의 이름과 
-- 성(Name으로 별칭) 및 급여를, 급여가 적은 순서로 출력하시오.

DESC employees;

SELECT 
    concat(first_name, last_name) AS "Name", 
    salary
FROM 
    employees
WHERE 
    salary NOT BETWEEN 7000 AND 10000  
ORDER BY salary ASC;

--2
SELECT 
    first_name || ' ' || last_name AS "Name", 
    salary, 
    job_id,
    commission_pct
FROM employees
WHERE (commission_pct IS NOT NULL) -- 수당 =commission 경우
ORDER BY 
    salary DESC, 
    nvl(commission_pct,0) DESC;

--3 
SELECT 
    EMPLOYEE_ID,
    first_name || ' ' || last_name AS "Name",
    salary,
    round(salary * 1.123) AS "Increased Salary"
FROM 
    employees
WHERE
    DEPARTMENT_ID = 60;