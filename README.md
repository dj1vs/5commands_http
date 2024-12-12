# 5command_http

Interpreter for 5command esoteric language, wrapped into an HTTP API.

## 5command

> 5command is an esoteric programming language created by User:Icepy in 2014. 5command has a very small command set of only 5 commands. 5command is a tape based language which has an infinite amount of slots. It has a debug mode that can be set to true or false in a interpreter. debug mode is automatically false. Also, anything that is not valid syntax, is a comment. 5command was built to print out very large numbers, in a small amount of time and space. 

### Commands

```
+  move the pointer right on the tape
-  move the pointer left on the tape
^  increment where the pointer is pointing at
v  decrement where the pointer is pointing at
*  print out the number at the pointer (without a space)
```

## HTTP API

Receives `5command` code via `/interpret` handle.

Receives raw code via request body and responds with raw string, which corresponds to programms stdout.