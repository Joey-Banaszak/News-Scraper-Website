# News-Scraper-Website
Online web scraper meant to make searching for news stories easier


LiveLens is a news searching website designed to provide quick access to news articles from a wide variety of trusted sources. Designed to be a student’s best friend, LiveLens is meant to make collecting and citing sources easier than ever. Currently LiveLens is only a prototype, its current features include keyword or source based searches and a database implementation meant to collect user searches for later. As development continues we hope to allow our users the ability to cite sources in a variety of ways, improve the UI, implement a username based account login system, and finally a email/SMS based notification system for updates on stories.

Before running the server we downloaded the mySQL package from pip to connect our data base. To connect the databse this command was used: sudo systemctl start mysql.
Inside the data base I used the sql shell to start running the database using this command: USE news_scraper; (followed by) EXIT;.

To run LiveLens I created a venv virtual environment on my server and ran the server using this command: nohup python3 app.py

It is important that each html file be place in a template directory inside of the server. For this current instance style is run out of the public directory on the server, though that is optional, however if that were modified the app.py file would need to be altered as well. 

The app.py file is the core of the project conencting each branch of the architecture and handling all major processes to be displayed to the user. 
