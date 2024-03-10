##Project Title: Google Sheets to RDBMS and VectorDB Ingestion Utility

#Problem Statement

Many small to medium level enterprises often receive table information in the form of Excel or Google Sheets. This data needs to be ingested into a Relational Database Management System (RDBMS) or a Vector Database (VectorDB) like ChromaDB. The process of converting this data into a suitable format for ingestion can be time-consuming and error-prone.  

#Solution
This utility aims to automate and simplify the process of ingesting data from Google Sheets into an RDBMS or ChromaDB. It fetches data from Google Sheets and generates Data Definition Language (DDL) and Data Manipulation Language (DML) scripts. These scripts can be directly ingested into an RDBMS.  For VectorDB ingestion, the utility converts the data into a document format that can be added to a collection in ChromaDB.  

#How it Works

1. The utility fetches data from a specified Google Sheet.
2. It then generates DDLs and DMLs based on the fetched data.
3. The generated DDLs and DMLs can be directly ingested into an RDBMS.
4. For ChromaDB ingestion, the utility converts the data into a document format.
5. The document is then added to a specified collection in ChromaDB.

This utility simplifies the process of data ingestion from Google Sheets to an RDBMS or ChromaDB, making it a valuable tool for small to medium level enterprises.