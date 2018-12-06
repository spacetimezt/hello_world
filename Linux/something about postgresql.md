# postgres安装



```
yum install https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-centos11-11-2.noarch.rpm

yum install postgresql

yum install postgresql-server
service postgresql initdb

vi /var/lib/pgsql/data/postgresql.conf
59行 
listen_addresses = '*'

vi /var/lib/pgsql/data/pg_hba.conf
最后ipv4
 81 # IPv4 local connections:
 82 host    all             all             127.0.0.1/32            ident
 83 host    all             all             0.0.0.0/0            password
systemctl enable postgresql
systemctl start postgresql


psql su - postgres


su - postgres
psql
alter user postgres password '123456abc';
上面这几句是改密码

远程登陆
psql -h 192.168.0.113 -U postgres  -W
输入密码123456abc即可


```

