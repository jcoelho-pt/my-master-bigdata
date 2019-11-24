# HADOOP INSTALLATION



## 1. REQUIREMENTS
**Java** is the primary requirement for running Hadoop on any system, so make sure you have Java installed on your system.

## 2. CREATE A USER FOR HADOOP*
It is recommended to create a normal (nor root) account for Hadoop working.
```bash
adduser hadoop
```
After creating the account, it also required to set up key-based ssh to its own account:
```bash
su - hadoop
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```
Now, SSH to localhost with Hadoop user. This should not ask for the password but the first time it will prompt for adding RSA to the list of known hosts.
```bash
ssh localhost
exit
```

## 3. DOWNLOAD HADOOP SOURCE ARCHIVE
Hadoop Releases: http://hadoop.apache.org/releases.html
In this step, download hadoop 3.1 source archive file using below command. You can also select [alternate download mirror](https://www.apache.org/dyn/closer.cgi/hadoop/common/) for increasing download speed.
```bash
wget http://www-eu.apache.org/dist/hadoop/common/hadoop-3.1.2/hadoop-3.1.2.tar.gz
tar xzf hadoop-3.1.2.tar.gz
mv hadoop-3.1.2 hadoop
```
