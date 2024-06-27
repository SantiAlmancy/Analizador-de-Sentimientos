
# Sentiment Analyzer from Hotel Reviews
![_365fea16-fd90-483b-8c4c-df3613e2f5cb Background Removed Small Background Removed](https://github.com/SantiAlmancy/Analizador-de-Sentimientos/assets/107863034/5d321be2-ea9f-44ef-9d2b-8b8e177ce136)

This proyect will predict if the comment introduced is either positive or negative based on a trainning with hundred of thounsands of comments from many websites and hotels.




## Objective
The objective of this project is to be able to detect what kind of sentiment is expressing the review from an hotel. This tool will help owners to take better and strategic desitions for their business.

## Tecnologies used for the web app
1. **BackEnd**
   - Django
   - Djando REST Framework 
3. **FrontEnd**
   - React
   - React DOM
   - Babel
   - ESLint
   - React Router

## Installation
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

## Deployment

To deploy this project run

```bash
  npm run deploy
```


## API Reference

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


#### add(num1, num2)

Takes two numbers and returns the sum.


## Documentation

- For more information, you can checkout our [Official Documentation](https://docs.google.com/document/d/1FK-aOhOsSnqMsrD8_Bw9apPNRCgE5sskCMFg69owqPM/edit?usp=sharing).
- And to check our resources, visit the [Google Drive Folder]().


## Authors

- [@mathpro28](https://github.com/mathpro28)
- [@SantiAlmancy](https://github.com/SantiAlmancy)
- [@SebastianItamari](https://github.com/SebastianItamari)
- [@AleDiazT](https://github.com/AleDiazT)

