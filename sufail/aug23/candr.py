#start with c and end with r

string = """A computer is a machine that can be programmed to carry out sequences of
 arithmetic or logical operations automatically. Modern computers can perform
 generic sets of operations known as programs. These programs enable computers
 to perform a wide range of tasks. A computer system is a complete computer
 that includes the hardware operating system main software  and peripheral
 equipment needed and used for full operation. This term may also refer 
to a group of computers that are linked and function together"""


print([x for x in(string.split(" ")) if x!="" and x[0]=="c" and x[-1]=="r"])



#print reverse

print([x[::-1] for x in (string.split(" "))])



#print first letter

print({x[0] for x in(string.split(" ")) if x!=""})
