#!/bin/bash
#字颜色范围30-37
echo "echo 方式"
echo -e "\033[30m黑色字dean\033[0m"
echo -e "\033[31m红色字dean\033[0m"
echo -e "\033[32m绿色字dean\033[0m"
echo -e "\033[33m黄色字dean\033[0m"
echo -e "\033[34m蓝色字dean\033[0m"
echo -e "\033[35m紫色字dean\033[0m"
echo -e "\033[36m天蓝字dean\033[0m"
echo -e "\033[37m白色字dean\033[0m"

echo "定义变量方式"
red_colour='\033[31m'
end_colour='\033[0m'
yellow_colour='\033[33m'
green_colour='\033[32m'

echo -e "${red_colour}red-dean${end_colour}"
echo -e "${yellow_colour}yellow-dean${end_colour}"
echo -e "${green_colour}green-dean${end_colour}"
