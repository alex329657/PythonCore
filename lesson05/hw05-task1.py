"""
Task 1: Quipu Calculator
The Quipu is the numbering system of the ancient Incas. A number is represented by knots in a string, using a positional
representation (in base-10).
The representation of 123: one knot + space + two knots + space + three knots
Zeros are represented using a blank space. (leading zeros are not allowed)
@ is a knot and ~ is a space.
123 => @~@@~@@@
20 => @@~~

Create a method that calculates mathematical expressions in quipu format.
Input
A string representing a mathematical expression with operands in the quipu format above, separated by the plus [+] or
minus [-] or division [/] or multiplication [*] sign.
*Hint1: The expression can also include parenthesis to change order of operation.
*Hint2: Between two 0-s you have to put a space, but between a 0 and 1 for example you haven't.
@~@ => 11
@~~@ => 101
@~~~@ => 1001
@ ~     ~ ~     ~ @ => 1001 (!!)
1 space 0 space 0 1

Output
A string representing the result of the mathematical expression in quipu format.
Example:
calculate("@~@@*@@")
=> "@@~@@@@"
calculate("@~@@+@@~~")
=> "@@@~@@"

Tests:
describe("Basic Tests", function(){
   it("It should works for basic tests", function(){
    Test.assertSimilar(calculate("@~@@*@@"), "@@~@@@@")
    Test.assertSimilar(calculate("@~@@+@@~~"), "@@@~@@")
    Test.assertSimilar(calculate("@~~~~@+@~@@"), "@~~~@~@@@")
    Test.assertSimilar(calculate("@~~-@@"), "@@@@@@@@")
    Test.assertSimilar(calculate('@~~*@@/@@@@-@@'), "@@@")
    Test.assertSimilar(calculate("(@~@@+@~@@@)*@~~~~"),  "@@~@@@@@~~~~")
   });  
 });
 """
str = input("Input string: ")


