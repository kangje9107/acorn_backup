-- 20 Dec

--unistr() : 매개변수문자를 unicode화함

-- ------------------------------------------------------
-- 1. 단일(행) (반환)함수
-- ------------------------------------------------------
-- 단일(행) (반환)함수의 구분:
--
--  (1) 문자 (처리)함수 : 문자와 관련된 특별한 조작을 위한 함수
--  (2) 숫자 (처리)함수 : 
--  (3) 날짜 (처리)함수
--  (4) 변환 (처리)함수
--  (5) 일반 (처리)함수
-- ---------------------------------------------------

--===================================================
--      문자처리함수
--===================================================

-- 1. initcap() : 첫글자 대문자화
SELECT 'ORACLE SQL', initcap('ORACLE SQL')
FROM dual;

SELECT email, initcap(email)
FROM employees;

-- 2. upper() : 모든 글자 대문자화
SELECT 'oracle sql', upper('oracle sql')
FROM dual;

SELECT last_name, upper(last_name)
FROM employees;

-- -- 장점 : 데이터가 어떻게 저장됐는지를 모르므로 일괄 upper로 검색 용이
-- -- 단점 : 해당 col에 함수를 적용했으므로 index 사용 불가
SELECT last_name, salary
FROM employees
-- -- WHERE upper(last_name) = 'KING';
WHERE last_name = initcap('KING'); --> 저장된 형식을 알고 사용한다고 가정 

-- 3. LOWER() : 소문자화 
SELECT last_name, lower(last_name)
FROM employees;

-- 4. CONCAT() : 두 개를 문자열로 연결 () || 연산자와 비슷 ), 2개밖에 안되서 중첩해야함 ㅠ 잘안씀
-- -- 숫자나 날짜를 concat해도 문자열로 바뀌어서 붙음 
SELECT last_name || ' ' || salary , concat(concat(last_name, ' '), salary) 
FROM employees;

-- 5.  문자열 길이 반환 함수
-- -- LENGTH(col) : 문자열 길이 반환 *
-- -- LENGTHB(col) : 문자열 Byte 반환 *
-- -- LENGTHC(col) : Unicode 문자 개수 반환
SELECT last_name, length(last_name)
FROM employees;

SELECT 
    unistr('X'), 
    lengthb(unistr('X')) lengthb,
    lengthc(unistr('X')) lengthc,
    length('X') lengthX,
    length('X') lengthXB,
FROM dual;

SELECT 
    '한글', 
    length('한글') length,
    lengthb('한글') lengthb,
    lengthc('한글') lengthc
FROM dual;

--6. INSTR() : 특정 문자열의 시작 위치(인덱스) 반환
-- -- instr(문자열, 찾을문자열, offset, occurrence) : offset위치부터 검색하고, 검색한 occurence 번째의 결과(인덱스) 반환해라
-- -- 못찾으면 0 반환.

SELECT
    --    '123456'      
    instr('MILLER', 'L', 1, 2) --> MILLER의 1번째글자부터 'L'을 찾아서 2번째나오는 'L'을 가져와라
FROM dual;

-- 7. substr() : 부분문자열 반환
-- --> substr(str, offset, 떼어낼 글자수 ) --> str를 offset 번째 글자부터 X개 떼어내라
SELECT substr('123456-1234567', 8, 3)
FROM dual;

-- --> 안좋은 예 : SQL*developer 의 날짜:  YY/~ 순으로 지정되있지만 여기서는 또 순서가 바뀐다. 
SELECT 
    hire_date as 입사일,
    substr(hire_date, 1, 2)  AS 입사년도 
FROM employees;

-- --> 올바른 예 : to_char(date) 하면 형식이 고정되서 나옴
SELECT 
    to_char(hire_date) as 입사일,
    substr( to_char(hire_date), 8, 2 ) AS 입사연도 
FROM employees;

-- 8. REPLACE() 문자 처리 함수
SELECT replace('JACK and JUE', 'J', 'BL') --> 모든 J를 BL로 바꿔라
FROM dual;

-- 9. LPAD() / RPAD()
-- --> LPAD(str, 전체자릿수, 채울문자) str의 왼쪽에 채울문자를 채워서 총 (전체자릿수)만큼 글자를 만들어라

SELECT 
    Rpad(substr('900303-1234567',1, 8),14,'*') AS 주민번호
FROM dual;
-- 이거 두개가 같은 결과. 
SELECT 
    substr('900303-1234567',1,8) || '******' AS 주민번호
FROM dual;


-- 11. TRIM()/ LTRIM () / RTRIM()

-- 11-1. TRIM() 문법
-- (1) TRIM( LEADING 'str' FROM 컬럼|표현식 ) : 왼쪽에서 삭제
-- (2) TRIM( TRAILING 'str' FROM 컬럼|표현식 ) : 오른쪽에서 삭제 
-- (3) TRIM( BOTH 'str' FROM 컬럼|표현식 )
-- (4) TRIM( 'str' FROM 컬럼|표현식 ) : BOTH랑 같음

SELECT trim( LEADING '0' FROM '00012345689780000')
FROM dual;

SELECT trim( '0' FROM '00012345689780000')
FROM dual;

-- --> ltrim(str, 지정문자) : 왼쪽에 연속되어있는 지정문자 전부 삭제. 
-- -->                      지정문자 default : ' ' 공백삭제 
SELECT ltrim('MMMMIMMMMLLER','M')
FROM dual;

SELECT 
    ltrim(' MILLER '),
    length( ltrim(' MILLER '))
FROM dual;

SELECT 
    rtrim('MILLERER', 'R')
FROM dual;

