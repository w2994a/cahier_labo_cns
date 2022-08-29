#!/bin/bash
tab=( $(find $1*.tex) )
for element in ${tab[@]}
do
    wc -l $element
done
((sum=2+4))
if [ $sum -lt 7 -a $sum -gt 4 ];then
    echo $sum
fi