
# Sentiment Analyzer from Hotel Reviews



![performing-twitter-sentiment-analysis1 Background Removed](https://github.com/SantiAlmancy/Analizador-de-Sentimientos/assets/107863034/8da463ce-0e0f-4b39-9f39-b107e272615d)




This proyect will predict if the comment introduced is either positive or negative based on a trainning with hundred of thounsands of comments from many websites and hotels.




## Objective 🏆
The objective of this project is to be able to detect what kind of sentiment is expressing the review from an hotel. This tool will help owners to take better and strategic desitions for their business.

## Installation ⚙️
In order to try out the sentiment analyzer first you need to install the requirements.
Make sure you have Python 3.11 installed. You can download it from [python.org](https://www.python.org/downloads/).

### Using `requirements.txt`

To set up the environment using `requirements.txt`, follow these steps:

- **Create a virtual environment**:
   ```sh
   python -m venv venv

- **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
    - On MacOS: 
        ```sh 
        source venv/bin/activate
- **Install the dependencies**:
    ```sh
    pip install -r requirements.txt

## Demo ▶️
![sa-demo](https://github.com/SantiAlmancy/Analizador-de-Sentimientos/assets/107863034/806ba179-1ae2-46b4-96fb-f82a35a3ef18)


## Technologies used for the web app ⚒️
1. **BackEnd**
   - Django
   - Djando REST Framework 
3. **FrontEnd**
   - React
   - React DOM
   - Babel
   - ESLint
   - React Router

## Deployment ☁️

To deploy this project run

```bash
  npm run deploy
```


## API Reference 🤖

#### Get all items

```http
  GET /api/hotels
```
Retrieves a list of existing hotels (limited to 20 rows).
```json
[
    {
        "hotel_id": "H00001",
        "hotel_name": "BEST WESTERN The Hotel California",
        "hotel_class": 3
    },
    {
        "hotel_id": "H00002",
        "hotel_name": "Hotel Beresford",
        "hotel_class": 4
    }
]

```

#### Get reviews from hotels

```http
  GET /api/hotels/<hotel_id>/reviews/
```
Retrieves a list of reviews for a specific hotel (limited to 20 rows).

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `hotel_id`| `string` | **Required**. Id of item to fetch |

```json
[
    {
        "review_id": 1,
        "title": "Great Stay",
        "review": "I had a wonderful experience at this hotel.",
        "value": "positive"
    },
    {
        "review_id": 2,
        "title": "Average Experience",
        "review": "The hotel was okay, but could be better.",
        "value": "negative"
    }
]

```

#### Post reviews

```http
  POST /api/reviews
```

Creates a new review for a hotel.

- Request: 
   ```json
   {
       "hotel_id": "H00001",
       "title": "Amazing Service",
       "review": "The service at this hotel was exceptional!",
       "value": "positive"
   }
   ```
- Response:
  ```json
  {
       "review_id": 101,
       "hotel_id": "H00001",
       "title": "Amazing Service",
       "review": "The service at this hotel was exceptional!",
       "value": "positive"
   }
  ```

#### Post new hotels

```http
  POST /api/hotels/add
```
Adds new hotels to the database.

- Request: 
   ```json
   [
       {
           "hotel_id": "H00001",
           "hotel_name": "BEST WESTERN The Hotel California",
           "hotel_class": 3
       },
       {
           "hotel_id": "H00002",
           "hotel_name": "Hotel Beresford",
           "hotel_class": 4
       }
   ]
   ```
- Response:
  ```json
  {
       "message": "Hotels created successfully"
  }
  ```



## Documentation 📚

- For more information, you can checkout our [Official Documentation](https://docs.google.com/document/d/1FK-aOhOsSnqMsrD8_Bw9apPNRCgE5sskCMFg69owqPM/edit?usp=sharing).
- And to check our resources, visit the [Google Drive Folder]().

## FAQ 🤔

#### How to run the backend?

You need to follow these commands:
- **Make Migrations**: Create new migrations based on the changes detected in your models.
    ```bash
    python manage.py makemigrations
    ```

- **Apply Migrations**: Apply the migrations to your database.
    ```bash
    python manage.py migrate
    ```

- **Start the Server**: Start the development server.
    ```bash
    python manage.py runserver
    ```

#### How to run the frontend?

- **Install npm**: Install npm dependency.
    ```bash
    npm install
    ```

- **Build the Project**: Build the project for production.
    ```bash
    npm run build
    ```

- **Start the Server**: Start the production server.
    ```bash
    npm start
    ```

#### Does it only detect English reviews?

No! It can detect many languages such as Spanish, German, French, etc. Thanks to the auto-translation if it detects that the comment is not English.

#### What is Hugging Face?

Hugging Face is a company specializing in natural language processing technologies and provides tools and models for building applications using machine learning.

#### How many states has the sentiment analyzer?

- If you chose Keras, it will have **Positive** and **Negative**. 
- But if you chose Transformers it has the following states: **very_negative**, **negative**, **neutral**, **positive** and **very positive**.

## Authors 4️⃣

- [@mathpro28](https://github.com/mathpro28)
- [@SantiAlmancy](https://github.com/SantiAlmancy)
- [@SebastianItamari](https://github.com/SebastianItamari)
- [@AleDiazT](https://github.com/AleDiazT)
