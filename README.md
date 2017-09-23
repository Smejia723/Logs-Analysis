# Logs-Analysis
Udacity project, I was tasked to create a reporting tool that prints out reports (in plain text) 
based on the data in a database. This reporting tool is a Python program using the psycopg2 module and 
SQL format to connect said database.

# what are the questions the reporting tool should answer:
-What are the most popular three articles of all time?
-Who are the most popular article authors of all time?
-On which days did more than 1% of requests lead to errors?

# Running the Program:
*these instructions are for if you have the Udacity-provided Virtual machine and Udacity-provided database, 
hence being a Udacity project*

Start the VM with a Unix-like command line terminal, such as terminal for Mac or Gitbash for Windows:
  1.  Within the VM, navigate to cd ~/Downloads/FSND-Virtual-Machine/vagrant
  2.  Run vagrant up
  3.  Run vagrant ssh
  3.  Connect to the database by running `psql -d news -f newsdata.sql`
  4.  run python logs.py
  5.  enjoy results of the three awensers
  5.  Exit VM with ctrl D when finished enjoying

#Required files and programs
1. VirtualBox: https://www.virtualbox.org/wiki/Downloads
2. git bash
3. newsdata.sql
4. python 2.7 or 3
5. logs.py
6. psycopg2 library
7. PostgreSQL: https://www.postgresql.org/download/
8. vagrant: https://www.vagrantup.com/
9. fsnd-virtual-machine zip file from udacity
