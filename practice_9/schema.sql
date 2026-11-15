create table groups(
  id serial primary key,
  name varchar(50) unique not null
);
insert into groups(name) values('Family'), ('Work'), ('Friends'), ('Other');

alter table phonebook
  add column email varchar(100),
  add column birthday DATE,
  add column group_id int REFERENCES groups(id),
  add column date_added TIMESTAMP DEFAULT NOW();
  
create table phones (
  id serial primary key,
  contact_id int REFERENCES phonebook(id) ON DELETE CASCADE,
  phone VARCHAR(30) NOT NULL,
  type varchar(50) CHECK (type IN ('home', 'work', 'mobile'))
);

insert into phones(contact_id, phone, type) SELECT p.id, p.phone, 'mobile'
from phonebook p
where p.phone IS NOT NULL;

ALTER TABLE phonebook DROP COLUMN phone;