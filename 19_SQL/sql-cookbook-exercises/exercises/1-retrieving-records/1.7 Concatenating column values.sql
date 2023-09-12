/*
 * Problem: You want to return values in multiple columns as one column.
 * For example, you would like to produce this result set from a query
 * against the EMP table:
 * 
 *  CLARK WORKS AS A MANAGER
 *  KING WORKS AS A PRESIDENT
 *  MILLER WORKS AS A CLERK
 */

 select ename||' WORK AS A'||job as msg
 from emp
 where deptno = 10