grammar VYP;

test: 'hello world' ID;
ID: [a-z]+;
WS: [ \t\r\n]+ -> skip;
