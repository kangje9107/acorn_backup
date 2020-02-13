---20 Dec

--- 숫자처리 함수 --- 

-- 1. round() 지정한 자릿수 이하에서 반올림
-- Select rows from a Table

SELECT round(456.789, -1) -- 10의자리수 미만에서 반올림 
FROM dual;
-- 2. trunc() : 절삭
SELECT trunc( 456.789, -1)
FROM dual;
-- 3. mod() : 나머지 --> 홀/짞 구할 때 사용
SELECT mod(10, 0) --오류를 내지않고 나눗셈을 수행하지않음. 
--SELECT mod(10, 3)
FROM dual;

SELECT 
    EMPLOYEE_ID, LAST_NAME, SALARY
FROM EMPLOYEES
WHERE mod(EMPLOYEE_ID, 2) = 1;


-- 4. ceil() : 크거나 같은 정수값 반환
SELECT ceil(10.6)
FROM dual;

-- 5. floor

-- 6. sign() : 양수, 음수 , 0인지 알려줌. 
-- --> sign()함수는 비교연산자를 대체할 수 있음. 

SELECT sign(100), sign(-20), sign(0)
FROM dual;

-- --> 비교와 비슷함. 
SELECT EMPLOYEE_ID, LAST_NAME, SALARY
FROM EMPLOYEES
WHERE sign(salary-15000) != -1; 


