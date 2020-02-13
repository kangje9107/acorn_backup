-- 과제11.sql

-- 1. 사원들의 업무별 전체 급여 평균이 $10,000보다 큰 경우를 조회하여 업무별 급여 평균을 출력하시오. 
-- 단 업무에 사원(CLERK)이 포함된 경우는 제외하고 전체 급여 평균이 높은 순서대로 출력하시오.(Oracle HR 계정 사용)

DESC employees;

SELECT job_id
FROM employees;

SELECT job_id, avg(salary)
FROM employees
-- WHERE job_id NOT LIKE '%CLERK'
GROUP BY job_id
HAVING
    avg(salary) > 10000
    AND job_id NOT LIKE '%CLERK'
ORDER BY avg(salary) DESC;

-- 2. 모든 사원의 연봉을 표시하는 보고서를 작성하려고 한다.
--    보고서에 사원의 이름과 성(Name으로 별칭), 급여, 수당여부에 따른 연봉을 포함하여 출력하시오.
--    수당여부는 수당이 있으면 “Salary + Commission”, 수당이 없으면 “Salary only”라고 표시하고,
--    별칭은 적절히 붙이시오. 또한 출력 시 연봉이 높은 순으로 정렬하시오. 
--    (Oracle HR 계정 사용, NVL2 함수도 조사하여 사용할 것)

DESC employees;

SELECT
    first_name || ' ' || last_name 
    AS "Name",
    salary 
    AS "Salary",
    (salary * ( 1 + nvl(commission_pct, 0))) * 12
    -- (salary * (1 + decode(commission_pct, NULL, 0, commission_pct))) * 12 
    AS "Annual Salary",
    -- decode(commission_pct, NULL, 'Salary only', 'Salary + Commission')
    nvl2(commission_pct, 'Salary + Commission', 'Salary only') 
    AS "Commission"
FROM
    employees
ORDER BY
    "Annual Salary" DESC;
