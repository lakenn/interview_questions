# def divide(a, b):
#     try:
#         result = a / b
#         print(f"The result of {a} / {b} is {result}")
#     except ZeroDivisionError as e:
#         print(f"Error: Cannot divide by zero. {e}")
#     except TypeError as e:
#         print(f"Error: Invalid input type. {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred. {e}")
#     finally:
#         print("Execution of the divide function is complete.")
#
# # Example usage
# divide(10, 2)  # Valid division
# divide(10, 0)  # ZeroDivisionError
# divide(10, 'a')  # TypeError


class ExceptionNode:
    def __init__(self, name):
        self.name = name


class TryBlock:
    def __init__(self):
        self.exceptions = set()  # **Encapsulation of exceptions**
        self.catches = set()     # **Encapsulation of catches**

    def add_exception(self, exception_name):
        self.exceptions.add(exception_name)

    def add_catch(self, exception_name):
        self.catches.add(exception_name)

    def can_catch(self, exception_name):
        return exception_name in self.catches  # **Simplifies catch checking**


class ASTNode:
    def __init__(self, node_type, children=None, exception=None):
        self.node_type = node_type
        self.children = children or []
        self.exception = exception


def parse_source_code():
    # This is a simplified example. In a real implementation, you would parse
    # the source code to build this AST.
    return ASTNode('root', [
        ASTNode('try', [
            ASTNode('throw', exception=ExceptionNode('ExceptionA')),
            ASTNode('catch', exception=ExceptionNode('ExceptionA'))
        ]),
        ASTNode('throw', exception=ExceptionNode('ExceptionB'))
    ])


def detect_uncaught_exceptions(ast):
    try_stack = []  # **Maintains nesting of try blocks**
    uncaught_exceptions = []  # **Tracks globally uncaught exceptions**

    def traverse_node(node):
        if node.node_type == 'try':
            try_block = TryBlock()  # **Start a new try block**
            try_stack.append(try_block)

        elif node.node_type == 'throw':
            exception_name = node.exception.name
            if try_stack:
                try_stack[-1].add_exception(exception_name)  # **Add exception to current try block**
            else:
                uncaught_exceptions.append(exception_name)  # **Handle global uncaught exceptions**

        elif node.node_type == 'catch':
            exception_name = node.exception.name
            if try_stack:
                try_stack[-1].add_catch(exception_name)  # **Register catch for current try block**

        for child in node.children:
            traverse_node(child)

        if node.node_type == 'try':
            try_block = try_stack.pop()  # **Backtrack the current try block**
            if try_stack:
                parent_try_block = try_stack[-1]  # **Propagate uncaught exceptions**
                for exception in try_block.exceptions:
                    if not try_block.can_catch(exception):
                        parent_try_block.add_exception(exception)
            else:
                for exception in try_block.exceptions:
                    if not try_block.can_catch(exception):
                        uncaught_exceptions.append(exception)

    traverse_node(ast)
    return uncaught_exceptions


# Example usage
ast = parse_source_code()
uncaught_exceptions = detect_uncaught_exceptions(ast)
print("Uncaught Exceptions:", uncaught_exceptions)
