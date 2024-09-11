---
draft: false
title: "Database Connection via JNDI"
aliases: "/connection-to-db-via-jndi/"
seoindex: "index, follow"
seotitle: "Database Connection via JNDI"
seokeywords: "jndi tutorial, jndi example, java jndi, tomcat jndi, jndi tomcat, jndi java, tomcat jndi example, jndi server, java jndi tutorial, java jndi example, jndi connection, jndi in java, jndi environment, jndi in tomcat"
seodesc: "See the tutorial on how to connect to the database using JNDI on the example of Java hosting environment on the base of Tomcat application server and MySQL database."
menu:
    docs:
        title: "Database Connection via JNDI"
        url: "/connection-to-db-via-jndi/"
        weight: 60
        parent: "database-hosting"
        identifier: "connection-to-db-via-jndi.md"
---

# Connection to DB using JNDI

To connect to DB using JNDI you have to perform the following steps:

* Log onto PaaS dashboard
* Create an environment
* Add database node into your environment
* Modify some configuration files in a web-app
* Create a connection in a java-class

Let's do it step-by-step:

1\. Create environment with database (MySQL in our case):

![environment with MySQL](01-env-with-mysql.png)

2\. Create a new user in a database:


```
Database name : jelasticDb
User_name : jelastic
Password : jelastic
```

How to create new user - [click here](/connection-to-mysql/).

3\. Modify configuration files in your web-application:

- ***context.xml***

```xml
<Context antiJARLocking="true" path="/JNDI">
    <Resource name="jdbc/jelasticDb" auth="Container" type="javax.sql.DataSource"
               maxActive="100" maxIdle="30" maxWait="10000"
               username="jelastic" password="jelastic" driverClassName="com.mysql.jdbc.Driver"
               url="jdbc:mysql://mysql-jndi-example.{hoster_domain}/jelasticDb"/>
</Context>
```

- ***web.xml***

```xml
<resource-ref>
 <description>MySQL Datasource example</description>
 <res-ref-name>jdbc/jelasticDb</res-ref-name>
 <res-type>javax.sql.DataSource</res-type>
 <res-auth>Container</res-auth>
</resource-ref>
```

4\. Create connection in java-class:

```java
public class MyConnection {

    private DataSource dataSource;

    public MyConnection() {
        try {

            InitialContext context = new InitialContext();
            dataSource = (DataSource) context.lookup("java:comp/env/jdbc/jelasticDb");

        } catch (NamingException ex) {
            Logger.getLogger(MyConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public Connection getConnection() {
        Connection conn = null;
        try {
            conn = dataSource.getConnection();
        } catch (SQLException ex) {
            Logger.getLogger(MyConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
        return conn;
    }
}
```


## What's next?

* [Create DB Server](/database-hosting/)
* [Connection to DB using Hibernate](/connect-db-hibernate/)
* [Database Configuration](/database-configuration-files/)