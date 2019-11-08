# DataEngineering-PubsubListener
This is a GCP Cloud Function, the main purpose of this function is to listen to messages that are being published to a topic in PUB/SUB.
The messages are kept in the subscriber for 7 days if they are now pulled and Knowlege.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### 1- Prerequisites
* [Anaconda]() - Anaconda allows us to keep virtual environments organize and it is the best setup tool for data analysis. 

### 2- Setup

```sh
$ git clone ~/DataEngineering-FileToSQLServerChuncks.git
$ conda create -n FileToSQLServerChuncks python=3.7
$ conda activate FileToSQLServerChuncks
$ pip install requirements.txt
```

4.- For Windows - In order to create a Task Scheduler a bash is included here as well, change the path for the new directory as well as the name of the new environment and the executable bin path for conda.  
    For Unix - (This needs to be implemented)

## Authors
* **Enrique Plata ** - *2019/09/01*