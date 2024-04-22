# Generated from /media/asa/New Volume/Uni/7/Compiler/HW3/ST_Exercise/STGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from gen.STGrammarParser import STGrammarParser
else:
    from gen.STGrammarParser import STGrammarParser

import sqlite3

class symbol():
    def __init__(self, id, name, type, address, value):
        self.id = id
        self.name = name
        self.type = type
        self.address = address
        self.value = value
# This class defines a complete listener for a parse tree produced by STGrammarParser.
class MySTGrammarListener(ParseTreeListener):

    def __init__(self):
        self.symbol_table = {}
        self.connection = sqlite3.connect("Symbols.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS symbol (
                            id integer, 
                            name TEXT, 
                            type TEXT, 
                            address integer, 
                            value TEXT
                            )""")
        self.connection.commit()

    # Exit a parse tree produced by STGrammarParser#start.
    def exitStart(self, ctx:STGrammarParser.StartContext):
        pass

    # Exit a parse tree produced by STGrammarParser#assigns.
    def exitAssigns(self, ctx:STGrammarParser.AssignsContext):
        self.cursor.execute("SELECT * FROM symbol")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)
        self.connection.close()

    # Exit a parse tree produced by STGrammarParser#assign.
    def exitAssign(self, ctx:STGrammarParser.AssignContext):
        identifier = ctx.getChild(0).getText()
        result = ctx.getChild(2)
        if identifier not in self.symbol_table:
            self.symbol_table[identifier] = symbol(None, identifier, None, id(identifier),0)
        self.symbol_table[identifier].type = result.rule_type
        self.symbol_table[identifier].value = result.value
        self.cursor.execute("SELECT COUNT(*) FROM symbol")
        num = self.cursor.fetchall()[0][0]
        self.symbol_table[identifier].id = int(num)
        self.cursor.execute("SELECT * FROM symbol WHERE name = '{}' LIMIT 1".format(identifier))
        items = self.cursor.fetchall()
        if (len(items) == 0):
            try:
                # Executing the SQL command and commit
                _id = self.symbol_table[identifier].id
                name = self.symbol_table[identifier].name
                type = self.symbol_table[identifier].type
                address = self.symbol_table[identifier].address
                value = str(self.symbol_table[identifier].value)
                params = (_id, name, type, address, value)
                self.cursor.execute(f"INSERT INTO symbol VALUES (?, ?, ?, ?, ?)", params)
                self.connection.commit()
                print("Data inserted")

            except:
                # Rolling back in case of error
                pass
        else:
            self.cursor.execute(f"UPDATE symbol SET value = ?, type =  ? WHERE name = ?", (str(self.symbol_table[identifier].value), self.symbol_table[identifier].type, self.symbol_table[identifier].name))
            self.connection.commit()


    # Exit a parse tree produced by STGrammarParser#expr.
    def exitExpr(self, ctx:STGrammarParser.ExprContext):
        if ctx.getChildCount() == 1:
            ctx.value = ctx.getChild(0).value
            ctx.rule_type = ctx.getChild(0).rule_type
        else:
            op = ctx.getChild(1).getText()
            if op == '+':
                left_child_type = ctx.getChild(0).rule_type
                right_child_type = ctx.getChild(2).rule_type
                if left_child_type == "String":
                    if right_child_type in ["Integer", "Float"]:
                        ctx.rule_type = "String"
                        ctx.value = ctx.getChild(0).value + str(ctx.getChild(2).value)
                elif left_child_type in ["Integer", "Float"]:
                    if left_child_type == "Integer" and right_child_type == "Integer":
                        ctx.rule_type = "Integer"
                        ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
                    else:
                        match right_child_type:
                            case "Integer" | "Float":
                                ctx.rule_type = "Float"
                                ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
                            case "String":
                                ctx.rule_type = "Error"
                                ctx.value = ""
                else:
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value + ctx.getChild(2).value
            else:
                left_child_type = ctx.getChild(0).rule_type
                right_child_type = ctx.getChild(2).rule_type
                if left_child_type == "String" or right_child_type == "String":
                    ctx.rule_type = "Error"
                    ctx.value = ""
                elif left_child_type in ["Integer", "Float"]:
                    if left_child_type == "Integer" and right_child_type == "Integer":
                        ctx.rule_type = "Integer"
                        ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
                    else:
                        ctx.rule_type = "Float"
                        ctx.value = ctx.getChild(0).value - ctx.getChild(2).value
                else:
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value - ctx.getChild(2).value

    # Exit a parse tree produced by STGrammarParser#term.
    def exitTerm(self, ctx:STGrammarParser.TermContext):
        if ctx.getChildCount() == 1:
            ctx.value = ctx.getChild(0).value
            ctx.rule_type = ctx.getChild(0).rule_type
        else:
            op = ctx.getChild(1).getText()
            if op == '*':
                left_child_type = ctx.getChild(0).rule_type
                right_child_type = ctx.getChild(2).rule_type
                if left_child_type == "String" or right_child_type == "String":
                    ctx.value = ""
                    ctx.rule_type = "Error"
                else:
                    if left_child_type == "Integer" and right_child_type == "Integer":
                        ctx.rule_type = "Integer"
                    else:
                        ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value * ctx.getChild(2).value
            else:
                left_child_type = ctx.getChild(0).rule_type
                right_child_type = ctx.getChild(2).rule_type
                if left_child_type == "String" or right_child_type == "String":
                    ctx.value = ""
                    ctx.rule_type = "Error"
                else:
                    ctx.rule_type = "Float"
                    ctx.value = ctx.getChild(0).value / ctx.getChild(2).value

    # Exit a parse tree produced by STGrammarParser#factor_is_string.
    def exitFactor_is_string(self, ctx:STGrammarParser.Factor_is_stringContext):
        ctx.rule_type = "String"
        ctx.value = ctx.getText()
    # Exit a parse tree produced by STGrammarParser#factor_is_integer.

    def exitFactor_is_integer(self, ctx:STGrammarParser.Factor_is_integerContext):
        ctx.rule_type = "Integer"
        ctx.value = int(ctx.getText())

    # Exit a parse tree produced by STGrammarParser#factor_is_float.

    def exitFactor_is_float(self, ctx:STGrammarParser.Factor_is_floatContext):
        ctx.rule_type = "Float"
        ctx.value = float(ctx.getText())

    # Exit a parse tree produced by STGrammarParser#factor_is_expression.

    def exitFactor_is_expression(self, ctx:STGrammarParser.Factor_is_expressionContext):
        ctx.rule_type = ctx.getChild(1).rule_type
        ctx.value = ctx.getChild(1).value


    # Exit a parse tree produced by STGrammarParser#factor_is_id.
    def exitFactor_is_id(self, ctx:STGrammarParser.Factor_is_idContext):
        identifier = ctx.getText()
        self.cursor.execute("SELECT * FROM symbol WHERE name = '{}' LIMIT 1".format(identifier))
        items = self.cursor.fetchall()
        if len(items) != 0:
            ctx.rule_type = items[0][2]
            match ctx.rule_type:
                case "Integer":
                    ctx.value = int(items[0][4])
                case "Float":
                    ctx.value = float(items[0][4])
                case _:
                    ctx.value = items[0][4]

        else:
            ctx.rule_type = "ERROR"
            ctx.value = ""

    # Exit a parse tree produced by STGrammarParser#sign.
    def exitSign(self, ctx:STGrammarParser.SignContext):
        ctx.value = ctx.getText()



del STGrammarParser