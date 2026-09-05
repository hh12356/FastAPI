#创建/删除数据库
CREATE DATABASE `sql_tutorial`;
DROP DATABASE `sql_tutorial`;

#展示数据库
SHOW DATABASES;

#切换数据库
USE `sql_tutorial`;

#创建表格
CREATE TABLE `student`(
	#属性名与类型
    #约束:NOT NULL非空，UNIQUE不可重复，DEFAULT预设值,AUTO_INCREMENT自动递增
	`student_id` INT AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL,
    `major` VARCHAR(20) DEFAULT '历史',
    `score` INT,
    #设置主键(自带UNIQUE效果）
    PRIMARY KEY(`student_id`)
);

#展示表格
DESCRIBE `student`;

#删除表格
DROP TABLE `student`;

#表格添加/删除属性
ALTER TABLE `student` ADD gpa DECIMAL(3,2);
ALTER TABLE `student` DROP COLUMN gpa;

#存入数据（属性按创建顺序写，可以写NULL表示没有）
INSERT INTO `student` VALUES(1,'小白','物理');
#自行规定输入属性顺序
INSERT INTO `student` (`name`,`major`,`student_id`) VALUES('小黑','物理',3);

#搜寻资料(*表示全部）
SELECT * FROM `student`;


#开启/关闭安全更新模式(防止大规模修改)
SET SQL_SAFE_UPDATES = 1;
SET SQL_SAFE_UPDATES = 0;

#修改数据
UPDATE `student`
SET `major` = '生化' , `name`='小灰' #修改多条
WHERE `student_id` = 3 OR `student_id` = 1; #多重条件

#删除数据
DELETE FROM `student`
WHERE `score` < 60 AND `major` = '物理';
#不等于：<>

#取得数据
SELECT `name`,`major` FROM `student`; 
#排序(ASC为递增，DESC为递减)(根据属性顺序做排序）(LIMIT限制数据数)
SELECT * FROM `student` ORDER BY `socre`,`student_id` DESC LIMIT 3;
#筛选(IN等同于OR）
SELECT * FROM `student`WHERE `major` IN ('历史','英文','物理');





























