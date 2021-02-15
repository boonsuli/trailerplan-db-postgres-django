-- TRILERPLAN postgresql schema

drop sequence if EXISTS P_USER_ID_SEQ;
create sequence P_USER_ID_SEQ start with 1 increment by 1;

drop table if exists P_USER cascade;
create table P_USER (
  ID SERIAL PRIMARY key,
  CIVILITE VARCHAR (10) not null,
  FIRST_NAME VARCHAR(20) not null,
  LAST_NAME VARCHAR(20) not null,
  SEXE VARCHAR (10) not null,
  BIRTHDAY date null,
  CITY VARCHAR (20) null,
  COUNTRY VARCHAR (20) not null
);
