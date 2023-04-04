/*
 * Problem: You have to return rows that satisfy multiple conditions
 * For example: If you would like to find all the employees in departament 10,
 * along with any employees who earn a commission, along with any employees in
 * departament 20 who earn at most $2,000.
 * 
 */

select
	*
from
	emp
where
	(deptno = 10
		or comm is not null
		or sal <= 2000)
	and deptno = 20
