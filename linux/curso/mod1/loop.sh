#!/usr/bin/env bash

echo "==== For 1"
for (( i = 0; i < 10; i++ )); do
  echo $i
done

echo "==== For 2 (seq)"
for i in $(seq 10); do
  echo $i
done

echo "==== For 3 (array)"
Frutas=(
'Laranja'
'Pera'
'Abacaxi'
'Melancia'
)
for i in "${Frutas[@]}"; do # @ significa todos os items do array
  echo "$i"
done

echo "==== While"
contador=0
while [[ $contador -lt ${#Frutas[@]} ]]; do
  echo ${Frutas[$contador]}
  contador=$(($contador+1))
done
