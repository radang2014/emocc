
# EmoCC

## Overview

Have you ever found programming in C so boring that you wished you could
just code using emojis instead? Well, you're in luck! With Emo-C, you
can write entire programs using exclusively emojis! For example, here is
a program that prints out the string "Hello world!":

```
💷💼👉🍎↕🐵👈⏭💷💼👉🍎📚🐵👈⏭🔢🌌🏠🌜🔢🌌😛⏸🔤✖😜🤜🤛🌛👎🌜💔🌛😛🛑🌜💔🌛😜🛑🖨🌜📤⏸💬⛔🏠⛔🍆⛔🍭⛔🍭⛔🍢⛔🌌⛔🍷⛔🍢⛔🍚⛔🍭⛔🍩⛔❗⛔💫⛔🌰💬🌛🛑🚗🌌✅🛑👍

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

Three dependencies are necessary for EmoCC to work:

 * A `gcc` compiler that works with Emojis.
 * Python 3 or later.
 * A `bash` shell.

## Language Specification

The Emo-C language is specified as a mapping between emoji characters and
C keywords/symbols because it literally just compiles down to C.

The following table shows which C keyword or symbol corresponds to which
Emo-C character. Any characters in an Emo-C program *not* in the table below
will remain unaltered when compiling down to C.

| C Keyword or Symbol | Emo-C Character | Unicode Hex Value  |
|---------------------|-----------------|--------------------|
| ``#``               | 💷               | U+1F4B7            |
| ``include``         | 💼               | U+1F4BC            |
| (space character)   | 🌌               | U+1F30C            |
| ``std``             | 🍎               | U+1F34E            |
| ``<``               | 👉               | U+1F449            |
| ``>``               | 👈               | U+1F448            |
| ``io``              | ↕               | U+2195             |
| ``.h``              | 🐵               | U+1F435            |
| (newline character) | ⏭               | U+23ED             |
| ``lib``             | 📚               | U+1F4DA            |
| ``int``             | 🔢               | U+1F522            |
| ``main``            | 🏠               | U+1F3E0            |
| ``(``               | 🌜               | U+1F31C            |
| ``)``               | 🌛               | U+1F31B            |
| ``{``               | 👎               | U+1F44E            |
| ``}``               | 👍               | U+1F44D            |
| ``[``               | 🤜               | U+1F91C            |
| ``]``               | 🤛               | U+1F91B            |
| ``char``            | 🔤               | U+1F524            |
| ``define``          | 🏷               | U+1F3F7            |
| ``void``            | 💔               | U+1F494            |
| ``fprintf``         | 🖨               | U+1F5A8            |
| ``stdin``           | 📥               | U+1F4E5            |
| ``stdout``          | 📤               | U+1F4E4            |
| ``stderr``          | 🚫               | U+1F6AB            |
| ``"``               | 💬               | U+1F4AC            |
| ``'``               | 💭               | U+1F4AD            |
| ``return``          | 🚗               | U+1F697            |
| ``0``               | 0️⃣               | U+30 U+FE0F U+20E3 |
| ``1``               | 1️⃣               | U+31 U+FE0F U+20E3 |
| ``2``               | 2️⃣               | U+32 U+FE0F U+20E3 |
| ``3``               | 3️⃣               | U+33 U+FE0F U+20E3 |
| ``4``               | 4️⃣               | U+34 U+FE0F U+20E3 |
| ``5``               | 5️⃣               | U+35 U+FE0F U+20E3 |
| ``6``               | 6️⃣               | U+36 U+FE0F U+20E3 |
| ``7``               | 7️⃣               | U+37 U+FE0F U+20E3 |
| ``8``               | 8️⃣               | U+38 U+FE0F U+20E3 |
| ``9``               | 9️⃣               | U+39 U+FE0F U+20E3 |
| ``;``               | 🛑               | U+1F6D1            |
| ``+``               | ➕               | U+2795             |
| ``-``               | ➖               | U+2796             |
| ``*``               | ✖               | U+2716             |
| ``/``               | ➗               | U+2797             |
| ``float``           | 🚢               | U+1F6A2            |
| ``double``          | 💑               | U+1F491            |
| ``exit``            | ⚰               | U+26B0             |
| ``EXIT_SUCCESS``    | ✅               | U+2705             |
| ``EXIT_FAILURE``    | ❌               | U+274C             |
| ``=``               | ↔               | U+2194             |
| ``while``           | 🔄               | U+1F504            |
| ``for``             | 🍀               | U+1F340            |
| ``if``              | 🛂               | U+1F6C2            |
| ``switch``          | 📻               | U+1F4FB            |
| ``case``            | 🎵               | U+1F3B5            |
| ``default``         | 🎶               | U+1F3B6            |
| ``:``               | 🔘               | U+1F518            |
| ``struct``          | 🏰               | U+1F3F0            |
| ``union``           | 🔳               | U+1F533            |
| ``malloc``          | 🆕               | U+1F195            |
| ``free``            | 🆓               | U+1F193            |
| ``sizeof``          | ℹ               | U+2139             |
| ``enum``            | 📛               | U+1F4DB            |
| ``inline``          | ⏯               | U+23EF             |
| ``static``          | ⚡               | U+26A1             |
| ``signed``          | 📝               | U+1F4DD            |
| ``unsigned``        | 📄               | U+1F4C4            |
| ``long``            | ⛓               | U+26D3             |
| ``u``               | 🤟               | U+1F91F            |
| ``typedef``         | 🏁               | U+1F3C1            |
| ``_t``              | 🚩               | U+1F6A9            |
| ``,``               | ⏸               | U+23F8             |
| ``&``               | ⚔               | U+2694             |
| ``\|``              | 🗡               | U+1F5E1            |
| ``~``               | 🔴               | U+1F534            |
| ``!``               | ❗               | U+2757             |
| ``else``            | 🛄               | U+1F6C4            |
| ``fgetc``           | 📷               | U+1F4F7            |
| ``fgets``           | 📸               | U+1F4F8            |
| ``fscanf``          | 🎥               | U+1F3A5            |
| ``sscanf``          | 🎞               | U+1F39E            |
| ``0x``              | ✡               | U+2721             |
| ``EOF``             | 🔚               | U+1F51A            |
| ``FILE``            | 🗂               | U+1F5C2            |
| ``fopen``           | 📂               | U+1F4C2            |
| ``fclose``          | 📁               | U+1F4C1            |

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

### String and Character Literals

Any group of characters between two `💬`
characters are treated as a string literal. Any group of characters between
two `💭` characters are treated as a
character literal. All characters within a string or character literal will
be unaltered when compiled down to C, even characters that would otherwise
map to C keywords or symbols (the escape character being the only exception).

Escape sequences always begin with the escape character
`⛔` and can be used to put a
`💬` character, a
`💭` character, or a
`⛔` character within a string or character
literal. They can also be used as an alternative way to specify normal,
typeable characters within strings without having to type non-emoji characters.
See the following table for the mapping between escape sequences and characters.

| Emo-C Escape Sequence | Unicode Hex Value (not including escape character) | C character       |
|-----------------------|----------------------------------------------------|-------------------|
| ⛔⛔                    | U+26D4                                             | ``⛔``             |
| ⛔💬                    | U+1F4AC                                            | ``💬``             |
| ⛔💭                    | U+1F4AD                                            | ``💭``             |
| ⛔0️⃣                    | U+30 U+FE0F U+20E3                                 | ``0``             |
| ⛔1️⃣                    | U+31 U+FE0F U+20E3                                 | ``1``             |
| ⛔2️⃣                    | U+32 U+FE0F U+20E3                                 | ``2``             |
| ⛔3️⃣                    | U+33 U+FE0F U+20E3                                 | ``3``             |
| ⛔4️⃣                    | U+34 U+FE0F U+20E3                                 | ``4``             |
| ⛔5️⃣                    | U+35 U+FE0F U+20E3                                 | ``5``             |
| ⛔6️⃣                    | U+36 U+FE0F U+20E3                                 | ``6``             |
| ⛔7️⃣                    | U+37 U+FE0F U+20E3                                 | ``7``             |
| ⛔8️⃣                    | U+38 U+FE0F U+20E3                                 | ``8``             |
| ⛔9️⃣                    | U+39 U+FE0F U+20E3                                 | ``9``             |
| ⛔🍏                    | U+1F34F                                            | ``A``             |
| ⛔🍎                    | U+1F34E                                            | ``a``             |
| ⛔🐻                    | U+1F43B                                            | ``B``             |
| ⛔🍌                    | U+1F34C                                            | ``b``             |
| ⛔😺                    | U+1F63A                                            | ``C``             |
| ⛔🥐                    | U+1F950                                            | ``c``             |
| ⛔⬇                    | U+2B07                                             | ``D``             |
| ⛔🍩                    | U+1F369                                            | ``d``             |
| ⛔⚡                    | U+26A1                                             | ``E``             |
| ⛔🍆                    | U+1F346                                            | ``e``             |
| ⛔🌫                    | U+1F32B                                            | ``F``             |
| ⛔🍟                    | U+1F35F                                            | ``f``             |
| ⛔👻                    | U+1F47B                                            | ``G``             |
| ⛔🍇                    | U+1F347                                            | ``g``             |
| ⛔🏠                    | U+1F3E0                                            | ``H``             |
| ⛔🌭                    | U+1F32D                                            | ``h``             |
| ⛔🆔                    | U+1F194                                            | ``I``             |
| ⛔🍦                    | U+1F366                                            | ``i``             |
| ⛔🗾                    | U+1F5FE                                            | ``J``             |
| ⛔🍬                    | U+1F36C                                            | ``j``             |
| ⛔🐨                    | U+1F428                                            | ``K``             |
| ⛔🥝                    | U+1F95D                                            | ``k``             |
| ⛔💌                    | U+1F48C                                            | ``L``             |
| ⛔🍭                    | U+1F36D                                            | ``l``             |
| ⛔👨                    | U+1F468                                            | ``M``             |
| ⛔🥩                    | U+1F969                                            | ``m``             |
| ⛔📰                    | U+1F4F0                                            | ``N``             |
| ⛔🌰                    | U+1F330                                            | ``n``             |
| ⛔🐙                    | U+1F419                                            | ``O``             |
| ⛔🍢                    | U+1F362                                            | ``o``             |
| ⛔🖨                    | U+1F5A8                                            | ``P``             |
| ⛔🍕                    | U+1F355                                            | ``p``             |
| ⛔🦟                    | U+1F99F                                            | ``Q``             |
| ⛔🍮                    | U+1F36E                                            | ``q``             |
| ⛔📻                    | U+1F4FB                                            | ``R``             |
| ⛔🍚                    | U+1F35A                                            | ``r``             |
| ⛔🥪                    | U+1F96A                                            | ``S``             |
| ⛔🍣                    | U+1F363                                            | ``s``             |
| ⛔📺                    | U+1F4FA                                            | ``T``             |
| ⛔🌮                    | U+1F32E                                            | ``t``             |
| ⛔☂                    | U+2602                                             | ``U``             |
| ⛔🥡                    | U+1F961                                            | ``u``             |
| ⛔🎮                    | U+1F3AE                                            | ``V``             |
| ⛔🥨                    | U+1F968                                            | ``v``             |
| ⛔👩                    | U+1F469                                            | ``W``             |
| ⛔🍷                    | U+1F377                                            | ``w``             |
| ⛔❌                    | U+274C                                             | ``X``             |
| ⛔🍱                    | U+1F371                                            | ``x``             |
| ⛔🧶                    | U+1F9F6                                            | ``Y``             |
| ⛔🍋                    | U+1F34B                                            | ``y``             |
| ⛔🦓                    | U+1F993                                            | ``Z``             |
| ⛔🥓                    | U+1F953                                            | ``z``             |
| ⛔❗                    | U+2757                                             | ``!``             |
| ⛔❓                    | U+2753                                             | ``?``             |
| ⛔➕                    | U+2795                                             | ``+``             |
| ⛔➖                    | U+2796                                             | ``-``             |
| ⛔✖                    | U+2716                                             | ``*``             |
| ⛔➗                    | U+2797                                             | ``/``             |
| ⛔💷                    | U+1F4B7                                            | ``#``             |
| ⛔↔                    | U+2194                                             | ``=``             |
| ⛔💲                    | U+1F4B2                                            | ``$``             |
| ⛔🥕                    | U+1F955                                            | ``^``             |
| ⛔🌜                    | U+1F31C                                            | ``(``             |
| ⛔🌛                    | U+1F31B                                            | ``)``             |
| ⛔🤜                    | U+1F91C                                            | ``[``             |
| ⛔🤛                    | U+1F91B                                            | ``]``             |
| ⛔👎                    | U+1F44E                                            | ``{``             |
| ⛔👍                    | U+1F44D                                            | ``}``             |
| ⛔🌌                    | U+1F30C                                            | (space character) |
| ⛔🔘                    | U+1F518                                            | ``:``             |
| ⛔🛑                    | U+1F6D1                                            | ``;``             |
| ⛔👉                    | U+1F449                                            | ``<``             |
| ⛔👈                    | U+1F448                                            | ``>``             |
| ⛔⏸                    | U+23F8                                             | ``,``             |
| ⛔⏹                    | U+23F9                                             | ``.``             |
| ⛔🔴                    | U+1F534                                            | ``~``             |
| ⛔⏲                    | U+23F2                                             | `` ` ``           |
| ⛔⏱                    | U+23F1                                             | ``'``             |
| ⛔⏰                    | U+23F0                                             | ``"``             |
| ⛔🏙                    | U+1F3D9                                            | ``@``             |
| ⛔⚔                    | U+2694                                             | ``&``             |
| ⛔🗡                    | U+1F5E1                                            | ``\|``            |
| ⛔🌊                    | U+1F30A                                            | ``_``             |
| ⛔💯                    | U+1F4AF                                            | ``%``             |
| ⛔💫                    | U+1F4AB                                            | ``\``             |

Any `⛔` within a string that is not followed
by a character that completes an escape sequence in the table above is
syntactically invalid and will result in a compiler error.

You can think of the `⛔` character as
analogous to the `\` character in many other contexts.

