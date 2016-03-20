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
    diff /tmp/sudoku.test  $solution > /dev/null 2>&1
    
    if [ $? -eq 0 ] ; then
        printf "$green ************************$nc\n"
        printf "$green| Test: $in_file Passed$nc\n"
        printf "$green ************************$nc\n\n"
        passed=$(($passed + 1))
    else
        printf "$red ************************$nc\n"
        printf "$red| Test: $in_file Failed$nc\n"
        

        failed=$(($failed + 1))
        echo "${nc} + Expected:"
        cat $solution
        echo " + Got:"
        cat "/tmp/sudoku.test"
        printf "\n$red ************************$nc\n\n"

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

