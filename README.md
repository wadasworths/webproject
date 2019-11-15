## Django 博客

```sh
Django==2.2.7
django-mdeditor==0.1.16
Markdown==2.6.11
mysqlclient==1.4.5
pytz==2019.3
sqlparse==0.3.0
uWSGI==2.0.18
```

#### 正式环境中的安全设置

##### MySQL 密码从环境变量中读取

```python
from os import environ

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': environ.get("DB_NAME"),
        'USER': environ.get("DB_USER"),
        'PASSWORD': environ.get("DB_PWD"),
        'HOST': environ.get("DB_HOST"),
        'PORT': environ.get("DB_PORT")
    }
}
```

##### 关闭DEBUG模式,限制链接HOST

```python
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','47.102.206.13']
```

#### 使用MySQL Docker

```sh
# 如果是新装的centos系统
yum update

yum install docker

# 开机启动docker服务
sudo service docker start
sudo chkconfig docker on

# 首先创建两个文件夹，一个用来存放mysql数据，另外一个是存放mysql配置文件
mkdir -p /root/docker/mysql/conf.d/
mkdir -p /root/docker/mysql/data/

# conf.d/my.cnf 配置文件内容
[client]
default-character-set=utf8
[mysqld]
character-set-server=utf8
performance_schema = OFF
[mysql]
no-auto-rehash
default-character-set=utf8

# 启动MySQL docker容器，本地没有mysql docker镜像会自动在Docker hub下载
docker run -d --name mysql \
           -v $(pwd)/conf.d:/etc/mysql/conf.d \
           -v $(pwd)/data:/var/lib/mysql \
           -e MYSQL_ROOT_PASSWORD="test_passwd" \
           -e MYSQL_DATABASE="test" \
           -p 3307:3306 \
            mysql:5.7.19 \
           --character-set-server=utf8 --collation-server=utf8_general_ci
```

...
