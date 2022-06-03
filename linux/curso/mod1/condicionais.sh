#!/usr/bin/env bash

VAR=""
VAR=""

if [[ "$VAR" = "$VAR2" ]]; then
  echo "Sao iguais."
fi

if [[ "$VAR" = "$VAR2" ]]
then
  echo "Sao iguais."
fi

if test "$VAR" = "$VAR2"
then
  echo "Sao iguais."
fi

if [ "$VAR" = "$VAR2" ]
then
  echo "Sao iguais."
fi

[ "$VAR" = "$VAR2" ] && echo "Sao iguais."
