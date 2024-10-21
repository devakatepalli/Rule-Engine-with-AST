import re

# Node class for the AST
class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.node_type}, {self.value}, {self.left}, {self.right})'

# Function to create an AST from a rule string
def create_rule(rule_string):
    tokens = re.split(r' (AND|OR) ', rule_string)
    if len(tokens) == 3:
        operator = tokens[1]
        left_operand = tokens[0]
        right_operand = tokens[2]
        return Node(node_type="operator", value=operator, 
                    left=Node(node_type="operand", value=left_operand),
                    right=Node(node_type="operand", value=right_operand))
    else:
        return Node(node_type="operand", value=rule_string)

# Function to combine multiple ASTs
def combine_rules(rule_nodes, operator="AND"):
    if len(rule_nodes) == 1:
        return rule_nodes[0]
    combined_node = rule_nodes[0]
    for rule_node in rule_nodes[1:]:
        combined_node = Node(node_type="operator", value=operator, left=combined_node, right=rule_node)
    return combined_node

# Function to evaluate an AST with given data
def evaluate_rule(ast, data):
    if ast.node_type == "operand":
        field, operator, threshold = ast.value.split()
        threshold = int(threshold)
        field_value = data.get(field)
        if operator == ">":
            return field_value > threshold
        elif operator == "<":
            return field_value < threshold
        elif operator == "==":
            return field_value == threshold
    elif ast.node_type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)
    return False

# Function to modify an AST
def modify_rule(ast, new_operator=None, new_operand=None):
    if new_operator:
        ast.value = new_operator
    if new_operand:
        ast.left = Node("operand", new_operand)
    return ast
