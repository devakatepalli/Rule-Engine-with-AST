from flask import Flask, request, jsonify
from ast_rule_engine import create_rule, combine_rules, evaluate_rule, modify_rule

app = Flask(__name__)

# Route to create a rule
@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get("rule_string")
    ast = create_rule(rule_string)
    return jsonify({"AST": repr(ast)})

# Route to combine rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    rules = request.json.get("rules")
    rule_asts = [create_rule(rule) for rule in rules]
    combined_ast = combine_rules(rule_asts)
    return jsonify({"Combined_AST": repr(combined_ast)})

# Route to evaluate a rule
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    rule_ast = create_rule(request.json.get("rule_string"))
    data = request.json.get("data")
    result = evaluate_rule(rule_ast, data)
    return jsonify({"Result": result})

# Route to modify a rule
@app.route('/modify_rule', methods=['POST'])
def modify_rule_api():
    rule_string = request.json.get("rule_string")
    new_operator = request.json.get("new_operator")
    new_operand = request.json.get("new_operand")
    ast = create_rule(rule_string)
    modified_ast = modify_rule(ast, new_operator=new_operator, new_operand=new_operand)
    return jsonify({"Modified_AST": repr(modified_ast)})

# Root route to handle the base URL
@app.route('/')
def home():
    return "Welcome to the Rule Engine API!"

# Route to handle favicon request to avoid 404
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return a 204 No Content response to skip favicon request

if __name__ == '__main__':
    app.run(debug=True)
