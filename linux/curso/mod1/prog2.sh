#!/usr/bin/env bash


for (( i = 0; i < 10; i++ )); do
  if [ $(( $i % 2 )) = 0 ]
  then
    echo "$i eh divisivel por 2."
  fi
done
