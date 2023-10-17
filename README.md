# What the Food

基于Paddlepaddle机器学习OCR和朴素贝叶斯分类算法的生鲜管理工具。

! What The Food is a unique software that helps users manage the refrigerator with a quick to access interface that can scan in grocery items conveniently to control food wastes by resolving the previously mentioned two issues. 

The software is designed through a uniquely developed backend API based on paddlehub’s machine learning ocr and has an extremely large database using mysql that sufficiently picks up keywords in your grocery receipts. A machine learning approach using Naive Bayes in Python Pandas to categorize items not censored in the database is also implemented to improve user experience in the long term. 

A brief visual overview of the project can be found here: https://www.canva.com/design/DAFYY0q5kos/SjeG_NZowEnY_FXoPiH1Pg/edit?utm_content=DAFYY0q5kos&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton .

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
