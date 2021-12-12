# 超市信息管理系统

> 使用语言：python3.9
> 所用技术：SQLite3,tkinter,openpyxl,pandas
> 使用Java开发中的MVC思想，代码虽有冗余，但更容易维护
>
> 默认账号：admin，密码：123456

## 一、创建数据库

1. 使用`SQLite3`创建商品信息管理系统所需数据表的数据库：`commodity_info`数据库
2. 创建商品信息表，对项目中的商品信息进行存储

```sqlite
-- 商品信息表
create table commodity_info.commodity(
    com_code int not null,
    -- 商品编号 int类型、非空
    com_name char not null,
    -- 商品名字 char类型、非空
    com_price int not null,
    -- 商品价格 int类型、非空
    com_stock int not null,
    -- 商品库存 int类型、非空
);
```

因为项目有登录的需求，所以创建一张管理员表

```sqlite
-- 管理员表
create table commodity_info.user(
    username char not null,     -- 账号
    password char not null      -- 密码
);
```

3. 项目不需要添加管理员，管理员账号、密码的添加由管理人员代码添加

## 二、登录界面UI

![登录界面UI](https://cdn.jsdelivr.net/gh/1804784474/images/image-20211212140140980.png)

## 三、主界面UI

![主界面UI](https://cdn.jsdelivr.net/gh/1804784474/images/image-20211212140323675.png)

## 四、功能界面UI

### 1、商品信息

![商品信息](https://cdn.jsdelivr.net/gh/1804784474/images/image-20211212140614140.png)

### 2、查询商品

![查询商品](https://cdn.jsdelivr.net/gh/1804784474/images/image-20211212140631627.png)

### 3、添加商品

![添加商品](https://cdn.jsdelivr.net/gh/1804784474/images/image-20211212140649051.png)

### 4、修改商品

![修改商品](https://cdn.jsdelivr.net/gh/1804784474/images/image-20211212140712851.png)

### 5、删除商品

![删除商品](https://cdn.jsdelivr.net/gh/1804784474/images/image-20211212140741387.png)

### 6、关于

展示项目制作者信息

### 7、退出

关闭程序
