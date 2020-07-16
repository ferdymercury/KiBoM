# Modified the R/L/C sort to try to make sense of the multiplier

- **Pull-request**: [#82](https://github.com/SchrodingersGat/KiBoM/pull/82)
- **Opened**: 2020-03-11 (updated 2020-07-16)
- **Status**: Open
- **Branch**: better_sort

## Description

It helps to get 5 pF before 1 nF.

The original search is alphabetic, making *1 nF* to be *smaler* than *5 pF*.
This patch interprets *5 pF* as 5000 and *1 nF* as 1000000 (fempto Farad).

Valid prefixes:

- **pico**, **p**: 1e-12
- **nano**, **n**: 1e-9
- **μ**, **u**, **micro**: 1e-6
- **milli**, **m**: 1e-3
- **kilo**, **k**: 1e3
- **mega**, **meg**, **M**: 1e6
- **giga**, **g**: 1e9

All case insensitive, except 'M', see: [Use "M" for "mega" and "m" for "milli"](Fork_PRs/Mega_prefix.md)

The prefix can be mixed with the value, instead of the decimal separator: "3R3", "4k7", "2p2", etc.

Valid units are:

- **Resistor**: r, ohms, ohm, Ω
- **Capacitor**: farad, f
- **Inductor**: henry, h

All case insensitive.

## How to use

Just use the propper units and multipliers.

## Limitations

Not all possible cases are covered. If you have a case to add just report it.
