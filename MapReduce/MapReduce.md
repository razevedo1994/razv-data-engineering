# MapReduce

MapReduce é uma tecnica de programacao projetada para analisar grandes conjuntos de dados atraves de cluster, nela 
o conjunto de dados é dividido e distribuido em um cluster. Na etapa do map, cada dado é analisado e convertido em 
um par (chave, valor). Em seguida, estes pares de chaves de valor são embaralhados através do cluster para que todas 
as chaves estejam na mesma máquina. Na etapa de reduce, os valores com as mesmas chaves são combinados entre si.

O Hadoop MapReduce é uma implementacao especifica dessa tecnica. A grande diferenca entre Hadoop e o Spark é 
que o Spark tenta realizar o maior numero de processamento em memoria, o que evita que o dado seja movido atraves 
do cluster. O Hadoop realiza os calculos em disco, o que o torna mais lento em relacao ao Spark.

# Codigo

A biblioteca [mrjob](https://mrjob.readthedocs.io/en/latest/) permite que executemos MapReduce jobs com Python 
localmente, sem a necessidade de um cluster ou de instalar o Hadoop.

No arquivo `wordcount.py` é possivel ver uma implementacao da tecnica MapReduce.