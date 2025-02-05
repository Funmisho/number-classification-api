# Number Classification API

This is a simple API that takes a number and returns interesting mathematical properties about it, including a fun fact. The API is built using Flask and deployed on AWS Lambda using Zappa.

## API Endpoint

**GET** `/api/classify-number?number=<number>`

### Example Request
GET https://<your-api-id>.execute-api.us-east-1.amazonaws.com/number-classification-api/api/classify-number?number=371
Copy
### Example Response (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
Example Response (400 Bad Request)
jsonCopy{
    "number": "alphabet",
    "error": true
}
Features

Classifies the given number and checks whether it is:

Prime
Perfect
Armstrong
Odd/Even


Returns a fun fact about the number using the Numbers API
Handles CORS (Cross-Origin Resource Sharing) for cross-origin requests

Technologies Used

Python: Programming language for the backend API
Flask: Web framework for creating the API
Zappa: Used for deploying the API to AWS Lambda and API Gateway
AWS Lambda: For running the code in a serverless environment
API Gateway: To expose the Lambda function as a publicly accessible API

Setup and Installation

Clone the repository:
bashCopygit clone https://github.com/your-username/number-classification-api.git
cd number-classification-api

Install dependencies:
bashCopypip install -r requirements.txt

Deploy using Zappa:

First, configure Zappa with zappa init
Then, deploy your app using zappa deploy


Access the API using the generated URL from API Gateway

Dependencies

Flask
flask_cors
requests
Zappa (for deployment)

License
This project is open-source and available under the MIT License.
