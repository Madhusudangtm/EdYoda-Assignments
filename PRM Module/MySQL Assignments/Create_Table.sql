create table if not exists countries(
  country_id varchar(20), 
  country_name varchar(50),
  region_id decimal(10,0)
  );

alter table countries
add constraint
  # check(country_name = 'Italy' or country_name = 'India' or country_name = 'China');
  check(country_name IN ('Italy' 'India' 'China'));