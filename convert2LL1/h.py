from collections import defaultdict

def eliminate_left_recursion(grammar):
    rules = grammar.strip().split('\n')
    productions = defaultdict(list)
    new_rules = []

    # Extract productions for each non-terminal
    for rule in rules:
        non_terminal, production = rule.split(':', 1)
        productions[non_terminal.strip("; ")] = [p.strip("; ").split() for p in production.split('|')]

    # Process each non-terminal
    for non_terminal, prods in productions.items():
        new_prods, new_non_terminal_prods = eliminate_left_recursion_util(prods, non_terminal)
        new_rules.extend([f"{non_terminal} : {' | '.join(p)}" for p in new_prods])
        new_rules.extend(new_non_terminal_prods)

    return '\n'.join(new_rules)

def eliminate_left_recursion_util(productions, non_terminal):
    non_terminal_prime = non_terminal + "'"
    alpha = []
    beta = []

    # Divide productions into those with and without left recursion
    for production in productions:
        if production[0] == non_terminal:
            alpha.append(production[1:])
        else:
            beta.append(production)

    new_productions = []
    new_non_terminal_productions = []

    if alpha:
        # Create new productions for non-terminal with left recursion
        new_non_terminal_productions.extend([f"{non_terminal} : {' '.join(p)} {non_terminal_prime}" for p in beta])
        new_non_terminal_productions.extend([f"{non_terminal_prime} : {' '.join(p)} {non_terminal_prime}" for p in alpha])
        new_non_terminal_productions.append(f"{non_terminal_prime} : EPSILON")
    else:
        # If no left recursion, keep the original productions
        new_productions.extend(beta)
        new_productions.append([non_terminal_prime])

    return new_productions, new_non_terminal_productions

# Example usage:
grammar = """
E : E '+' T | T;
T : T '*' F | F;
F : '(' E ')' | 'id';
"""

new_grammar = eliminate_left_recursion(grammar)
print(new_grammar)
