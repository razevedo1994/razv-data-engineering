/*
 * Problem: You have rows that contain nulls and would like to return
 * non-null values in place of those nulls.
 *  
 */

 select coalesce(comm, 0)
 from emp;