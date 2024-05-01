class LL1Converter:
    def __init__(self, grammar):
        self.grammar = grammar
        self.ll1_grammar = {}

    def remove_left_recursion(self):
        new_grammar = {}
        for non_terminal, production_rules in self.grammar.items():
            new_non_terminal = non_terminal + "'"
            alpha = []
            beta = []
            for rule in production_rules:
                if rule.startswith(non_terminal):
                    alpha.append(rule[1:] + new_non_terminal)
                else:
                    beta.append(rule + new_non_terminal)
            new_grammar[non_terminal] = [b for b in beta if b]  # Remove empty rules
            new_grammar[new_non_terminal] = [a for a in alpha if a] + ['']  # Add epsilon
        self.grammar = new_grammar

    def factor_common_prefix(self):
        new_grammar = {}
        for non_terminal, production_rules in self.grammar.items():
            common_prefixes = {}
            for rule in production_rules:
                prefix = rule[0]
                if prefix not in common_prefixes:
                    common_prefixes[prefix] = []
                common_prefixes[prefix].append(rule)
            new_production_rules = []
            for prefix, rules in common_prefixes.items():
                if len(rules) > 1:
                    common_rule = prefix + '|'.join(rule[1:] for rule in rules)
                else:
                    common_rule = rules[0]
                new_production_rules.append(common_rule)
            new_grammar[non_terminal] = new_production_rules
        self.grammar = new_grammar

    def construct_parsing_table(self):
        parsing_table = {}
        for non_terminal, production_rules in self.grammar.items():
            for rule in production_rules:
                first_set = self.first(rule)
                for terminal in first_set:
                    if terminal != '':
                        if non_terminal not in parsing_table:
                            parsing_table[non_terminal] = {}
                        parsing_table[non_terminal][terminal] = rule
        self.parsing_table = parsing_table

    def first(self, symbol):
        if symbol in self.grammar:
            first_set = set()
            for rule in self.grammar[symbol]:
                first_set |= self.first(rule[0])
            return first_set
        else:
            return {symbol}

    def convert_to_ll1(self):
        self.remove_left_recursion()
        self.factor_common_prefix()
        self.construct_parsing_table()

    def print_ll1_grammar(self):
        for non_terminal, production_rules in self.grammar.items():
            print(non_terminal, '->', ' | '.join(production_rules))


# Example usage
if __name__ == "__main__":
    grammar = {
        'S': ['if E then S else S', 'if E then S', 'id := E'],
        'E': ['E + T', 'T'],
        'T': ['T * F', 'F'],
        'F': ['(E)', 'id']
    }

    converter = LL1Converter(grammar)
    converter.convert_to_ll1()
    converter.print_ll1_grammar()
