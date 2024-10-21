import unittest
from ast_rule_engine import create_rule, evaluate_rule, combine_rules

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        rule_string = "age > 30 AND income > 50000"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)
        self.assertEqual(ast.node_type, "operator")
        self.assertEqual(ast.left.value, "age > 30")
        self.assertEqual(ast.right.value, "income > 50000")
    
    def test_evaluate_rule(self):
        rule_string = "age > 30 AND income > 50000"
        ast = create_rule(rule_string)
        data = {"age": 35, "income": 60000}
        result = evaluate_rule(ast, data)
        self.assertTrue(result)
    
    def test_combine_rules(self):
        rule1 = create_rule("age > 30")
        rule2 = create_rule("income > 50000")
        combined_ast = combine_rules([rule1, rule2], "AND")
        self.assertEqual(combined_ast.node_type, "operator")
        self.assertEqual(combined_ast.left.value, "age > 30")
        self.assertEqual(combined_ast.right.value, "income > 50000")

if __name__ == '__main__':
    unittest.main()
