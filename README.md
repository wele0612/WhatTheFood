# nwHacks2023

To Save Food, Start With You. Join Us With Project - !What The Food

There is 1260 billion CAD worth of food waste annually, and have you ever stockpiled lots of items or bought redundant groceries and left it to rot and stink in the fridge?

! What The Food is a unique software that helps users manage the refrigerator with a quick to access interface that can scan in grocery items conveniently to control food wastes by resolving the previously mentioned two issues. 

The software is designed through a uniquely developed backend API based on paddlehub’s machine learning ocr and has an extremely large database using mysql that sufficiently picks up keywords in your grocery receipts. A machine learning approach using naive bayes to categorize items not censored in the database is also implemented to improve user experience in the long term. 

We truly believe that small changes on a personal level can help the world move towards a better future. Project - ! What The Food is here for you.

______

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