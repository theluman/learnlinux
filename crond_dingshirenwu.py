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
