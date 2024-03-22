/*
 * Problem: You want to sort the results of a query by specific parts of a string.
 * For example, you want to return employee names and jobs from tabke EMP and sort
 * by the last two characters in the JOB field.
 *  
 */

select ename, job
from emp
order by substring(job, length(job)-2) 