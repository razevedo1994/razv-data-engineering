# Data Lake

### O que é um Data Lake?
Um Data Lake é um repositorio centralizado que permite que voce armazene todos os seus dados
estruturados e nao-estruturados em qualquer escala. Voce pode armazenar os seus dados sem ter que
primeiro estrutura-los, e entao executar diferentes tipos de analises: de dashboards a visualizacoes,
processamento de Big Data, analise em tempo real e aprendizado de maquina.


### Camadas de um Data Lake

 - **Camada 1**- (raw, bronze):
   - Esta camada consiste em um ou mais buckets que armazenam os dados vinds dos servicos de ingestao. Os dados armazenados nessa camada devem ser mantidos e preservados em sua forma original e nenhuma transformacao deve ocorrer nos dados. Quem usa: Data Engineers, Spark jobs
 - **Camada 2**- (processed, staged, silver):
   - Esta camada armazena os datasets resultantes da transformacao dos dados brutos da camada 1 em arquivos colunares (como Parquet, ORC, ou Avro) usando processamento ETL (por exemplo, Spark, ou AWS Glue). Com os dados organizados em particoes e em um formato colunar, os jobs de processamento conseguem ingerir estes dados com maior performance e menores custos. QUem usa: Data Scientist, Spark jobs, DBT, AWS Athena
-  **Camada 3**- (curated, enriched, gold):
   -  Os dados armazenados nesta camada sao um subgrupo da camada 2 que foram organizados para usos especificos. Os dados desta camada geralmente sao acessados mais frequentemente por diversos stakeholders. Dependendo do caso de uso os dados podem ser servidos com diferente tecnologias: Amazon EMR, Redshift, Presto, Athena, etc. Quem usa: Data Analysts, Data Scientists, Data Warehouse, Ferramentas de BI.



### Formatos de arquivos

[Parquet](https://databricks.com/glossary/what-is-parquet)
