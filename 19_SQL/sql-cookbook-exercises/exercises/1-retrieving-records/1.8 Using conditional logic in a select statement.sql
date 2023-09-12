/*
 * Problem: You want to perform IF-ELSE opration on values in your SELECT statement.
 * For example, you would like to produce a result set such that if an employee is paid
 * $2,000 or less, a message of "UNDERPAID" is returned; if an employee is paid $4,000
 * or more, a message of "OVERPAID" is returned; and if they make somewhere in between, then 
 * "OK" is returned.
 *  
 */

 select 
    ename, 
    sal,
    case when sal <= 2000 then 'UNERPAID'
        when sal >= 4000 then 'OVERPAID'
        else 'OK'
    end as status 
from emp