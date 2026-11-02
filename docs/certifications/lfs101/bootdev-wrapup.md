# basic stuff

## notes
`~` is an alias for home directory

**compiled program** ; coded on human versions of machine code, run natively in your pc by using a compiler. due to that, it's pretty fast. low portability. examples are Go, C and Rust
**interpreted program** ; executed by another program first, needs the interpreter. slower cuz it translates then executes every line. high portability. examples are Python, Ruby and JS

    easy analogy: compiler is like translating a book and you read it. interpreter is like someone reading each sentence in their language, then translating it to you.

**shebang:** line at the top of a script that tells your shell which program to use. format: `#! interpreter [optional-arg]`

--- 

## shell

the program that reads your commands.
aka REPLs

i actually use fish but the notes here will be on bash

there's also zsh but i haven't touched it

an sh which bash was based on

they're all POSIX-compliant except for fish (sort of)

---

## commands

you can run multiple commands by separating then with a semicolon `;`
if you want the second only if the first succeed, `&&`

`pwd` printing current working directory
`/home` absolute path
`cd` moving around
`mkdir` create directory
`mv` move and rename stuff
`echo` shell says what u ask

`cp` copy stuff. flags: `-r`
`rm` permanently remove files. flags: `-r`, `-f` force.

`ls` listing the contents of a directory. flags: `-a`, `-r`, `-i` inode, `-l` all info, `t` descending order, `-S` sort by size, `-X` alphabetical, `-1` one file per line

`cat` concatenate. see the contents of files
`head` see the start. flags: `-n` number of lines
`tail` see the end. flags: same

`less` paging through a file. commands: `space` down one page. `b` up one page. `/` search. `q` quit.
`more` worse version of less

`touch` useful to create empty files only when non existent

`grep` search for text in files, case sensitively. flags: `-r` paired with `.` on path
`find` finding stuff by name. be it title or pattern (such as filetype)

i always mix up the syntax of those two

```bash
grep "example" file.txt
find directory -name "example"
```

`which` location of an installed CLI program, such as shell

---

## variables

use $ to access variables.

`PATH` built-in variable on how to execute stuff. check its own section

`env` to see all environment variables currently set

`$HOME` self explanatory
`$?` exit code of the last program you ran

`export` set a variable for this session only
`unset` remove a variable for this session only

---

## flags and arguments

usually - for letter and -- for words.

`-h` or `--help` is self explanatory

you can combine flags.

often a command take multiple arguments, one of them possibly being a flag. the syntax is usually intuitive.

---

## path

$PATH is the variable that guards a list of directions that your shell will look into when you try to run a command.

they probably contain `/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin` but you can add whatever.

remember to add $PATH itself in order to not overwrite the existing path. 

    reminder that the shell runs on RAM so it won't be a permanent change. you'd have to add into your initialization file to get it on every session.

---

## imput and output

`$?` check the exit code of the last program you ran.

`stdout` output. yeah. redirect it with `>`
`stderr` like stdout but for error messages. redirect it with `2>`
`stdin` input. shocking. redirect it with `<`

**piping:** taking the output of a program directly into the input of another program. very useful for automation tasks.

`|` is the pipe operator.
