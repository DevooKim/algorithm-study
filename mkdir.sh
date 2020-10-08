#!/bin/bash
n=2;
MAX=10;
NAME="week"

while [ "$n" -le "$MAX" ];
do
    dir="$NAME$n"
    mkdir $dir
    mkdir ./$dir/"book"
    mkdir ./$dir/"problem"
    echo "test" >> ./$dir/"book"/remove.txt
    echo "test" >> ./$dir/"problem"/remove.txt
    n=`expr "$n" + 1`;
done