DROP FUNCTION IF EXISTS query_pagination(int, int);
create or replace function query_pagination(p_limit int, p_offset int)
returns table(id int, name varchar, surname varchar, email varchar, group_name varchar, phone text)
language plpgsql 
as $$
begin
  return query
    select p.id, p.first_name, p.last_name, p.email, groups.name,
    STRING_AGG(ph.phone || COALESCE(' (' || ph.type || ')', ''), ', ')
    from phonebook p
    LEFT JOIN groups ON groups.id = p.group_id
    LEFT JOIN phones ph ON ph.contact_id = p.id
    group by p.id, groups.name
    order by p.id
    limit p_limit
    offset p_offset;
end; $$;

create or replace procedure add_phone(name varchar, c_phone varchar, p_type varchar)
language plpgsql
as $$
declare
  v_id int;
begin
  select id into v_id from phonebook where first_name = name;
  if v_id is null then
    raise exception 'Contact % not found', name;
  end if;

    insert into phones(contact_id, phone, type) values(v_id, c_phone, p_type);
end; $$;

create or replace procedure move_to_group(contact_name varchar, group_name varchar)
language plpgsql
as $$
declare
  g_id int;
begin
  select id into g_id from groups
  where name = group_name;
  if g_id is null then
    insert into groups(name) values(group_name)
    returning id into g_id;
  end if;

  update phonebook set group_id = g_id
  where first_name = contact_name;
  if not found then
    raise exception 'Contact % was not found', contact_name;
  end if;
end; $$;


create or replace function search_contacts(pattern TEXT)
returns table(c_id int, name varchar, surname varchar, email varchar, group_name varchar, phone text)
language plpgsql
as $$
begin
  return query 
    select p.id, p.first_name,p.last_name, p.email, groups.name,
      STRING_AGG(ph.phone || COALESCE(' (' || ph.type || ')', ''), ', ') 
    from phonebook p
    left join groups on groups.id = p.group_id
    left join phones ph on ph.contact_id = p.id
    where p.first_name ilike '%' || pattern || '%'
      or p.last_name ilike '%' || pattern || '%'
      or p.email ilike '%' || pattern || '%'
      or p.id in (select contact_id from phones where phones.phone ilike '%' || pattern || '%')
    group by p.id, groups.name
    order by p.id;
end; $$;
