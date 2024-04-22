grammar ArithmeticExpression;

start: assigns  EOF;
assigns: assign NEWLINE assigns | assign;
assign: ID '=' expr;
expr:  expr (ADD | SUB) term | term| ('+'| '-')term;
term:  term (MUL| DIV) factor | factor;
factor: number | LPAREN expr RPAREN| STRING | ID ;
number : sign NUMERICALVALUE;
sign : ('+'| '-')* ;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
NUMERICALVALUE: FLOAT | INTEGER;
fragment FLOAT:[0-9]*'.'[0-9]*;
fragment INTEGER:[0-9]+;
STRING: '"'.*?'"';
WS: [ \t\r]+ -> skip;
NEWLINE : '\n';
ID : [a-z,A-Z]([a-z,A-Z] | [0-9])*;
