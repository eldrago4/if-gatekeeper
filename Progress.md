### Day 1

Made a rough sketch for the idea. Figured out that I will need to make custom api for the discord bot that will help will processing gates information of airports. Since the core of the project lies in database/api I will work on it first. 
I decided to choose postgresql for database and found out I can host it on neon. Since i will be coding in java it can be connecting via jdbc method.

- [x] Installed postgres16 & pgadmin4-web on linux
- [x] initialized and configured neon database
- [x] connected psql to neon db via string, tested if I can make changes to remote db via local shell.
-
As I have the db set up, now I will move to java code part and build the webscrapper to scrape and plug the data into database via jdbc.

### Day 2

- [x] ran web scrapper on source and collected 50 airports as a sample to test the app before rolling out
- [x] successfully retrieved data of 50 airports

### Day 3

- [x] worked on building the API, chose [Hono framework](https://hono.dev/) to make it in node.js
- [x] integrated API with postgresql db
- [x] built the logic of api (working with filtering reponse based on aircraft)
- [x] improved security of api by using dotenv for storing db url
-  explored vercel by performing instant rollbacks and using extensive monitoring tools provided by it to minimize backend overhead.

### Day 4

#### Agenda ->
- make ux for landing page
- test api after last security patches.

- [x] made a temporary lightweight ui for landing page since it was showing 404 before. This will help to know the running status of api. I learnt about file structure of next.js apps. Got an insight on how I can use lottie and gsap to embed images in website design and decrease resources usage.