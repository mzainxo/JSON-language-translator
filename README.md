# Translation Service

This project is a translation service that utilizes the MarianMT model from Hugging Face's Transformers library to translate JSON data between multiple languages. The service is built using FastAPI and is designed to be efficient and scalable.

## Features

- Supports translation between English and multiple languages including French, Chinese (Simplified), Spanish, and Hindi.
- Recursively translates string values in nested JSON structures.
- API endpoint for translation requests.

## Project Structure

```
translation-service
├── src
│   ├── api
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── services
│   │   ├── __init__.py
│   │   └── translator.py
│   ├── translator_main.py
│   └── __init__.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd translation-service
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Service

To run the translation service, execute the following command:
```
uvicorn src.translator_main:app --host 0.0.0.0 --port 8000
```

You can then access the API at `http://localhost:8000/translate`.

## Docker

To build and run the Docker image for the translation service, follow these steps:

1. Build the Docker image:
   ```
   docker build -t translation-service .
   ```

2. Run the Docker container:
   ```
   docker run -p 8000:8000 translation-service
   ```

The service will be available at `http://localhost:8000/translate`.

## API Usage

To use the translation API, send a POST request to `/translate` with the following JSON body:

```json
{
    "json_data": { "key": "value" },
    "target_language": "fr"
}
```

Replace `"fr"` with the desired target language code (e.g., `"zh"` for Chinese, `"es"` for Spanish, `"hi"` for Hindi).

## License

This project is licensed under the MIT License.