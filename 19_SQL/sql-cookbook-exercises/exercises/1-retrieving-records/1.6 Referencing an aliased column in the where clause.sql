select *
from (select	sal as salary,
				comm as commission
		from emp) x 
where salary < 5000