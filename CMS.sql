create database CustomerManagement;

use CustomerManagement ;

create table Users (
user_id varchar (10) primary key,
name varchar(20),
password varchar (20)
);

insert into Users 
values ('1',"Ram","Admin@12");

select * from Users;

create table Customer (
customer_id varchar(10) primary key,
name varchar(20),
phone varchar(20),
gender varchar(10),
address varchar (50),
password varchar (20)
);

insert into Customer 
values ('1',"Shyam",'8567943268',"male","Lucknow","shy@1"),
('2',"Mohan",'5975643648',"male","Indore","moh@2"),
('3',"Priya",'9684327615',"female","Delhi","pri@3"),
('4',"Suman",'6842397561',"female","Noida","sum@4");

select * from Customer;

create table Product (
product_id varchar(10) primary key,
product_name varchar(20),
amount varchar(10)
);

insert into Product 
values ('1',"Book",'250'),
('2',"Fan",'500'),
('3',"Table",'1100'),
('4',"Lamp",'3000'),
('5',"Boxes",'120');

select * from Product ;

create table PurchaseItems (
product_id varchar(10),
customer_id varchar(10),
product_name varchar (20),
purchase_date date,
status varchar(20),

FOREIGN KEY (product_id) REFERENCES Product(product_id),
FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

insert into PurchaseItems 
values ('2','1',"Fan",'2026-05-19',"Buy"),
('2','3',"Fan",'2026-05-18',"Buy"),
('4','4',"Lamp",'2026-05-19',"Buy"),
('3','2',"Table",'2026-05-17',"Buy"),
('1','2',"Book",'2026-05-19',"Buy"),
('5','1',"Boxes",'2026-05-20',"Buy");

select * from PurchaseItems;

create table ReturnItems (
product_id varchar(10),
customer_id varchar(10),
product_name varchar (20),
return_date date,
status varchar(20),

FOREIGN KEY (product_id) REFERENCES Product(product_id),
FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

insert into ReturnItems 
values ('2','1',"Fan",'2026-05-22',"Return"),
('4','4',"Lamp",'2026-05-21',"Return"),
('1','2',"Book",'2026-05-22',"Return");

select * from ReturnItems;

create table Review (
product_id varchar(10),
customer_id varchar(10),
rating int check (rating >=1 AND rating <= 5),
review varchar(200),

FOREIGN KEY (product_id) REFERENCES Product(product_id),
FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);

insert into Review 
values ('2','3',4,"The product is good."),
('4','4',2,"Not working well."),
('5','1',3,"It's okey okey");

select * from Review;
select * from Purchaseitems;
select * from ReturnItems;
select * from Product ;
select * from Customer;
select * from Users;


