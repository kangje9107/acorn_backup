-- 20 Dec
-- sample2.sql
-- 관계형 DB table == 수학의 '집합' 을 확인해보자 

-- Pseudo Column (의사 컬럼) : ROWID, ROWNUM 
-- --> 실제 테이블에 존재하지않지만 모든 테이블에서 사용 가능한 컬럼
-- --> ROWNUM: 행 번호 출력
--         **진짜 행번호가 아님** SELECT절에 의해 뽑히면서 붙여짐. 
-- --> ROWID : 행의 물리주소(숫자값)를 논리로 바꾼 값
--          행의 실제 물리주소 및 unique한 식별자. but **언제든 가변적임** Ex) by oracle partitioning

-- Oracle partitioning : 대용량 데이터 저장시 데이터를 가변적으로 쪼개어 저장, 실제 물리주소는 임의로 바뀜.
-- 실제 물리적인 레코드가 여러개로 쪼개서 들어가므로, 물리적 행의 번호는 엉망 진창임. 
-- 그러나 이게 논리적 SQL 처리 결과에 영향을 주진 않음 (Oracle 설계)
-- ex) 년/월/일 1억개의 행을 나누어 각 일자별로 다른 *.dbf 파일에 쪼개서 저장하게 하는 기능.  


SELECT    
    ROWID,          
    ROWNUM,         --> SELECT에 의해 붙여지므로 order by를 거치면서 뒤죽박죽이 되는 것  
    last_name,
    salary
FROM
    employees
ORDER bY 
    salary;

