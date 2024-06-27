
# Sentiment Analyzer from Hotel Reviews
![_365fea16-fd90-483b-8c4c-df3613e2f5cb Background Removed Small Background Removed](https://github.com/SantiAlmancy/Analizador-de-Sentimientos/assets/107863034/5d321be2-ea9f-44ef-9d2b-8b8e177ce136)

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

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get reviews from hotels

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Post reviews

```http
  POST /api/reviews
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Post new hotels

```http
  POST /api/hotels/add
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |



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

- **Build the Project**: Build the project for production.
    ```bash
    npm run build
    ```

- **Start the Server**: Start the production server.
    ```bash
    npm start
    ```

#### How many languages does the model detect?

At the moment just English. Spanish comming soon!

#### What is Hugging Face?

Hugging Face is a company specializing in natural language processing technologies and provides tools and models for building applications using machine learning.

#### How many states has the sentiment analyzer?

It has two states. Positive and Negative.

## Authors 4️⃣

- [@mathpro28](https://github.com/mathpro28)
- [@SantiAlmancy](https://github.com/SantiAlmancy)
- [@SebastianItamari](https://github.com/SebastianItamari)
- [@AleDiazT](https://github.com/AleDiazT)
