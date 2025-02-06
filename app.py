from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math
from collections import OrderedDict

app = Flask(__name__)
CORS(app)

# Function to check if a number is prime
def is_prime(n):
    if n < 2 or n % 1 != 0:  # Exclude floats and numbers < 2
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(n):
    if n < 1 or n % 1 != 0:  # Exclude floats and negative numbers
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# Function to check if a number is an Armstrong number
def is_armstrong(n):
    if n < 0:
        return False
    digits = [int(d) for d in str(abs(int(n)))]  # Convert to integer for Armstrong check
    power = len(digits)
    return sum(d**power for d in digits) == abs(int(n))

# Function to get the sum of digits of a number
def digit_sum(n):
    return sum(int(digit) for digit in str(abs(int(n))))  # Sum absolute digit values

# Function to get fact from Numbers API
def get_fun_fact(n):
    response = requests.get(f"http://numbersapi.com/{n}/math")
    return response.text if response.status_code == 200 else "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Validate input: Check if input is None or not a valid number
    try:
        number = float(number)  # Convert to float for decimal support
    except (ValueError, TypeError):
        return jsonify({"number": number, "error": "Invalid input. Must be a number."}), 400

    # Determine properties
    prime_status = is_prime(number)
    perfect_status = is_perfect(number)
    armstrong_status = is_armstrong(number)
    odd_even = "odd" if number % 2 != 0 else "even"
    properties = [odd_even]

    if armstrong_status:
        properties.insert(0, "armstrong")

    # Get fun fact
    fun_fact = get_fun_fact(int(number))  # Convert to int to match Numbers API format

    # Prepare response
    response = OrderedDict([
        ("number", number),
        ("is_prime", prime_status),
        ("is_perfect", perfect_status),
        ("properties", properties),
        ("digit_sum", digit_sum(number)),
        ("fun_fact", fun_fact)
    ])

    return jsonify(response), 200  # Always return 200 for valid numbers



  
