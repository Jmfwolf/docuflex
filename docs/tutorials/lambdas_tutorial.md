# Using Lambdas in DocuFlex

DocuFlex supports the use of lambdas, which are used to define functions. A lambda declaration begins with the keyword `lambda`, followed by the function name and parameters. The function body is enclosed in curly braces `{}`. In this tutorial, we will cover how to declare and call lambdas in DocuFlex.

## Declaring a Lambda

To declare a lambda, use the `lambda` keyword followed by the function name, parameters in parentheses, and the return type after an arrow `->`. For example:

```
lambda formatTitle(title: String) -> String {
  return title.toUpperCase() + " - DocuFlex"
}
```

This declares a lambda called `formatTitle` that takes a `title` parameter of type `String` and returns a `String`. The function body simply converts the `title` parameter to uppercase and appends " - DocuFlex" to it.

## Calling a Lambda

To call a previously declared lambda, use its name followed by parentheses and any arguments required by the function. For example:

```
introduction.title = formatTitle("Getting Started")
```

This calls the `formatTitle` lambda and passes it the string "Getting Started" as an argument. The return value of the lambda is then assigned to the `introduction.title` variable.

## Lambda Examples

Here are some more examples of lambdas in DocuFlex:

```
lambda multiply(a: Int, b: Int) -> Int {
  return a * b
}

lambda divide(a: Int, b: Int) -> Float {
  return a / b
}

lambda greet(name: String) -> String {
  return "Hello, " + name + "!"
}
```

These lambdas define a function for multiplying two integers, dividing two integers and returning a float, and greeting someone by name respectively.

Here's an example of calling the `multiply` lambda and assigning its result to a variable:

```
@result = multiply(5, 7)
```

This calls the `multiply` lambda with arguments `5` and `7`, and assigns the result `35` to the `result` variable.

## Conclusion

Lambdas are a powerful feature of DocuFlex that allow you to define and call custom functions within your documents. By mastering the use of lambdas, you can create more sophisticated and dynamic documents that can adapt to changing needs and requirements.