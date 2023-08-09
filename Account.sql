create table Personal(
	username varchar(30) not primary key,
	password varchar(30) not null 
);

create table Account(
	username varchar(30) not null primary key,
  	website varchar(30) not null,
	websiteUsername varchar(20) not null,
  	password varchar(30) not null,
  	email varchar(30) not null,
	foregin key (username) references Personal(usename)
	
);


insert into Account(website,username,password,email) values('github.com','YabseraBogale','1234567','gamil@.com')
