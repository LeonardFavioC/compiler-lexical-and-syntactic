# Compiler in Python
## use syntactic and lexical analyzer
## Details
- Analyze the sintax in lexical analyzer
- After Syntax LL(1)
- First and Follow Sets  based on the productions
- LL1 parsing Table
- String parsing function which takes string as Input and outputs whether the string is accepted or rejected by the grammar


```Exercise written in python```

```The goal this exercise to validate some strings of an input file, first pass it through the lexical analyzer then through the syntactic.```

### Lexical Analyzer
```accept number, identifiers, and special characters previously defined```

### Syntactic Analyzer
``` First and Follow Sets based of productions```
`Show implementation table`
`Validate the syntax from the output of the lexico analyzer`

### Prerequisites
* python2.7
* panda library

### Rules

**The gramar are saved in grammar(productions)**
**The input values are saved in math.txt**


**For example:**

Case 1:

**INPUT**

`(444444 +  ((a+mod(5,6)) / {   6-(7*pot)8,8)))))`

**OUTPUT:**

`Sintax not accepted`

Case 2:

**INPUT**

`5+      9*x1`

**OUTPUT:**

`Sintax not accepted`
Case 3:

**INPUT**

`pot(56,60  )`

**OUTPUT:**

`Sintax accepted`

## Usage

`Run in python 2.7 or 3 from terminal`

- Locate in folder

- Run

`python syntacticAnalyzer.py`

**By:**
* Caraguay Leonardo
* Quezada Guido
* Zhunaula Jonathan

`Based`
- https://github.com/sid24rane/LL1-parser/blob/
- https://github.com/gqroot/analizadorLexico

