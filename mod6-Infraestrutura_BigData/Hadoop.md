# HADOOP

## BASICS OF HADOOP AND ITS ECOSYSTEM
[Hadoop platform](http://hadoop.apache.org/) is built on Java technologies and capable of processing huge volume of heterogeneous data in a distributed clustered environment. Its scaling capability makes it a perfect fit for distributed computing.  
Inspired by Google’s MapReduce and Google File System (GFS) papers.

### CONCEPTS
**Node:** simply means a virtual or physical machine that can be used for processing and storing. There are two types of nodes in hadoop ```Name``` node and ```Data node```. It is called as a node as all these computers are interconnected. NameNode is also known as the Master node.  
**Rack:** set of 1 to n nodes, which are usually grouped in metal structures with this name that have dimensions established by the industry and located in the same network.  
**Cluster:** is a collection of racks  
**Distributed Systems:** set of physical or virtual machines or nodes physically separated and connected to each other by a communications network; each team has its hardware and software components that the programmer perceives as a single system. Against the provisions of Moore's law, these types of systems are an alternative to server scaling.  
**NameNode (aka Master)** is responsible for managing the namespace repository (index) for the filesystem, and managing Jobs  
**DataNode (aka Segment)** is responsible for storing blocks of data and running tasks  
**MapReduce** push compute to where data resides

### MODULES
- **Hadoop Common:** The common utilities that support the other Hadoop modules.
- **Hadoop Distributed File System (HDFS):** A distributed file system that provides high-throughput access to application data.
- **Hadoop YARN:** A framework for job scheduling and cluster resource management.
- **Hadoop MapReduce:** A YARN-based system for parallel processing of large data sets.
- **Hadoop Ozone:** An object store for Hadoop.
- **Hadoop Submarine:** A machine learning engine for Hadoop.

### ECOSYSTEM
<p align="left">
  <img width="300" heigth="310" src="images/Hadoop-Hadoop_Ecosystem.png?raw=true" alt="Hadoop Ecosystem"/>
</p>

#### MONITORIZATION & DATA INGESTION
**Apache Ambari:** web-based tool for provisioning, managing, and monitoring Apache Hadoop clusters  
**Chukwa:** a data collection system for managing large distributed systems  
**Flume:** a distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data  
**ZooKeeper:** a high-performance coordination service for distributed applications

#### DATA PROCESSING
<p align="left">
  <img width="300" height="310" src="images/Hadoop-Data_Processing.png?raw=true" alt="Hadoop Ecosystem - Data Processing"/>
</p>

### HADOOP KEY POINTS
- **Accessible:** runs on large groups of machines in clusters or in clouds such as Amazon's Elastic Compute Cloud (EC2).
- **Robust**: is designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures
- **Scalable**: allows horizontal scaling to manage larger volumes of data through replication, adding more nodes to the cluster 
- **Simple**: allows users to write efficient code in parallel using complex concepts such as MapReduce or the distributed HDFS file system designed according to the Google GSF  


## HDFS

### HDFS CONCEPTS
- Sits on top of native (ext3, xfs, etc.) file system
- Performs best with a ‘modest’ number of large files  
    – Millions, rather than billions, of files  
    – Each file typically 100Mb or more
- Files in HDFS are ‘write once’  
    – No random writes to files are allowed  
    – Append support is available in Hadoop 0.21
- HDFS is optimized for large, streaming reads of files  
    – Rather than random reads 

**Hadoop Distributed File System**  
– Data is organized into files & directories  
– Files are divided into blocks, typically 64-128MB each,and distributed across cluster nodes  
– Block placement is known at runtime by map-reduce so computation can be co-located with data  
– Blocks are replicated (default is 3 copies) to handle failure  
– Checksums are used to ensure data integrity  
**Replication is the one and only strategy for error handling, recovery and fault tolerance**  
– Make multiple copies and be happy! 

### HDFS COMPONENTS
• NameNode
• DataNode
• Standby NameNode
• Job Tracker
• Task Tracker

## Hadoop Daemons

## Installing Hadoop

## Hadoop Web Interfaces
