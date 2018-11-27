# 守护进程

daemon_comm.sh

```

#! /bin/sh

while [ 1 ]
do
   sleep 3
   pnums=`ps -ef | grep abcd | grep -v "grep " | wc -l`
   echo abcd $pnums
   if [ "$pnums" = "0" ]; then
	cd /usr/local/ && ./abcd > /dev/null &
	echo abcd not found
   fi
done

```


start.sh

```
#!/bin/sh
sleep 30
cd /usr/local/ && sh daemon_comm.sh > /dev/null &
exit
```

