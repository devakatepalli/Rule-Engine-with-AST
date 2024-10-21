# Rule Engine with Abstract Syntax Tree (AST)

## Overview

This application is a simple rule engine designed to evaluate user eligibility based on various attributes such as age, department, income, and spend. It utilizes an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic creation, combination, modification, and evaluation of rules.

## Features

- Create rules using a defined string format.
- Combine multiple rules into a single AST.
- Evaluate rules against user data to determine eligibility.
- Modify existing rules by changing operators or operands.
- Unit tests to verify the functionality of the application.

## Technologies Used

- Python 3.13
- Flask (for the API)
- Unit testing with unittest

## Directory Structure

rule-engine-app/
│
├── app.py                  # Flask API
├── ast_rule_engine.py       # Logic for AST, rule creation, evaluation
├── requirements.txt         # Python dependencies
└── tests/
    └── test_rules.py        # Test cases


## Getting Started

### Prerequisites

- Python 3.13 installed on your system.
- pip (Python package installer).

### Installation

1. cd rule-engine-app

2. Create necessary files:
   type nul > app.py
   type nul > ast_rule_engine.py
   type nul > requirements.txt
   mkdir tests
   type nul > tests\test_rules.py

3. Add dependencies to requirements.txt:
      Open requirements.txt and add:
            Flask
            pytest
   
4. Install the required dependencies:
      pip install -r requirements.txt

5. Start the Flask application:
      python app.py

      API will now be running at http://127.0.0.1:5000

### Endpoints
I am using PostMan API

1. Create Rule
   
   Endpoint: /create_rule
   Method: POST
   Request Body:
   json
   {
      "rule_string": "age > 30 AND income > 50000"
   }
   
2. Combine Rules

   Endpoint: /combine_rules
   Method: POST
   Request Body:
   json
   {
      "rules": ["age > 30", "income > 50000"]
   }

3. Evaluate Rules

   Endpoint: /evaluate_rule
   Method: POST
   Request Body:
   json
   {
      "rule_string": "age > 30 AND income > 50000",
      "data": {
               "age": 35,
               "income": 60000
              }
   }

   4. Modify Rules

   Endpoint: /modify_rule
   Method: POST
   Request Body:
   json
   {
      "rule_string": "age > 30",
      "new_operator": "OR",
      "new_operand": "income < 50000"
   }

### Running Tests

To run the unit tests, navigate to the rule-engine-app directory and run the tests

python -m unittest discover tests/


