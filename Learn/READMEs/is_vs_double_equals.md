There is a simple rule of thumb to tell you when to use == or is.

"==" is for value equality. Use it when you would like to know if two objects have the same value.
"is" is for reference equality. Use it when you would like to know if two references refer to the same object.

if something is None:
is None is a bit (~50%) faster than == None 
