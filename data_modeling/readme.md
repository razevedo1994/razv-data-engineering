# Data Modeling

**Databases**: A database is a structured repository or collection of data that is stored and retrieved electronically for use in applications. Data can be stored, updated, or deleted from a database.

**Database Management System (DBMS)**: The software used to access the database by the user and application is the database management system.

- [Database](https://en.wikipedia.org/wiki/Database)

- [Introduction to DBMS](https://www.geeksforgeeks.org/introduction-of-dbms-database-management-system-set-1/)

Data Modeling at a high level is all about an abstraction that organizes elements of data and how they relate to each other. The process pf data modeling is to organize data into a database system to ensure that your data is persisted and easily usable by you in your organization.
#
## The Process of Data Modeling

- **Gather requirements**: The team must gather requirements from the application team, the business users, and our end users to understand that data must be retained and served as a business or the end-users. We need to map out that our data must be stored and persisted and how that data will relate to each other.

- **Conceptual Data Modeling**: This is mapping the concepts of the data that you have or will have. The relationship between your data will be organized in this process.

- **Logical Data Modeling**: LOgical data modeling is done where the conceptual models are mapped to logical models using the concept of tables, schemas, and columns.

- **Physical Data Modeling**: Physical data modeling is done transforming the logical data modeling to the databases definition language or DDL, to be able to create the databases, the tables, and the schemas. We will be writing our DDLs to create tables in the way that the database understands.

The correct order of the Data Modeling process is: 
- Conceptual -> Logical -> Physical

**Does data modeling happen before you create a database, or is it an iterative process?**

- It's definitely an iterative process. Data engineers continually reorganize, restructure, and optimize data models to fit the needs of the organization.

**How is data modeling different from machine learning modeling?**

- Machine learning includes a lot of data wrangling to create the inputs for machine learning models, but data modeling is more about how to structure data to be used by different people within an organization. You can think of data modeling as the process of designing data and making it available to machine learning engineers, data scientists, business analytics, etc., so they can make use of it easily.
#

