#!/usr/bin/env bash

NOME="Rodrigo

Azevedo"

echo "$NOME"

NUMERO_1=24
NUMERO_2=45

TOTAL=$(($NUMERO_1+$NUMERO_2))

echo "$TOTAL"

SAIDA_CAT="$(cat /etc/passwd | grep razevedo)"

echo "$SAIDA_CAT"

echo "-----------------------------------------"

echo "Parametro 1: $1"
echo "Parametro 2: $2"

echo "Todos os parametros: $*"

echo "Quantos parametros: $#"

echo "Saida do ultimo comando: $?"

echo "PID: $$"

echo $0
