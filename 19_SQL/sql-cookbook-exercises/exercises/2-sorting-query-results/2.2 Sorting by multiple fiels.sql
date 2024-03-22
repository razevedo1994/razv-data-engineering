/*
 * Problem: You want to sort the rows from EMP first by DEPTNO ascending,
 * then by salary descending.
 *  
 */

select empno, deptno, sal, ename, job
from emp
order by 2, 3 desc