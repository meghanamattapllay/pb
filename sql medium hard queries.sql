create database hi;
use hi;

create table departments(dept_id int,dept_name varchar(50),location varchar(50));

create table employees(emp_id int,emp_name varchar(50),dept_id int,salary int,manager_id int);

create table projects(project_id int,project_name varchar(50),dept_id int,budget int);

insert into departments values(10,'engineering','chennai'),(20,'sales','hyderabad'),(30,'hr','bengaluru'),(40,'research','pune'),(50,'support','chennai');

insert into employees values(101,'arun',10,50000,103),(102,'bala',20,45000,106),(103,'charan',10,80000,null),(104,'divya',30,40000,108),(105,'ezhil',10,65000,103),(106,'farah',20,75000,null),(107,'gokul',40,55000,109),(108,'harini',30,70000,null),(109,'irfan',40,90000,null),(110,'janani',10,60000,103);

insert into projects values(1,'cloud migration',10,500000),(2,'mobile app',10,300000),(3,'crm upgrade',20,250000),(4,'recruitment ai',30,200000);

select emp_id,emp_name,dept_id,salary from employees e where salary>(select avg(salary) from employees where dept_id=e.dept_id);

select emp_id,emp_name,dept_id,salary from employees e where salary=(select max(salary) from employees where dept_id=e.dept_id);

select max(salary) from employees where salary<(select max(salary) from employees);

select emp_name,salary from employees where salary=(select max(salary) from employees where salary<(select max(salary) from employees));

select emp_id,emp_name,salary from employees e where salary>(select salary from employees where emp_id=e.manager_id);

select emp_id,emp_name,salary from employees e where exists(select 1 from employees where manager_id=e.emp_id and salary>e.salary);

select dept_id from employees group by dept_id having avg(salary)>(select avg(salary) from employees);

select * from employees where dept_id in(select dept_id from employees group by dept_id having avg(salary)>(select avg(salary) from employees));

select emp_id,emp_name,salary from employees where salary>all(select salary from employees where dept_id=(select dept_id from departments where dept_name='hr'));

select emp_id,emp_name,salary from employees where salary>any(select salary from employees where dept_id=(select dept_id from departments where dept_name='research'));

select dept_id,dept_name from departments d where not exists(select 1 from projects where dept_id=d.dept_id);

select * from employees where dept_id in(select dept_id from projects group by dept_id having count(*)>1);

select * from employees where dept_id in(select dept_id from projects where budget=(select max(budget) from projects));

select emp_id,emp_name,salary from employees where abs(salary-(select avg(salary) from employees))=(select min(abs(salary-(select avg(salary) from employees))) from employees);

select dept_id from employees e group by dept_id having max(salary)>all(select salary from employees where dept_id=e.dept_id and emp_id in(select manager_id from employees where manager_id is not null));
