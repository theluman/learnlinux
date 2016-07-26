#!/bin/bash/env python
#-*- coding:utf-8 -*-
'''
linux 定时任务分两种,使用crond设定，每分钟检测，分钟级别的定时任务，低于分钟级别的定时任务需要自己写脚本实现
1、系统自身定期执行的任务工作：系统周期性执行的任务工作，如轮询系统日志、备份系统数据、清理缓存等
    系统运行日志 ls -l /var/log/messages*
    系统自身定期执行任务设置
    [dean@localhost ~]$ ls -l /etc/|grep cron
    -rw-r--r--.  1 root root      541 Jul 13  2015 anacrontab
    drwxr-xr-x.  2 root root     4096 Jun 16 13:02 cron.d
    drwxr-xr-x.  2 root root     4096 Jun 13 14:46 cron.daily
    -rw-r--r--.  1 root root        0 Jul 13  2015 cron.deny
    drwxr-xr-x.  2 root root     4096 Oct 30  2015 cron.hourly
    drwxr-xr-x.  2 root root     4096 Aug 12  2015 cron.monthly
    -rw-r--r--.  1 root root      451 Aug 12  2015 crontab
    drwxr-xr-x.  2 root root     4096 Aug 12  2015 cron.weekly
2、用户执行的定时任务，如数据库备份，站点数据备份等等
    列如时间同步

3、定时任务软件at,crontab,anacron
	    at 依赖于atd服务进程，定时任务只执行一次，不常用，可以被crontab取代
	    crontab 依赖于crond服务，周期性执行任务，常用
        anacron 经常需要开关的机器，定时任务在关机时没有执行的利用anacron执行
    crond服务，crontab是生产中经常用的重点

4、crond使用说明
    Usage:
 crontab [options] file
 crontab [options]
 crontab -n [hostname]

Options:
 -u <user>  define user
 -e         edit user's crontab
 -l         list user's crontab
 -r         delete user's crontab
 -i         prompt before deleting
 -n <host>  set host in cluster to run users' crontabs
 -c         get host in cluster to run users' crontabs
 -s         selinux context
 -x <mask>  enable debugging

单位是分钟、小时、日、月、周及以上的任意组合

/etc/cron.deny  该文件中所有用户不允许使用crontab命令
/etc/cron.allow 该文件中所列用户允许使用crontab命令，优先于/etc/cron.deny
/var/spool/cron/ 所有用户的crontab 配置文件默认都存放在此目录，文件名以用户名命名

格式，用户的定时任务一般分为6段（每段空格分段，系统的定时任务分为7段），前五段为时间设定段，第六段为命令或脚本
    01 * * * * cmd   
    02 * * * * cmd
    03 * * * * cmd
    04 * * * * cmd
分时日月周
    分钟（00-59） 小时（00-23） 日（01-31） 月（01-12） 周（0-7,0和7都是周日）
特殊字符
    *  任意时间都，就是‘每’时间的意思，例如      00 23 * * * cmd,每天的23点
    -  表示分隔符，表示一个时间范围段，如17-19,  00 17-19 * * * cmd，每天的17.18.19点
    ,  逗号，表示分割时段，30 17,18,19 * * * cmd 每天的17点半，18点半，19点半，30,3-5，-17-19，* * * cmd
    /n n代表数字，‘每隔n单位时间’   */10 * * * * cmd, 每隔10分钟执行，也可以写成 0-59/10.* * * * cmd

oldboy 画图 http://oldboy.blog.51cto.com/2561410/1180894

重要 * 23-7/1 * * * cmd  23点到7点每隔1小时的每分钟都执行cmd  
    00 23-7/1 * * * cmd  23点到7点每隔一小时的00分执行cmd, 即每隔一小时执行

5、生产环境crontab 专业实例
    书写crontab 6个基本要领
        1.加必要注释
            什么人，什么时间，因为谁（需求方），做了什么事
        2、执行shell脚本，在前面加上/bin/sh 或者加 /usr/bin/bash  这两个是链接关系，同一个命令
        3、在指定用户下执行相关定时任务，注意不同用户的环境变量问题
        4、定时任务结尾加 >/dev/null 2>&1 或者 >日志文件路径 2>&1
        5、生产的任务程序不要随意打印输出信息，如确实需要输出日志，定位到日志文件中，不要随便echo出来
            cron 日志  cat /var/log/cron
        6、如果直接在crontab -e 中加入命令，容易出错，比如%需要转义等，可以把命令加到文件中，然后crontab中执行文件,执行文件是最专业的定时任务

系统的定时任务配置：
    cat /etc/crontab     系统的定时任务设置文件

生产场景如何调试crontab定时任务
1、增加执行频率调试任务
    规范的流程  个人的开发配置环境-->办公室的测试环境-->idc机房的测试环境-->idc机房的正式环境
2、调整系统时间调试任务，生产机器不能调整时间
3、通过日志输出来调试
4、注意一些任务命令带来的问题
    */1 * * * * echo '==' >> /tmp/sss.log >/dev/null 2>&1 这个不能执行，已经追加到日志了，就不能在送给null
5、注意环境变量导致的定时任务故障
6、通过定时任务日志调试定时任务

问题实例
创建文件提示‘no space left on device'
    磁盘block满了或inode满了
