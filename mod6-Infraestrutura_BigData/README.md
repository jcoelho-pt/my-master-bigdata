# Mod.6 - Infraestructura Big Data
## Objetivos
Tras el estudio de este módulo, los alumnos habrán alcanzado los siguientes objetivos:

1. Distinguir entre procesamiento batch y streaming.  
2. Comprender los conceptos principales sobre ambos tipos de procesamiento.  
3. Familiarizarse con las tecnologías Big Data que los posibilitan, entre otras:  
    * Hadoop  
    * Spark  
    * Kafka  
4. Adquirir conocimientos sobre arquitecturas de procesamiento paralelo.  
5. Adquirir conocimientos sobre arquitectura cloud (IaaS): AWS, etc.

## Troubleshooting Hadoop
#### ERROR: java.net.ConnectException: Conexión rehusada
1. For all daemons, delete the namenode and datanode directories in:
````/home/bigdata/hadoop_store/hdfs/namenode```` 
create them again with:
````
mkdir -p / home / bigdata / hadoop_store / hdfs / namenode
mkdir -p / home / bigdata / hadoop_store / hdfs / datanode
````
2. Format hdfs: ````hdfs namenode -format````
3. Restart yarn deamons: 
````
./sbin/start-yarn.sh
````
