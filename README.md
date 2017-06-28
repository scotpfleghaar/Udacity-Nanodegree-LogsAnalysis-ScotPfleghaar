# Udacity-Nanodegree-LogsAnalysisProject-ScotPfleghaar

# Logs Analysis

> Scot Pfleghaar

## About
This is the third project provided by Udacity’s Nanodegree program. Here is the project synopsis:

> “You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

> The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

> The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.”

## To Run

### You will need the following:
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)
### Setup
1. Install Vagrant And VirtualBox
2. Clone this repository: [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)

### To Run

Launch the Vagrant VM inside Vagrant sub-directory using the following command:
  
  ```
    $ vagrant up
  ```
Then Log into the vagrant vm using command:
  
  ```
    $ vagrant ssh
  ```
To Load the data use this command:
  
  ```
    psql -d news -f newsdata.sql
  ```

The database includes three tables:
- Authors table
- Articles table
- Log table

To preform the logs analysis, run `python newsreports.py` from the command line.