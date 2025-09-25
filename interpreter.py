# interpreter.py
import sys

# Environment to store variables
env = {}

# Function to evaluate expressions
def evaluate(expr):
    # Replace variables with their values
    for var in env:
        expr = expr.replace(var, str(env[var]))
    try:
        # Evaluate arithmetic expressions or return string
        if expr.startswith('"') and expr.endswith('"'):
            return expr.strip('"')
        return eval(expr)
    except Exception as e:
        return f"Error: {e}"

# Read file passed as argument
file_path = sys.argv[1]
with open(file_path, 'r') as f:
    lines = f.readlines()

# Execute each line
for line in lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith("LET "):
        # LET x = 10
        parts = line.split()
        var_name = parts[1]
        value = " ".join(parts[3:])
        env[var_name] = evaluate(value)
    elif line.startswith("PRINT "):
        # PRINT x + y
        expr = line[6:]
        print(evaluate(expr))
    else:
        print(f"Unknown command: {line}")
