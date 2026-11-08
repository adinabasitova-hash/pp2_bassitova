create or replace function get_contact_by_pattern(p_pattern varchar)
returns table(id int, name varchar, surname varchar, phone varchar)
language plpgsql
as $$
begin 
  return query
    select p.id, p.first_name, p.last_name, p.phone
    from phonebook p
    where p.first_name ilike '%'||p_pattern||'%' or p.last_name ilike '%' || p_pattern || '%' or p.phone ilike '%'||p_pattern ||'%';
end;$$;


create or replace procedure add_new_contact(
  name varchar,
  c_phone varchar,
  surname varchar default null
)
language plpgsql
as $$
begin
  if exists(select 1 from phonebook where first_name = name and last_name is not distinct from surname) then
    update phonebook set phone = c_phone where first_name = name and last_name is not distinct from surname;
  else
    insert into phonebook(first_name, last_name, phone) values(name, surname, c_phone);
  end if;
end; $$;

create or replace procedure add_many_contacts(
  name varchar[],
  c_phone varchar[],
  surname varchar[] default null,
  inout bad_values varchar[] default '{}'
)
language plpgsql
as $$
begin
  if array_length(name,1) is null or array_length(name,1) != array_length(c_phone,1) then
    raise exception 'The lists of names and contacts are empty or have different lengths';
  end if;

  for i in 1..array_length(name,1) loop
    if c_phone[i] ~ '^\+?[0-9]{11}$'
    then call add_new_contact(name[i],c_phone[i], surname[i]);
    else
      bad_values = array_append(bad_values, 
      concat_ws(' ', name[i], surname[i]) || '-' || c_phone[i]);
   end if;
  end loop;
end; $$;
            

create or replace function query_pagination(p_limit int, p_offset int)
returns table(
  id int,
  name varchar,
  surname varchar,
  c_phone varchar
  
)
language plpgsql
as $$
begin 
  return query
    select p.id, p.first_name,p.last_name, p.phone
    from phonebook p
    order by p.id
    limit p_limit offset p_offset;
end; $$;

create or replace procedure delete_contact(pattern varchar)
language plpgsql 
as $$
declare
  deleted_count int;
begin
  delete from phonebook
  where first_name = pattern or phone = pattern;

  get diagnostics deleted_count = row_count;
  if deleted_count = 0 then
    raise notice 'No such contact';
  else
    raise notice 'All done, % rows were deleted', deleted_count;
  end if;
end; $$;