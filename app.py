from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app)

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n):
    return n > 1 and sum(i for i in range(1, n) if n % 1 == 0) == n

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d**power for d in digits) == n

# Function to get the sum of digits of a number
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

# Function to get fact from Numbers API
def get_fun_fact(n):
    response = requests.get(f"http://numbersapi.com/{n}/math")
    return response.text if response.status_code == 200 else "No fun fact available."   

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Validate input
    if not number or not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)

    # Determine properties
    prime_status = is_prime(number)
    perfect_status = is_perfect(number)
    armstrong_status = is_armstrong(number)
    odd_even = "odd" if number % 2 != 0 else "even"
    properties = [odd_even]
    
    if armstrong_status:
        properties.insert(0, "armstrong")

    # Get fun fact
    fun_fact = get_fun_fact(number)

    # Prepare response
    response = {
        "number": number,
        "is_prime": prime_status,
        "is_perfect": perfect_status,
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }

    return jsonify(response), 200



  
