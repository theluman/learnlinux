menu(){
cat <<EOF
    1.[install lamp]
    2.[install lnmp]
    3.[exit]
    pls input the num you want:
EOF
}
menu
read num
[ $num -gt 0 ] >/dev/null 2>&1 && echo "you have selected $num" || echo "a num must be needed"

