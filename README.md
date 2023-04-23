# SE-Assessment-API-Dev.

> Akashay Anand

> Deployment link


> Articles writen while learning this contents
https://medium.com/@akashayanand1/rest-architecture-api-6b1e8bbc23d2


# Code Description

> Importing all contents which may be required in this project

<img width="359" alt="image" src="https://user-images.githubusercontent.com/131605066/233853242-810d0dd9-1b26-4066-abbd-89ddee336649.png">


> Creating an instance of FastAPI. ; // similar to express in Node js
this will help to call methods like get/post

<img width="221" alt="image" src="https://user-images.githubusercontent.com/131605066/233853056-49fb68d6-4d34-4a48-9ddd-ef64034fdaa7.png">


> This Schema model depict Pydantic model and taken from GitHub Assessment portal
//  our Mock Data is based on this Model.

<img width="835" alt="image" src="https://user-images.githubusercontent.com/131605066/233853352-d72a7a6e-fc4a-4fb9-ab52-81fd1d62daea.png">


> Mock data; // for now teasting perpus, this data set include 4 different entries and we will be performing actions on these using various endpoint url

<img width="504" alt="image" src="https://user-images.githubusercontent.com/131605066/233852616-7ba22a4b-73dd-4ede-b941-ee947944079b.png">
<note: this img only showes one set>

> /////////////// Endpoint 

// Root path
> Using decorator ; 

<img width="590" alt="image" src="https://user-images.githubusercontent.com/131605066/233853589-27293946-4d0b-4688-80c5-0d4659af6cd1.png">

> all the available set of data will be return through this address
// ex: http://127.0.0.1:8000/trades 

<img width="305" alt="image" src="https://user-images.githubusercontent.com/131605066/233853663-93f331ee-b6a6-4da7-9014-a7bd1708214a.png">

// Output

<img width="378" alt="image" src="https://user-images.githubusercontent.com/131605066/233854014-ae36c923-c25a-465e-9fc4-18d8aab83e33.png">

> Search trades
// here you can search for specific trade using 'path parameter(trade id)'
// ex // ex: http://127.0.0.1:8000/trades/2 

<img width="514" alt="image" src="https://user-images.githubusercontent.com/131605066/233854112-6f5f54a5-c28a-44cb-8c57-8447e61f1589.png">

// Output ;; object with 'id=2' is returned by api

<img width="374" alt="image" src="https://user-images.githubusercontent.com/131605066/233854236-adc01d2b-38b6-4e39-ade4-201e94330c2b.png">


>  here I have implemented filter options using 'query parameter'
// ex: http://127.0.0.1:8000/filter?search=upstox 

<img width="796" alt="image" src="https://user-images.githubusercontent.com/131605066/233854049-9020bc43-4515-4a28-946c-e5544121eacd.png">

// Output 

<img width="313" alt="image" src="https://user-images.githubusercontent.com/131605066/233854516-218b8be9-7d76-4fcc-abaa-693b5cd3ca77.png">


> Advance Filtering option
<img width="778" alt="image" src="https://user-images.githubusercontent.com/131605066/233854606-b6c52046-8899-4eb1-b893-ec0073cd9f0c.png">

///////////////////////////////////////////////////////////////




