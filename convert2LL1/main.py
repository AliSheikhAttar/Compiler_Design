from collections import defaultdict
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


def left_factor(grammar):
    rules = grammar.strip().split('\n')
    productions = defaultdict(list)
    new_rules = []

    # Extract productions for each non-terminal
    for rule in rules:
        non_terminal, production = rule.split(':', 1)
        productions[non_terminal.strip()] = [p.strip().split() for p in production.split('|')]

    # Process each non-terminal
    for non_terminal, prods in productions.items():
        new_prods = left_factor_util(prods)
        new_rules.extend([f"{non_terminal} : {' | '.join(p)}" for p in new_prods])

    return '\n'.join(new_rules)

def left_factor_util(productions):
    new_productions = []

    while productions:
        current = productions.pop(0)
        similar = [p for p in productions if p[0] == current[0]]

        if similar:
            # Find the longest common prefix
            common = longest_common_prefix([current] + similar)
            new_productions.append(common + [current[0] + "'"])

            # Update the original productions and add new ones
            for prod in [current] + similar:
                if len(common) == len(prod):
                    productions.remove(prod)
                else:
                    new_productions.append(prod[len(common):])
        else:
            # If no common prefix, keep the original production
            new_productions.append(current)

    return new_productions

def longest_common_prefix(productions):
    prefix = []

    for symbols in zip(*productions):
        if len(set(symbols)) == 1:
            prefix.append(symbols[0])
        else:
            break

    return prefix
from collections import defaultdict

def compute_first_sets(grammar):
    first_sets = defaultdict(set)
    visited = set()

    # Extract productions
    productions = defaultdict(list)
    for rule in grammar.strip().split('\n'):
        non_terminal, production = rule.split(':', 1)
        if non_terminal.strip() not in productions:
            productions[non_terminal.strip()] = [p.strip("; ").split() for p in production.split('|')]
        else:
            productions[non_terminal.strip()].extend([p.strip("; ").split() for p in production.split('|')])
    # Extract terminals and non-terminals
    non_terminals = set(productions.keys())
    terminals = set()
    for prods in productions.values():
        for prod in prods:
            terminals.update(set(prod))

    terminals -= non_terminals
    terminals.add('EPSILON')

    # Recursive function to compute First sets
    def compute_first(non_terminal):
        if non_terminal in visited:
            return
        visited.add(non_terminal)

        for production in productions[non_terminal]:
            for symbol in production:
                if symbol in terminals:
                    first_sets[non_terminal].add(symbol)
                elif symbol in non_terminals:
                    compute_first(symbol)
                    if symbol in first_sets:
                        first_sets[non_terminal].update(first_sets[symbol])

                if 'EPSILON' not in first_sets[symbol]:
                    break

                first_sets[non_terminal].update(first_sets[symbol] - {'EPSILON'})

    # Compute First sets for each non-terminal
    for non_terminal in non_terminals:
        compute_first(non_terminal)

    return first_sets

from collections import defaultdict

def compute_follow_sets(grammar, first_sets):
    follow_sets = defaultdict(set)
    visited = set()

    # Extract productions
    productions = defaultdict(list)   
    
    for rule in grammar.strip().split('\n'):
        non_terminal, production = rule.split(':', 1)
        if non_terminal.strip() not in productions:
            productions[non_terminal.strip()] = [p.strip("; ").split() for p in production.split('|')]
        else:
            productions[non_terminal.strip()].extend([p.strip("; ").split() for p in production.split('|')])
  

    # Extract non-terminals
    non_terminals = set()
    for rule in grammar.strip().split('\n'):
        left, _ = rule.split(':', 1)
        non_terminals.add(left.strip())

    # Add EOF to start symbol
    follow_sets['start'].add('EOF')

    # Recursive function to compute Follow sets
    def compute_follow(non_terminal):
        if non_terminal in visited:
            return
        visited.add(non_terminal)

        for rule in grammar.strip().split('\n'):
            left, right = rule.split(':', 1)
            right_productions = [p.strip().split() for p in right.split('|')]
            for production in right_productions:
                if non_terminal in production:
                    index = production.index(non_terminal)
                    rest = production[index + 1:]
                    if not rest:
                        if left != non_terminal:
                            compute_follow(left)
                        follow_sets[non_terminal].update(follow_sets[left])
                    else:
                        first_of_rest = set(rest)
                        if 'EPSILON' in first_of_rest:
                            first_of_rest.remove('EPSILON')
                            follow_sets[non_terminal].update(first_of_rest)
                            compute_follow(left)
                        else:
                            follow_sets[non_terminal].update(first_of_rest)
                    follow_sets[non_terminal].discard('EPSILON')
                    compute_follow(non_terminal)

    # Compute Follow sets for each non-terminal
    for non_terminal in non_terminals:
        compute_follow(non_terminal)

    return follow_sets


def construct_ll1_table(grammar, first_sets, follow_sets):
    ll1_table = defaultdict(dict)

    # Extract productions
    productions = defaultdict(list)
    for rule in grammar.strip().split('\n'):
        non_terminal, production = rule.split(':', 1)
        productions[non_terminal.strip()] = [p.strip().split() for p in production.split('|')]

    # Compute LL(1) parsing table
    for non_terminal, prods in productions.items():
        for prod in prods:
            first_set = first_sets[prod[0]]
            for terminal in first_set:
                if terminal != 'EPSILON':
                    ll1_table[non_terminal][terminal] = prod
            if 'EPSILON' in first_set:
                for terminal in follow_sets[non_terminal]:
                    ll1_table[non_terminal][terminal] = prod

    return ll1_table

# Example usage:
grammar = """
E : E '+' T | T;
T : T '*' F | F;
F : '(' E ')' | 'id';
"""

# Step 1: Eliminate Left Recursion
grammar_no_left_recursion = eliminate_left_recursion(grammar)

# Step 2: Compute FIRST Sets
first_sets = compute_first_sets(grammar_no_left_recursion)

# Step 3: Compute FOLLOW Sets
follow_sets = compute_follow_sets(grammar_no_left_recursion, first_sets)

# Step 4: Construct LL(1) Parsing Table
ll1_table = construct_ll1_table(grammar_no_left_recursion, first_sets, follow_sets)

# Print LL(1) parsing table
for non_terminal, row in ll1_table.items():
    print(non_terminal + ":")
    for terminal, production in row.items():
        print(f"  {terminal}: {' '.join(production)}")