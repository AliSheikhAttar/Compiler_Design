grammar ArithmeticExpression;

start: function_definitions? assigns? EOF;

function_definitions: function_definition (NEWLINE+ function_definition)* NEWLINE*;

function_definition: 'string' ID '(' parameter_list ')' NEWLINE 'begin' NEWLINE assigns NEWLINE return_statement NEWLINE 'end';

parameter_list: parameter (',' parameter)* | ;
parameter: type ID;

type: 'int' | 'float' | 'string';

assigns: assign (NEWLINE* assign)* NEWLINE*;

assign: id '=' expr;

return_statement: 'return' expr;

id: ID;

expr: expr ADD expr
    | expr SUB expr
    | term
    | function_call
    ;

term: term MUL term
    | term DIV term
    | factor
    ;

factor: sign? NUMERICALVALUE #factor_is_numeric
      | LPAREN expr RPAREN #factor_is_expression
      | ID #factor_is_id
      | STRING #factor_is_string
      ;

function_call: ID '(' argument_list ')';

argument_list: expr (',' expr)* | ;  // Allow empty argument list

sign: ('+'|'-');

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
NUMERICALVALUE: FLOAT | INTEGER;
STRING: '"' .*? '"';
fragment FLOAT: [0-9]* '.' [0-9]+;
fragment INTEGER: [0-9]+;
WS: [ \t\r]+ -> skip;
NEWLINE: '\n';
ID: [a-zA-Z]([a-zA-Z0-9])*;
