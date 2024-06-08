grammar AssignmentStatement;

start returns [value_attr = str(), type_attr = str()]:
      prog NEWLINE* EOF ;
prog returns [value_attr = str(), type_attr = str()]:
      'program' ID NEWLINE* (declaration)* NEWLINE+ compoundst;
declaration returns [value_attr = str(), type_attr = str()]:
      'var' NEWLINE* (variable_declaration NEWLINE*)+ ;
variable_declaration returns [value_attr = str(), type_attr = str()]:
       ID(','ID)* ':' type ;
type returns [value_attr = str(), type_attr = str()]:
      'float' | 'int' | 'string';
compoundst  returns [value_attr = str(), type_attr = str()]:
      'begin' NEWLINE* (statement NEWLINE+)+ 'end' ;
statement  returns [value_attr = str(), type_attr = str()]:
      ifst | assign | compoundst | forst | whilest | casest|compoundtrn ;
ifst  returns [value_attr = str(), type_attr = str()]:
      'if' cond 'then' NEWLINE* statement NEWLINE*
       ('else' NEWLINE* statement)? ;
whilest returns [value_attr = str(), type_attr = str()]:
        'while' cond 'do' NEWLINE*  statement;
forst returns [value_attr = str(), type_attr = str()]:
        'for'  assign 'to' number 'do' NEWLINE* compoundst;
casest  returns [value_attr = str(), type_attr = str()]:
        'Case'  ID  'of' NEWLINE casebody 'end' ;
casebody returns [value_attr = str(), type_attr = str()]:
       (ID(','ID)* ':' (term|String) NEWLINE)+;
cond  returns [value_attr = str(), type_attr = str()]:
      expr RELOP expr ;
simpletrn returns [value_attr = str(), type_attr = str()]:
        cond '?' trnbody ;
trnbody returns [value_attr = str(), type_attr = str()]:
        (expr|simpletrn)':' (simpletrn|expr) ;
compoundtrn returns [value_attr = str(), type_attr = str()]:
        ID ':=' simpletrn ;
assign returns [value_attr = str(), type_attr = str()]:
        ID ':=' expr ;
//        ID(','ID)* ':=' term ;
expr returns [value_attr = str(), type_attr = str()]:
     expr '+' term        #expr_term_plus
    | expr '-' term      #expr_term_minus
    | expr RELOP term    #expr_term_relop
    | term               #term4
    ;

term returns [value_attr = str(), type_attr = str()]:
    term '*' factor      #term_fact_mutiply
    | term '/' factor    #term_fact_divide
    | factor             #factor3
    ;

factor returns [value_attr = str(), type_attr = str()]:
    '(' expr ')'      #fact_expr
    | ID              #fact_id
    | number          #fact_number
    | String          #fact_string
    | array           #fact_array
    ;

number returns [value_attr = str(), type_attr = str()]:
    FLOAT             #number_float
    | INT             #number_int
    ;

array returns [value_attr = str(), type_attr = str()]:
    INT_ARRAY        #array_int
    | FLOAT_ARRAY    #array_float
    | STRING_ARRAY   #array_string
    ;


/* Lexical Rules */
INT     : DIGIT+ ;

FLOAT:
    DIGIT+ '.' DIGIT*
    | '.' DIGIT+ ;

String:
        '"' (ESC|.)*? '"' ;
ID:
    LETTER(LETTER|DIGIT)* ;

ARRAY_TYPE:
    ID '[' INT ']';

INT_ARRAY:
    '[' INT (',' INT)* ']';

FLOAT_ARRAY:
    '[' FLOAT (',' FLOAT)* ']';

STRING_ARRAY:
    '[' String (',' String)* ']';


fragment
        DIGIT: [0-9] ;
fragment
        LETTER: [a-zA-Z] ;
fragment
        ESC: '\\"' | '\\\\' ;


WS: [ \t\r]+ -> skip ;
NEWLINE: '\n' | '\r\n';
RELOP: '<=' | '<' | '>'|'>='| '&&'|'||'| '==' | '!=' ;

LINE_COMMENT
    :   '#' ~[\r\n]* -> channel(HIDDEN)
    ;