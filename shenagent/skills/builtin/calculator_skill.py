import ast
import operator

from skills import skill

_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _eval(node) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_eval(node.operand))
    raise ValueError(f"不支持的表达式节点: {type(node).__name__}")


@skill
def calculate(expression: str) -> dict:
    """精确计算四则运算表达式，支持加减乘除、取余、幂运算和括号

    Args:
        expression: 数学表达式字符串，例如 (3.7 + 5.2) * 2
    """
    value = _eval(ast.parse(expression, mode="eval").body)
    return {"expression": expression, "result": value}
