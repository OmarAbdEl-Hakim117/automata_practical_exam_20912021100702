# Define a sample grammar
# Grammar: S -> S + S | S * S | a
grammar = {
    'S': [['S', '+', 'S'], ['S', '*', 'S'], ['a']]
}

def generate_trees(string, symbol, grammar):
    """
    Recursively generate all possible parse trees for a given string and symbol.
    Each tree is represented as a nested list structure.
    """
    if not string:
        return []

    # If the symbol is a terminal (not expandable), check for direct match
    if symbol not in grammar:
        return [[symbol]] if string == symbol else []

    trees = []  # Store all valid trees for this symbol generating this string

    # Try each production rule for the current symbol
    for production in grammar[symbol]:
        if len(production) == 1:
            # Single symbol production (like S -> a)
            if string == production[0]:
                trees.append([symbol, production[0]])
        elif len(production) == 3:
            # Binary productions (like S -> S + S or S * S)
            for i in range(1, len(string) - 1):
                # Split the string on an operator
                left = string[:i]
                middle = string[i]
                right = string[i+1:]

                if middle != production[1]:
                    continue  # Not matching operator in production

                left_trees = generate_trees(left, production[0], grammar)
                right_trees = generate_trees(right, production[2], grammar)

                for lt in left_trees:
                    for rt in right_trees:
                        trees.append([symbol, lt, middle, rt])
    return trees

# Example input
input_str = "a+a+a"
# Parse it starting from start symbol 'S'
parse_trees = generate_trees(input_str, 'S', grammar)

# Output
print(f"Number of parse trees: {len(parse_trees)}")
print("Grammar is ambiguous" if len(parse_trees) > 1 else "Grammar is unambiguous")
