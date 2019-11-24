# HADOOP ECOSYSTEM
<p align="left">
  <img width="335" heigth="320" src="images/Hadoop-Hadoop_Ecosystem.png?raw=true" alt="Hadoop Ecosystem"/>
</p>

#### MONITORIZATION & DATA INGESTION
**Apache Ambari:** web-based tool for provisioning, managing, and monitoring Apache Hadoop clusters  
**Chukwa:** a data collection system for managing large distributed systems  
**Flume:** a distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data  
**ZooKeeper:** a high-performance coordination service for distributed applications

#### DATA PROCESSING
<p align="left">
  <img width="330" height="260" src="images/Hadoop-Data_Processing.png?raw=true" alt="Hadoop Ecosystem - Data Processing"/>
</p>

- **[Avro](http://avro.apache.org/)** is a data serialization system; with Avro we can store and read data easily from different programming languages. It is optimized to minimize the disk space required to store data  
- **[Drill](https://drill.apache.org/)** _Schema-free SQL Query Engine for Hadoop, NoSQL and Cloud Storage_, leverages advanced query compilation and re-compilation techniques to maximize performance without requiring up-front schema knowledge.In a single query you can join data from several storage systems. For example, you can join a collection of user profiles in MongoDB with a directory of event logs in Hadoop  
- **[Impala](https://impala.apache.org/)** open source, native analytic database for Apache Hadoop  
- **[Hive](https://hive.apache.org/)** data warehouse software facilitates reading, writing, and managing large datasets residing in distributed storage using SQL - provides aggregation methods, ad hoc queries and analysis of large datasets stored in Hadoop  
- **[HCatalog](https://cwiki.apache.org/confluence/display/Hive/HCatalog)** is a table and storage management layer for Hadoop that enables users with different data processing tools — Pig, MapReduce — to more easily read and write data on the grid  
- **[Lucerne](http://lucene.apache.org/core/)** a high-performance, full-featured text search engine library written entirely in Java. It is a technology suitable for nearly any application that requires full-text search, especially cross-platform  
- **[Mahout](http://mahout.apache.org/)** is a machine learning and data mining project used to assist in the search for patterns in large datasets. It has recommendation, clustering and classification algorithms  
- **[Oozie](http://oozie.apache.org/)** is a workflow scheduler system to manage Apache Hadoop jobs; Oozie Workflow jobs are Directed Acyclical Graphs (DAGs) of actions; Oozie Coordinator jobs are recurrent Oozie Workflow jobs triggered by time (frequency) and data availability  
- **[Pig](http://pig.apache.org/)** High level procedural language used for data analysis and parallel process execution  
- **[Spark](https://spark.apache.org/)** data computing engine. Spark provides a simple and expressive programming model that supports multiple applications including ETL (extract, transform, load), machine learning, chain processing and graphic computing  
- **[Sqoop](http://sqoop.apache.org/)** is a tool designed to efficiently transfer information between Hadoop and storage systems with structured data, such as relational databases. Some of its features are: import individual tables or entire databases to HDFS; it generates Java classes that allow you to interact with the imported data; it allows you to import from SQL databases to Hive.

