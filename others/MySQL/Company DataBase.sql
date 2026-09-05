#创建公司数据库表格

CREATE DATABASE `Company`;
USE `Company`;

CREATE TABLE `employee`(
	`emp_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `birth_date` DATE,
    `sex` VARCHAR(1),
    `salary` INT,
    `branch_id` INT,
    `sup_id` INT
);

CREATE TABLE `branch`(
    `branch_id` INT PRIMARY KEY,
    `branch_name` VARCHAR(20),
    `manager_id` INT,
    #设置外键
    #ON DELETE SET NULL 即外键被删除后设置为NULL（主键不能设为NULL）
	FOREIGN KEY (`manager_id`) REFERENCES `employee`(`emp_id`) ON DELETE SET NULL 
);

#已有表格添加外键属性
ALTER TABLE `employee`
ADD FOREIGN KEY (`branch_id`) 
REFERENCES `branch`(`branch_id`) 
ON DELETE SET NULL;

ALTER TABLE `employee`
ADD FOREIGN KEY (`sup_id`) 
REFERENCES `employee`(`emp_id`) 
ON DELETE SET NULL;

CREATE TABLE `client`(
    `client_id` INT PRIMARY KEY,
    `client_name` VARCHAR(20),
    `phone` VARCHAR(20)
);

CREATE TABLE `works_with`(
    `emp_id` INT,
    `client_id` INT,
    `total_sales` INT,
    PRIMARY KEY(`emp_id`,`client_id`),
    #ON DELETE SET CASCADE 即外键被删除后整条数据一起删掉
    FOREIGN KEY(`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE,
    FOREIGN KEY(`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE
);

#添加数据，未初始化外键先写NULL
INSERT INTO `branch` VALUES(1,'研发',NULL);
INSERT INTO `branch` VALUES(2,'行政',NULL);
INSERT INTO `branch` VALUES(3,'资讯',NULL);

INSERT INTO `employee` VALUES(206,'小黄','1998-10-08','F',50000,1,NULL);
INSERT INTO `employee` VALUES(207,'小绿','1985-09-16','M',29000,2,206);
INSERT INTO `employee` VALUES(208,'小黑','2000-12-19','M',35000,3,206);
INSERT INTO `employee` VALUES(209,'小白','1997-01-22','F',39000,3,207);
INSERT INTO `employee` VALUES(210,'小蓝','1925-11-10','F',84000,1,207);

#更新外键(也可以select在框内更改）
UPDATE `branch` SET `manager_id` = 206 WHERE `branch_id`=1;
UPDATE `branch` SET `manager_id` = 207 WHERE `branch_id`=2;
UPDATE `branch` SET `manager_id` = 208 WHERE `branch_id`=3;

INSERT INTO `client` VALUES(400,'阿狗','254354335');
INSERT INTO `client` VALUES(401,'阿猫','254354336');
INSERT INTO `client` VALUES(402,'旺来','254354387');
INSERT INTO `client` VALUES(403,'露西','254354399');
INSERT INTO `client` VALUES(404,'艾利克斯','254352235');

INSERT INTO `works_with` VALUES(206,400,'70000');
INSERT INTO `works_with` VALUES(207,401,'24000');
INSERT INTO `works_with` VALUES(208,402,'9800');
INSERT INTO `works_with` VALUES(208,403,'24000');
INSERT INTO `works_with` VALUES(210,404,'87940');

#取得公司资料

#1.取得所有员工资料
SELECT * FROM `employee`;

#2.取得所有客户资料
SELECT * FROM `client`;

#3.按薪水递减取得员工资料
SELECT * FROM `employee` ORDER BY `salary` DESC;

#4.取得薪水前三员工的数据
SELECT * FROM `employee` ORDER BY `salary` DESC LIMIT 3;

#5.取得所有员工的名字(DISTINCT使返回数据不重复)
SELECT DISTINCT `name` FROM `employee`;


#聚合函数

#1.取得员工总数(COUNT统计数据笔数，除去NULL)
SELECT COUNT(*) FROM `employee`;

SELECT COUNT(`sup_id`) FROM `employee`;

#2.取得1970-01-01之后出生的女员工人数
SELECT COUNT(*) FROM `employee` 
WHERE `birth_date` > '1970-01-01' AND `sex` = 'F';

#3.取得员工的平均薪水(AVG取平均值)
SELECT AVG(`salary`) FROM `employee`;

#4.取得所有员工薪水的总和(SUM计算总和)
SELECT SUM(`salary`) FROM `employee`;

#5.最高薪水
SELECT MAX(`salary`) FROM `employee`;

#6.最低薪水
SELECT MIN(`salary`) FROM `employee`;


#通配符 %代表多个字符 _代表一个字符

#1.取得电话尾号为335的客户
SELECT * FROM `client` WHERE `phone` LIKE '%335';

#2.取得姓艾的客户
SELECT * FROM `client` WHERE `client_name` LIKE '艾%';

#3.取得生日在12月的员工
SELECT * FROM `employee` WHERE `birth_date` LIKE '%-12-%';#OR'____-12-__'


#并集Union 合并搜寻结果

#1.员工名字 union 客户名字
SELECT `name` FROM `employee` UNION SELECT `client_name` FROM `client`;

#2.员工id+名字 union 客户id+名字(AS改名)
SELECT `emp_id` AS `id`,`name` FROM `employee` UNION SELECT `client_id`,`client_name` FROM `client`;

#3.员工薪水 union 销售金额
SELECT `salary` AS `amount` FROM `employee` UNION SELECT `total_sales` FROM `works_with`;


#连接join 

#取得所部门经理的名字
#table名.属性名区分属性
#LEFT/RIGHT使对应侧表格全部显示，另一侧未对应返回NULL
SELECT `emp_id`,`name`,`branch_name` 
FROM `employee` RIGHT JOIN `branch` ON `employee`.`emp_id` = `branch`.`manager_id`;


#子查询 subquery 利用一个查询结果查询另一个数据,嵌套查询

#1.找出研发部门的经理名字
SELECT `name` FROM `employee`
WHERE `emp_id` = (
	SELECT `manager_id` FROM `branch` WHERE `branch_name` = '研发'
);

#2.找出对单位客户销售金额超50000的员工名字(不止一笔结果用IN不用=)
SELECT `name` FROM `employee` 
WHERE `emp_id` IN (
	SELECT `emp_id` FROM `works_with` WHERE `total_sales` >= 50000
);

























