### Day 1

Made a rough sketch for the idea. Figured out that I will need to make custom api for the discord bot that will help will processing gates information of airports. Since the core of the project lies in database/api I will work on it first. 
I decided to choose postgresql for database and found out I can host it on neon. Since i will be coding in java it can be connecting via jdbc method.

- [x] Installed postgres16 & pgadmin4-web on linux
- [x] initialized and configured neon database
- [x] connected psql to neon db via string, tested if I can make changes to remote db via local shell.
-
As I have the db set up, now I will move to java code part and build the webscrapper to scrape and plug the data into database via jdbc.
