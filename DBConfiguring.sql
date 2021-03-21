create database test_db;
create database sessions;

drop database if exists test_db;


create table public.chats (
    id bigint,
    adding_time timestamp default CURRENT_TIMESTAMP,
    update_time timestamp default CURRENT_TIMESTAMP,
    getting_last_message_timestamp timestamp default null,
    last_time_checked timestamp default null,
    last_message_id bigint default 1,
    name text,
    username text,
    pair_username text,
    is_group bool default false,
    is_channel bool default false,
    description text,
    pair_id bigint default null,
    pair_id_checked bool default null,
    primary key (id)
);

create table public.users (
    id bigint,
    adding_time timestamp default CURRENT_TIMESTAMP,
    update_time timestamp default CURRENT_TIMESTAMP,
    first_name text,
    last_name text,
    username text,
    bio text,
    primary key (id)
);

create table public.messages(
    message_db_id bigserial,
    adding_time timestamp default CURRENT_TIMESTAMP,
    message_timestamp timestamp not null,
    id bigint not null,
    chat_id bigint,
    user_id bigint default null,
    reply_to bigint default null,
    thread_start bigint default null,
    media_group_id bigint default null,
    forward_from_id bigint,
    forward_from_message_id bigint,
    text text default null,
    media jsonb,
    formatting jsonb,
    primary key (id,chat_id),
    foreign key (chat_id) references chats (id)
);


CREATE OR REPLACE FUNCTION add_message(_message_timestamp timestamp,_message_id bigint, _chat_id bigint, _user_id bigint,
    _reply_to bigint,_thread_start bigint,_media_group_id bigint,_forward_from_id BIGINT,_forward_from_message_id bigint,
     _text text, _media jsonb, _formatting jsonb) RETURNS void as
$$
    begin
            insert into public.messages (message_timestamp,
                                         id,
                                         chat_id,
                                         user_id,
                                         reply_to,
                                         thread_start,
                                         media_group_id,
                                         forward_from_id,
                                         forward_from_message_id,
                                         text,
                                         media,
                                         formatting) values (_message_timestamp,
                                                             _message_id,
                                                             _chat_id,
                                                             _user_id,
                                                             _reply_to,
                                                             _thread_start,
                                                             _media_group_id,
                                                             _forward_from_id,
                                                             _forward_from_message_id,
                                                             _text,
                                                             _media,
                                                             _formatting);
    end;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION add_user(_user_id bigint,sender_username text,sender_first_name text, sender_last_name text) RETURNS void as
$$
    begin
            insert into users (id, first_name, last_name, username) values (_user_id,sender_first_name,sender_last_name,sender_username);
    end;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION add_chat(_chat_id bigint,_title text,_username text, pair_chat_id bigint,_is_group bool,_is_channel bool) RETURNS void as
$$
    begin
            insert into chats (id, name , username, pair_id, is_group,is_channel) values (_chat_id,_title,_username,pair_chat_id,_is_group,_is_channel);
    end;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION set_chat_checked(_chat_id bigint) RETURNS void as
$$
    begin
            update chats SET getting_last_message_timestamp = current_timestamp where _chat_id=chats.id;
    end;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_user(user_id bigint) RETURNS bool as
$$
    begin
        return exists(select 1 from  users where id=user_id);
    end;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION check_chat(chat_id bigint) RETURNS bool as
$$
    begin
        return exists(select 1 from  chats where id=chat_id);
    end;
$$ LANGUAGE plpgsql;

create  or replace function  get_unupdated_chats(dt timestamp) returns table (_id bigint,
                                                                            _pair_id bigint,
                                                                            _last_message_id bigint,
                                                                            _getting_last_message_timestamp timestamp,
                                                                            _pair_id_checked bool,
                                                                            _username text,
                                                                            _pair_username text) as
$$
    begin
        select id,
                pair_id,
                last_message_id,
                getting_last_message_timestamp,
                pair_id_checked,
                username,
                pair_username from chats where (getting_last_message_timestamp<dt or
                                               getting_last_message_timestamp is null or
                                               chats.pair_id_checked=false) and (last_time_checked is null or last_time_checked <dt)  ;
    end;
$$LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION message_protect() RETURNS trigger as
$$
    begin
        if not exists(select 1 from messages where id = new.id and chat_id=new.chat_id) then
            update chats SET getting_last_message_timestamp = CURRENT_TIMESTAMP, last_message_id=new.id where chats.id=new.chat_id;
            return new;
        else
            return null;
        end if;
    end;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION users_protect() RETURNS trigger as
$$
    begin
        if not exists(select 1 from users where id = new.id) then
            return new;
        else
            return null;
        end if;
    end;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION chats_protect() RETURNS trigger as
$$
    begin
        if not exists(select 1 from chats where id = new.id) then
            if new.is_channel then
                new.pair_id_checked = false;
            end if;
            update public.chats set pair_id_checked=true, pair_id=new.id, pair_username=new.username where id = new.pair_id;
            new.pair_username = (select username from chats where chats.id=new.pair_id);
            return new;
        else
            return null;
        end if;
    end;
$$ LANGUAGE plpgsql;


CREATE TRIGGER on_insert_to_messages before INSERT on public.messages FOR EACH ROW execute PROCEDURE message_protect();
CREATE TRIGGER on_insert_to_users before INSERT on public.users FOR EACH ROW execute PROCEDURE users_protect();
CREATE TRIGGER on_insert_to_chats before INSERT on public.chats FOR EACH ROW execute PROCEDURE chats_protect();

alter table chats add column IF NOT EXISTS last_time_checked timestamp default null;
insert into chats (id,username,is_channel) values (1264079104, 'ssleg', true);