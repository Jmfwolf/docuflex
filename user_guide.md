# DocuFlex Language User Guide

## Introduction

Welcome to the DocuFlex User Guide! This guide will introduce you to the basic components of the DocuFlex language and show you how to use it to create software documentation. We'll cover how to define a class, add properties, use inheritance, and more.

## Commenting in DocuFlex

DocuFlex uses the `// @DocuFlex` prefix to differentiate its comments from regular comments in the source code. This prefix signals the interpreter to parse the following content. For example:

```docuflex
// @DocuFlex
```

## Defining a Class

In DocuFlex, you define a class using the `class` keyword followed by the class name and its properties enclosed in curly brackets `{}`. For example:

```docuflex
// @DocuFlex
class ClassName {
    property1: "Value1";
    property2: "Value2";
}
```

In this example, `ClassName` is the name of your class, and `property1` and `property2` are properties of the class with values "Value1" and "Value2" respectively.

## Inheritance

To create a class that inherits from another class, you use the `extends` keyword followed by the name of the parent class. For example:

```docuflex
// @DocuFlex
class ChildClass extends ParentClass {
    property1: "Value1";
}
```

In this example, `ChildClass` is a new class that inherits all the properties of `ParentClass` and also has an additional property `property1` with a value of "Value1".

## Arrays

To define an array of values, you use square brackets `[]`. For example:

```docuflex
// @DocuFlex
class ClassName {
    property1: ["Value1", "Value2", "Value3"];
}
```

In this example, `property1` is an array that contains the values "Value1", "Value2", and "Value3".

## Objects

To define an object, you use curly brackets `{}`. For example:

```docuflex
// @DocuFlex
class ClassName {
    property1: { subproperty1: "Value1", subproperty2: "Value2" };
}
```

In this example, `property1` is an object that contains the subproperties `subproperty1` and `subproperty2` with values "Value1" and "Value2" respectively.

## Multiline Strings

To define a multiline string, you use triple double quotes `"""`. For example:

```docuflex
// @DocuFlex
class ClassName {
    property1: """
    This is a
    multiline string
    """;
}
```

In this example, `property1` is a multiline string that contains the text "This is a multiline string".

## Conclusion

That's it for the basics of DocuFlex! We've covered how to define a class, use inheritance, define arrays and objects, and use multiline strings. Remember, the key to mastering DocuFlex is practice. So, start creating your documentation and you'll become proficient in no time. Happy documenting!