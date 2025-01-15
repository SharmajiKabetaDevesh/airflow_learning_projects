Airflow: a platform to programmatically author, schedule and monitor workflows, things became simple and efficient.



So, what does this Apache Airflow provides, such that the industry craves for it .... 



DAGS?

   It consists of DAGS (Directed Acyclic Graph) which define the sequence of process to take place i.e. first preprocess, second train and then evaluate. They are directed means sequence has to be followed no going back defines the relationship between various tasks.



Scheduled jobs?

   Suppose your workflow must be run every Sunday, you can schedule it in such a way that it will only be trigger on Sundays. How cool is this?

In simple terms, you can automate your workflow. The best part of automation is you can avoid future human errors.

Your DAG can be easily monitored, controlled, and triggered.



Operator?

      Defines what to do (e.g., run a Python function, execute a Bash command, move files).



XCom (Cross — Communication)?

    Communication among two operators. If any operator returns some value, it gets store in xcom, airflow provides a mechanism to pull xcom value using xcom_pull() and use it in some other operation and also to push value using xcom-push().




Issues faced while Implementing:

1) Installing it on windows is not possible, we have to use docker images.

2) Docker images are resource hungry and after writing a DAG you have to again restart it.

3) Use a Linux based OS to directly install the packages no overhead of docker and it can detect the new DAGS no need to restart.

![Screenshot (440)](https://github.com/user-attachments/assets/d057f8d1-832b-4c0a-bba1-7e3b4ab1921b)
![Screenshot (443)](https://github.com/user-attachments/assets/3b233c67-b6ce-4656-90a0-db33dc6a3e57)
![Screenshot (444)](https://github.com/user-attachments/assets/bd6d93f9-3558-4631-b405-cd4ef393607d)
![Screenshot (445)](https://github.com/user-attachments/assets/55d8b009-930f-4fd1-b184-2721bf5de518)

