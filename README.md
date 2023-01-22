# hwHacks2023

Mysql commands to initialize the database:

```
create database grocery;

use grocery;

CREATE TABLE IF NOT EXISTS `users`(
   `username` VARCHAR(100) NOT NULL,
   `password` VARCHAR(100) NOT NULL,
   `grocery` TEXT,
   `sessdata` TEXT,
   PRIMARY KEY ( `username` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```