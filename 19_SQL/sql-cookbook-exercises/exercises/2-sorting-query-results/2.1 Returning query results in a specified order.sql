/*
 * Problem: You want to display the names, jobs, and salaries of employees
 * in departament 10 in order based on their salary (from lowest to highest).
 *  
 */

select ename, job, sal
from emp
where deptno = 10
order by sal