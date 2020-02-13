-- 19 Dec

-- SQL : 문자열기호 ' ' 쓰지않음
-- Oracle Keywords 대문자, 개발자가 직접 만든 테이블은 소문자
-- 단축키: ctrl + shift + P + ENTER



--=============== SYS.XE로 실행=============================

-- 1. 비번번경 by sys account
-- ALTER <user> IDENTIFIED BY <비번>;
ALTER USER hr IDENTIFIED BY hr; 

-- 2. 계정 LOCK / UNLOCK
-- ALTER USER <user> LOCK;
ALTER USER hr ACCOUNT LOCK;
-- C:\app\sql_workspace>sqlplus hr/hr 

-- DESC <table>; table 스키마를 묘사하라
DESC DBA_USERS; -- DBA_USERS : 모든 사용자정보 담은 테이블 
SELECT USERNAME, ACCOUNT_STATUS FROM DBA_USERS;

-- UNLOCK
ALTER USER hr ACCOUNT UNLOCK;
DESC DBA_USERS;
SELECT USERNAME, ACCOUNT_STATUS FROM DBA_USERS;


-- 3. 1과 2를 한번에 사용 가능
ALTER USER hr ACCOUNT LOCK IDENTIFIED BY hr;
ALTER USER hr ACCOUNT UNLOCK IDENTIFIED BY hr;

ALTER USER hr IDENTIFIED BY hr ACOOUNT LOCK;
ALTER USER hr IDENTIFIED BY hr ACOUUNT UNLOCK;

DESC DBA_USERS;
SELECT USERNAME, PASSWORD, ACCOUNT_STATUS FROM DBA_USERS;





-- ================HR.XE로 실행. ==========================
-- DEPARTMENTS는 HR에 있는 table임.


DESC departments; 
DESCRIBE employees;
