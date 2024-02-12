#!/bin/bash
for ((i=26; i<=28; i++)); do
    if [ $i -ne 19 ]; then
        touch "${i}-answer.txt"
    fi
done
