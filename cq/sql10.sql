create database s;
use s;

create table employees (emp_id int,emp_name varchar(50),department varchar(50),salary int,hire_date date);

insert into employees values
(1,'arun','it',90000,'2024-01-10'),
(2,'bala','it',80000,'2024-02-15'),
(3,'charan','it',80000,'2024-03-20'),
(4,'divya','hr',75000,'2024-01-12'),
(5,'esha','hr',70000,'2024-04-01'),
(6,'farhan','hr',70000,'2024-05-05'),
(7,'gokul','sales',95000,'2024-02-02'),
(8,'hari','sales',85000,'2024-06-18');

select emp_name,department,salary,row_number() over(order by salary desc) as row_num from employees;

select emp_name,department,salary,rank() over(order by salary desc) as salary_rank from employees;

select emp_name,department,salary,dense_rank() over(order by salary desc) as salary_rank from employees;

select emp_name,department,salary,row_number() over(partition by department order by salary desc) as row_num from employees;

select emp_name,department,salary,rank() over(partition by department order by salary desc) as salary_rank from employees;

with ranked as (select emp_name,department,salary,dense_rank() over(partition by department order by salary desc) as rnk from employees) select emp_name,department,salary from ranked where rnk<=2;

select emp_name,department,salary,first_value(emp_name) over(partition by department order by salary desc) as highest_paid_employee from employees;

select emp_name,department,salary,last_value(emp_name) over(partition by department order by salary desc rows between unbounded preceding and unbounded following) as lowest_paid_employee from employees;

select emp_name,department,salary,first_value(salary) over(partition by department order by salary desc rows between unbounded preceding and unbounded following) as highest_salary,last_value(salary) over(partition by department order by salary desc rows between unbounded preceding and unbounded following) as lowest_salary from employees;

with ranked as (select emp_name,department,salary,dense_rank() over(order by salary desc) as rnk from employees) select emp_name,department,salary from ranked where rnk=2;