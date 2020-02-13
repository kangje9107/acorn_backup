
--[1]
SELECT 
    employee_id, 
    first_name || ' ' || last_name AS Name,
    salary,
    job_id,
    hire_date,
    manager_id
FROM 
    employees;
--2.
SELECT 
    first_name || ' ' || last_name AS Name,
    job_id AS Job,
    salary AS Salary,
    salary*12 + 100 AS "Increase Ann_Salary",
    salary + 100 AS "Increase Salary"
FROM 
    employees;

--3.
SELECT 
     last_name || ': 1 Year Salary = $' || salary *12 AS "1 Year Salary"
FROM 
    employees;