# Selenium Automation of Train Seats Availability

IRCTC website, is a Indian government website which facilitates booking of train tickets and show availability of the seats for a particular route.
There are four (or sometimes five) classes of tickets for each train available on that route and the checking availability across all classes was a cumbersome
process given the complexity of the website. The website interface looked something like below:

<img width="800" alt="image" src="https://user-images.githubusercontent.com/50548928/168699851-c8aa173c-3bd6-4349-95b2-8d37795d44b5.png">

The problem was the number of clicks you have to do to check availability across all the classes. In the example above, to know seats availability 
across all the classes would have required around 60 clicks on the website! (3 clicks per class).

Hence I developed an automation with Selenium, to simulate these 60 clicks and at the same time scrape the data and present it in a simple 
easy to read table format like this:

<img width="800" alt="image" src="https://user-images.githubusercontent.com/50548928/168700658-71dd2402-e8b0-43ca-b444-4de887684a82.png">

Complete demo of the webapp:

https://user-images.githubusercontent.com/50548928/168700851-c6aeba79-b9e9-4a10-8c74-e1e2511e21d6.mov


