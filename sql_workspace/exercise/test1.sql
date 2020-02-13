/*아래 SQL을 수행하는 Execute Plan을 생성하고 출력하시오.
   (SCOTT 계정으로 실행)
   (SQL) SELECT * FROM emp WHERE ename = 'SMITH';
   (문장아이디) sql1
*/














EXPLAIN PLAN
    SET statement_id= 'sql1'
    INTO plan_table
FOR 
    SELECT * 
    FROM emp
    WHERE ename = 'SMITH';


SELECT * FROM table(DBMS_XPLAN.display());

/*
아래 SQL 문을 통해, 쿼리에 사용되는 두 테이블(emp, dept)에 대한 사용 통계정보를
  수집하고자 한다. 테이블 사용통계정보 수집을 위한 일련의 SQL 문장을 실행하시오.
  (SCOTT 계정으로 실행)
  (보기) select empno, ename, d.deptno, dname 
        from emp e join dept d
        on e.deptno = d.deptno
        where empno = 7369
*/

















ANALYZE TABLE emp COMPUTE STATISTICS;
ANALYZE TABLE dept COMPUTE STATISTICS;

SELECT table_name, blocks, num_rows, avg_row_len
FROM USER_TABLES
WHERE table_name in ('EMP','DEPT')


/*
4. 더욱 효율적인 자원사용과 빠른 SQL 문장의 처리를 위해, 오라클의 병렬옵션(Parallel option)을 적용하
  고자 한다. 이를 위해, 우선 현재의 오라클 베포판과 버전에서, 병렬옵션이 설치되어 있는지를 확인하고
  자 한다. 이를 위한 SELECT 문장을 적절한 데이터 사전과 함께 작성하시오.
*/



















col parameter format a40
col value format a30
set linesize 120
select * from V$option where parameter like '%Parallel%';
/*
PARAMETER                           VALUE
------------------------------ --------------------
Parallel Server                          FALSE
Parallel backup and recovery     TRUE    
Parallel execution                     TRUE
Parallel load                             TRUE

*/








/*


비용기반 옵티마이저(CBO, Cost-Based Optimizer)에서 통계정보는 좋은 실행계획 선택에 매우 중요한
   요소로, 현재 시점에 통계정보가 없거나, 맞지 않는 통계정보를 최신의 통계정보로 재생성 해주는 작업
   을 오라클10g 이상부터 적용할 수 있다. 이때, 자동 통계정보 수집을 위한 환경을 설정해주는 PL/SQL
   block 으로 작성하시오. (SYS계정으로 수행)


Oralce 10g 부터 Optimizer가 CBO로 바뀌면서, oracle은 테이블 통계 정보를 수집하는 기능으로 default 로
 scheduler job에 등록 했다. 그런데 이게 data 가 많을 때는 수집 시간이 몇 시간씩 소요되면서 시스템 운영에 
 문제가 되는 경우도 있다.  예를 들면, 통계 정보 수집은 I/O를 대량으로 발생 시켜서 운영중이던 쿼리가 늦어지는 
 경우가 발생한다.
그래서 시스템 특성에 맞게 통계정보를 수집하는 package(procedure)를 제공하고 이 기능은 disable 시킨다.  
Disable 방법이 10g와 11g 가 다르다

*/









BEGIN
    DBMS_AUTO_TASK_ADMIN.DISABLE(
        CLIENT_NAME => 'AUTO OPTIMIZER STATS COLLECTION', 
        OPERATION => NULL
        WINDOW_NAME => NULL

    );
END;