#!/bin/bash

red=$(echo -ne '\e[01;31m')
green=$(echo -ne '\e[01;32m')
cyan=$(echo -ne '\e[01;34m')
nc=$(echo -ne '\e[00;0m')

passed=0
failed=0

function run_test {
    i=$1
    #in_file=$(echo $i | sed 's/txt$/in/g')
    solution=$(echo $i | sed 's/txt$/sol/g')
   
    in_file=$i

    real=$solution

    #echo $in_file
    #echo -n "${nc}"
        
    #echo -n "$green|$nc ${cyan}$(printf '%-50s' $i) ["
   
    python ./main.py $in_file > /tmp/sudoku.test
     
    
    #echo -n "$green|$nc ${cyan}$(printf '%-50s' $i) ["
    diff <(echo "/tmp/sudoku.test") <(echo $solution) > /dev/null
    
    if [ $? -eq 0 ] ; then
        echo "${cyan}PASS${cyan}"  
        passed=$(($passed + 1))
    else
        printf "${red}FAIL${cyan}"  
        failed=$(($failed + 1))
        echo " + Expected:"
        cat $solution
        echo " + Got:"
        cat "/tmp/sudoku.test"
    fi
    
    #rm /tmp/$$test*
}

for test_set in tests ; do
    printf "$green+-------------------[ %-13s ]-----------------------+$nc\n" $test_set
    tests=$(find $test_set -name '*.txt' | sort)
    
    for i in $tests ; do
        run_test $i
    done
    echo -ne "${nc}"
done

printf "$green+-----------------------------------------------------------+$nc\n" $test_set
printf "$green|                     Passed: $passed/$(($passed + $failed))                       |$nc\n"
printf "$green+-----------------------------------------------------------+$nc\n" $test_set

