
# EmoCC

## Overview

Have you ever found programming in C so boring that you wished you could
just code using emojis instead? Well, you're in luck! With Emo-C, you
can write entire programs using exclusively emojis! For example, here is
a "Hello World" program that prints out the characters `👋🌎`:

```
💷💼👉🍎↕🐵👈⏭💷💼👉🍎📚🐵👈⏭🔢🌌🏠🌜🔢🌌😛⏸🔤✖😜🤜🤛🌛👎🌜💔🌛😛🛑🌜💔🌛😜🛑🖨🌜📤⏸💬👋🌎💬🌛🛑🚗🌌✅🛑👍

```

Just simply throw any Emo-C program into the `emocc` compiler and you'll
get a working executable!

## How to Use

`emocc` works just like `gcc`, except that you may only compile one Emo-C
source file at a time and that file must be the first argument. Otherwise,
all `gcc` flags are supported. For example, `hello_world.emoc` can be compiled
as follows:

```
emocc hello_world.emoc -o hello_world
```

### Dependencies

Two dependencies are necessary for EmoCC to work:

 * A `gcc` compiler that works with Emojis.
 * Python 3 or later.

## Language Specification

The Emo-C language is specified as a mapping between emoji characters and
C keywords/symbols because it literally just compiles down to C.

The following table shows which C keyword or symbol corresponds to which
Emo-C character. Any characters in an Emo-C program *not* in the table below
will remain unaltered when compiling down to C.

| C Keyword or Symbol | Emo-C Character | Unicode Hex Value  |
|---------------------|-----------------|--------------------|
| `#`                 | 💷               | U+1F4B7            |
| `include`           | 💼               | U+1F4BC            |
| (space character)   | 🌌               | U+1F30C            |
| `std`               | 🍎               | U+1F34E            |
| `<`                 | 👉               | U+1F449            |
| `>`                 | 👈               | U+1F448            |
| `io`                | ↕               | U+2195             |
| `.h`                | 🐵               | U+1F435            |
| (newline character) | ⏭               | U+23ED             |
| `lib`               | 📚               | U+1F4DA            |
| `int`               | 🔢               | U+1F522            |
| `main`              | 🏠               | U+1F3E0            |
| `(`                 | 🌜               | U+1F31C            |
| `)`                 | 🌛               | U+1F31B            |
| `{`                 | 👎               | U+1F44E            |
| `}`                 | 👍               | U+1F44D            |
| `[`                 | 🤜               | U+1F91C            |
| `]`                 | 🤛               | U+1F91B            |
| `char`              | 🔤               | U+1F524            |
| `define`            | 🏷               | U+1F3F7            |
| `void`              | 💔               | U+1F494            |
| `fprintf`           | 🖨               | U+1F5A8            |
| `stdin`             | 📥               | U+1F4E5            |
| `stdout`            | 📤               | U+1F4E4            |
| `stderr`            | 🚫               | U+1F6AB            |
| `"`                 | 💬               | U+1F4AC            |
| `'`                 | 💭               | U+1F4AD            |
| `return`            | 🚗               | U+1F697            |
| `0`                 | 0️⃣               | U+30 U+FE0F U+20E3 |
| `1`                 | 1️⃣               | U+31 U+FE0F U+20E3 |
| `2`                 | 2️⃣               | U+32 U+FE0F U+20E3 |
| `3`                 | 3️⃣               | U+33 U+FE0F U+20E3 |
| `4`                 | 4️⃣               | U+34 U+FE0F U+20E3 |
| `5`                 | 5️⃣               | U+35 U+FE0F U+20E3 |
| `6`                 | 6️⃣               | U+36 U+FE0F U+20E3 |
| `7`                 | 7️⃣               | U+37 U+FE0F U+20E3 |
| `8`                 | 8️⃣               | U+38 U+FE0F U+20E3 |
| `9`                 | 9️⃣               | U+39 U+FE0F U+20E3 |
| `;`                 | 🛑               | U+1F6D1            |
| `+`                 | ➕               | U+2795             |
| `-`                 | ➖               | U+2796             |
| `*`                 | ✖               | U+2716             |
| `/`                 | ➗               | U+2797             |
| `float`             | 🚢               | U+1F6A2            |
| `double`            | 💑               | U+1F491            |
| `exit`              | ⚰               | U+26B0             |
| `EXIT_SUCCESS`      | ✅               | U+2705             |
| `EXIT_FAILURE`      | ❌               | U+274C             |
| `=`                 | ↔               | U+2194             |
| `while`             | 🔄               | U+1F504            |
| `for`               | 🍀               | U+1F340            |
| `if`                | 🛂               | U+1F6C2            |
| `switch`            | 📻               | U+1F4FB            |
| `case`              | 🎵               | U+1F3B5            |
| `default`           | 🎶               | U+1F3B6            |
| `:`                 | 🔘               | U+1F518            |
| `struct`            | 🏰               | U+1F3F0            |
| `union`             | 🔳               | U+1F533            |
| `malloc`            | 🆕               | U+1F195            |
| `free`              | 🆓               | U+1F193            |
| `sizeof`            | ℹ               | U+2139             |
| `enum`              | 📛               | U+1F4DB            |
| `inline`            | ⏯               | U+23EF             |
| `static`            | ⚡               | U+26A1             |
| `signed`            | 📝               | U+1F4DD            |
| `unsigned`          | 📄               | U+1F4C4            |
| `long`              | ⛓               | U+26D3             |
| `u`                 | 🤟               | U+1F91F            |
| `typedef`           | 🏁               | U+1F3C1            |
| `_t`                | 🚩               | U+1F6A9            |
| `,`                 | ⏸               | U+23F8             |

By convention, all "face" emojis are reserved for variable names and thus
did not appear in the table above. To ensure that your Emo-C programs remain
compatible with future updates (where I may add new rows to this table),
stick with using face emojis for any variable, type, etc. that you name
yourself.

### Limitations

Is every possible C construct accounted for in the above language specification?
Definitely not! But I hope this is a good start. If the provided specification
does not fully support your needs, you can always add new entries to
`emo_to_c.json`. I may add new entries there from time to time.

If you think an important C feature is missing and would like to contribute
to this project, please feel free to do so! If you need GitHub permissions
to make a contribution or otherwise have questions, contact me at 
[radang2014REMOVEME@gmail.com](mailto:radang2014REMOVEME@gmail.com), with
characters removed as indicated.

### String Literals

Any group of characters between two `💬`
characters are treated as a string literal. All characters within a string
literal will be unaltered when compiled down to C, even characters that would
otherwise map to C keywords or symbols (the escape character being the only
exception).

The escape character `⛔` can be used to put a
`💬` character or a
`⛔` character within a string. Use
`⛔💬` to
specify a `💬` within a string and use
`⛔⛔` to
specify a `⛔` within a string. Any
`⛔` within a string that is followed by
neither a `💬` character nor
`⛔` character is syntactically invalid and
will result in a compiler error.

You can think of the `⛔` character as
analogous to the `\` character and the `💬`
character as analogous to the `"` character in many other contexts.

