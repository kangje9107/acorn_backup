
CREATE TABLE department9(
    deptno NUMBER(2),
    dname VARCHAR(15),
    loc VARCHAR2(15),

    CONSTRAINT dempartment9_dname_ck CHECK(dname IN('개발', '인사'))
);
INSERT into DEPARTMENT9 (deptno, dname, loc)
values (10, '개', '서울');

CREATE TABLE dept02(
    deptno number(2), 
    dname VARCHAR2(15), 
    loc VARCHAR2(15)
);

INSERT INTO dept02 ( deptno, dname, loc) values (10, '인사', '서울');
INSERT INTO dept02 ( deptno, dname, loc) values (20, '개발', '광주');
INSERT INTO dept02 ( deptno, dname, loc) values (30, '관리', '부산');
INSERT into dept02 ( deptno, dname, loc) values (40, '영업', '경기');

commit;

CREATE TABLE emp02(
    empno number(4)
        constraint emp02_empno_pk PRIMARY KEY, 
    ename VARCHAR2(15), 
    deptno number(2)
        CONSTRAINT emp02_deptno_fk REFERENCES dept02(deptno)
);

INSERT INTO emp02 (empno, ename, deptno) VALUES (10, 'John', 10);
INSERT INTO emp02 (empno, ename, deptno) VALUES (20, 'Smith', 20);
INSERT INTO emp02 (empno, ename, deptno) VALUES (30, 'Sam', NULL);
INSERT INTO emp02 (empno, ename, deptno) VALUES (40, 'Mike', 50);

CREATE TABLE emp03 (
    empno   NUMBER(4)
        CONSTRAINT emp03_empno_pk PRIMARY KEY,
    ename   VARCHAR2(15),
    deptno  NUMBER(2),

    constraint emp03_deptno_fk foreign key(deptno) REFERENCEs dept02(deptno)
);