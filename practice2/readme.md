# table of contents


1. ex1.py -- how to do print (print "string")
2. ex2.py -- how to do print (print "string")
3. ex3.py -- is how to do run math opration (+, -, :, * )
4. ex4.py -- is how to description and get string from variables

5. ex5.py -- how to do more variables and printing
about to use " (double-quotes) and ' (single-quotes) and
WARNING %s to output words and than %d is to get output number

6. ex6.py -- is how to colaborate the %s, %d, and +
7. ex7.py -- is how to do more printing
example: how to output program is horisontal, but your command is vertical
8. ex8.py -- "print formatter %" is the command  to do a more complicated formatting of a string
example: if your us a " (double-quotes), than you get a output ' (single-quotes)
9. ex9.py --  \ (back slash) is to get vertical output, but the command is horisontal
and """ (triple-quots) is a key to get simple print command

10. ex10.py -- is how to use escape squence
Escape Sequences

This is all of the escape sequences Python supports. You may not use many of these, but memorize their format and what they do anyway. Try them out in some strings to see if you can make them work.

Escape	What it does.
\\	       Backslash                                     (\)
\'	       Single-quote                                  (')
\"	       Double-quote                                  (")
\a	       ASCII bell                                    (BEL)
\b	       ASCII backspace                               (BS)
\f	       ASCII formfeed                                (FF)
\n	       ASCII linefeed                                (LF)
\N{name}	 Character named name in the Unicode database  (Unicode only)
\r	       Carriage Return                               (CR)
\t	       Horizontal Tab                                (TAB)
\uxxxx	   Character with 16-bit hex value xxxx          (u'' string only)
\Uxxxxxxxx Character with 32-bit hex value xxxxxxxx      (u'' string only)
\v	       ASCII vertical tab                            (VT)
\ooo	     Character with octal value ooo
\xhh	     Character with hex value hh


11. ex11.py -- how to get any input strings from person

12. ex12.py -- about raw_input or %r command, %r command is to get input data from person, and than print again in output from print command

13. The argv is the "argument variable," a very standard name in programming, that you will find used in many other languages. argv is the command to get data from name of your file project.

14. ex14.py is combination raw_input and argv
in the example username is as command to run program.

15. reading file with raw_input and argv function.
to runing program you must be writing a litle coding, like this is "$ echo "This is a test file." > test.txt"

16. ex16.py -- how to do reading and writing

17. ex17.py -- echo to make a file, and cat to show the file? You can learn how to do that in Appendix A.

18. ex18.py -- hot to use def function

19. ex19.py -- function and variables

20. ex20.py -- Exercise 20: Functions and Files
   '$ python3 ex20.py test.txt' that is the command to run ex20.py

21. ex21.py -- is a example from return fuction
22. ex24.py -- more practice example,
\t (backslash + t) is a command for tab
\' (backslash + any caracter) is a coomand to add any caracter
\\ (double backslash) is command to add \ (one backslash)
'dev' is pair with 'return'

23. ex25.py -- is how to work with a python modul

24. ex27.py -- Informatic Logic

25. ex28.py -- how to use informatic logic(boolean)

26. ex29.py -- how to use if
you can get output, just when coding on the script answer is 'TRUE'

    Rules for If-Statements
    1. Every if-statement must have an else.
    2. If this else should never run because it doesn't make sense,
       then you must use a die function in the else that prints out an error message and dies,
       just like we did in the last exercise. This will find many errors.
    3. Never nest if-statements more than two deep and always try to do them one deep.
    4. Treat if-statements like paragraphs,
       where each if-elif-else grouping is like a set of sentences.
       Put blank lines before and after.
    5. Your boolean tests should be simple.
       If they are complex,
       move their calculations to variables earlier in your function and use a good name for the variable.

27. ex30.py -- how to use if, elif, and else
over all this exercise is same like exercise 29

28. ex31.py -- how to combination raw_input and if, elif, and else

29. ex32.py -- Loops and Lists

30. ### WARNING IN EXERCISE 37 IS THE SIMBOLS REVIEW!!!
##Rules for Loops
Use a while-loop only to loop forever, and that means probably never. This only applies to Python; other languages are different.
Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.

30. ex33.py -- while loops

31. ex34.py -- List []

32. ex36 -- is how to designing and debugings

33. ex38 -- doing this to list

    ####What Lists Can Do####
Let's say you want to create a computer game based on Go Fish.
If you don't know what Go Fish is, take the time now to go read up on it on the internet.
To do this you would need to have some way of taking the concept of a "deck of cards" and put it into your Python program.
You then have to write Python code that knows how to work this imaginary version of a deck of cards so that a person playing your game thinks that it's real, even if it isn't.
What you need is a "deck of cards" structure, and programmers call this kind of thing a "data structure".

What's a data structure? If you think about it,
a "data structure" is just a formal way to structure (organize) some data (facts).
It really is that simple, even though some data structures can get insanely complex,
all they are is just a way to store facts inside a program so you can access them in different ways.
They structure data.

    #####When to Use Lists#####
You use a list whenever you have something that matches the list data structure's useful features:
1. If you need to maintain order.
   Remember, this is listed order, not sorted order.
    Lists do not sort for you.
2. If you need to access the contents randomly by a number.
   Remember, this is using cardinal numbers starting at 0.
3. If you need to go through the contents linearly (first to last).
   Remember, that's what for-loops are for.

Then that's when you use a list.


31. ex39 -- all about Dictionaries