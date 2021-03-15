# Stock News Alert

The purpose of this application is to alert the user whenever a specifed stock price increases or decreases by 5% and attach articles that are potentially related to such change. 

## How It Works

The application uses multiple APIs to gather data and updates the user whenever there is a change in the stock price. The first API used, alphavantage, gathers information about the current stock price such as opening and close prices. The second API, Newsapi, is used to collect news articles that are related the that given stock's company. Once the price of the stock is checked, if it decreased or increased by 5 percent in the last day, the application would make a query to the news API to gather the top articles relating to that company. Once all information is filtered, the applicaiton uses the Twilio API to send the user a message composed of the stock price and the change, as well as the heading of the top 3 articles and links to the full articles.

## How To Run It

In order to run this application, make sure that Python3 is installed on your computer. Once installed, use your text editor to change API keys, phone numbers and the Stock name. This application can also be deployed using Python Anywhere which you can schedule it to check every day at a specific time for the stock price change. Just upload your python application on there and make sure to set it to run at a specific time every day or every couple of hours. 
