# Random Vector API

This is a Flask-based API that generates a random 500-dimensional vector based on input sentences.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Generating Random Vectors](#generating-random-vectors)
  - [Cached Random Vectors](#cached-random-vectors)
- [API Documentation](#api-documentation)
- [Enhancements](#enhancements)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/amit2014/random-vector-api.git
   cd random-vector-api

2. Create and activate a virtual environment (recommended):
   
   ```
   python3 -m venv venv
   source venv/bin/activate
   
3. Install the required dependencies:
   
   ```
   pip install -r requirements.txt 

## Usage

### Generating Random Vectors

To generate a random vector based on an input sentence, use the /v1/random_vector endpoint:

    ```
    curl -X POST -H "Content-Type: application/json" -d '{"sentence": "This is an example     sentence"}' http://127.0.0.1:8000/v1/random_vector
	
### Cached Random Vectors

To access cached random vectors, use the /cached_random_vector endpoint:

    ```
    curl http://127.0.0.1:8000/cached_random_vector

## API Documentation

The API is documented using Swagger UI. You can access the documentation by visiting http://127.0.0.1:8000/swagger when the app is running.


## Enhancements


The API has been enhanced to include the following features:

1. Versioning: API endpoints are versioned under /v1.
2. Caching: Cached random vectors are available at /cached_random_vector.
3. Pagination: Pagination for large response payloads can be implemented using query parameters.
4. API Monitoring: Basic monitoring using logging is implemented. Advanced monitoring tools like Prometheus and Grafana can be integrated.

## Contributing

Contributions are welcome!

## License

This project is licensed under the MIT License.


