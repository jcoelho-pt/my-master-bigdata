# HADOOP BASICS
[Hadoop platform](http://hadoop.apache.org/) is built on Java technologies and capable of processing huge volume of heterogeneous data in a distributed clustered environment. Its scaling capability makes it a perfect fit for distributed computing.  
Inspired by Google’s MapReduce and Google File System (GFS) papers.

## CONCEPTS
**Node:** simply means a virtual or physical machine that can be used for processing and storing. There are two types of nodes in hadoop ```Name``` node and ```Data node```. It is called as a node as all these computers are interconnected. NameNode is also known as the Master node.  
**Rack:** set of 1 to n nodes, which are usually grouped in metal structures with this name that have dimensions established by the industry and located in the same network.  
**Cluster:** is a collection of racks  
**Distributed Systems:** set of physical or virtual machines or nodes physically separated and connected to each other by a communications network; each team has its hardware and software components that the programmer perceives as a single system. Against the provisions of Moore's law, these types of systems are an alternative to server scaling.  

## MODULES
- **Hadoop Common:** The common utilities that support the other Hadoop modules. It contains the necessary .jar files and scripts to run Hadoop. In addition, the Hadoop Common package provides the source code, documentation and a contribution section that includes projects from the Hadoop community.
- **Hadoop Distributed File System (HDFS):** A distributed file system that provides high-throughput access to application data. HDFS has optimized the reading and writing of large masses of data and large files. Its design reduces the input-output in the network, is scalable and highly available thanks to the replication and fault tolerance techniques it implements.
- **Hadoop YARN:** A framework for job scheduling and cluster resource management.
- **Hadoop MapReduce:** A YARN-based system for parallel processing of large data sets.
- **Hadoop Ozone:** An object store for Hadoop.
- **Hadoop Submarine:** A machine learning engine for Hadoop.


## HADOOP KEY POINTS
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

## HADOOP DAEMONS
In a fully configured cluster, "running Hadoop" means running a series of "daemons" or programs resident on different servers in the network. These demons have specific roles, some exist only on one server and others on multiple servers.  

### NameNode (aka Master)
Is responsible for managing the namespace repository (index) for the filesystem, and managing Jobs. There is only one in the cluster and therefore acts as a **master node**.  
Its main function is to keep in memory the structure of how the files are divided into blocks and what DataNode stores each of those blocks.

### DataNode (aka Segment)
Is responsible for storing blocks of data and running tasks.  
They are responsible for reading and writing customer requests, the so-called slave nodes. When a client requests a reading or writing of data, the file is divided into blocks and the NameNode is responsible for saying where each of these blocks is located or stored. In addition, the DataNodes communicate with other nodes to replicate the data, increase redundancy and favor error control.  

### Secondary NameNode
Its main role is to mix the NameNode image with the log of executed transactions to prevent the log from growing too much. Normally this demon runs on a separate physical machine, since this process requires a lot of CPU and a lot of memory. It keeps a copy of the NameSpace image so it can be used in case the NameNode fails.  

The HDFS High Availability feature addresses the above problems by providing the option of running two (and as of 3.0.0 more than two) redundant NameNodes in the same cluster in an Active/Passive configuration with a hot standby. This allows a fast failover to a new NameNode in the case that a machine crashes, or a graceful administrator-initiated failover for the purpose of planned maintenance.

## Installing Hadoop

## Hadoop Web Interfaces
