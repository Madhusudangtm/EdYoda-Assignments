create table if not exists countries(
COUNTRY_ID varchar(2) null,
COUNTRY_NAME varchar(40) null,
REGION_ID decimal(10,0) null
);

create table if not exists country_new
as select * from countries
where 1<>1;

show columns from country_new