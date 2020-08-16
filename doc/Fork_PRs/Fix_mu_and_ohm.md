# Support for real 'micro' prefix and fix 'Ohm' symbol support

- **Pull-request**: [#135](https://github.com/SchrodingersGat/KiBoM/pull/135)
- **Issue**: [#133](https://github.com/SchrodingersGat/KiBoM/pull/133)
             [#134](https://github.com/SchrodingersGat/KiBoM/pull/134)
- **Opened**: Merged (2020-08-16)
- **Status**: Open
- **Branch**: fix_mu_and_ohm


## Mu vs micro issue (#133)

While testing the code I found that:

https://github.com/SchrodingersGat/KiBoM/blob/06a14866d8166cfa71ae8ac1a48bda0c160fb380/kibom/units.py#L16

Is using:
GREEK SMALL LETTER MU	U+03BC	GREEK SMALL LETTER MU	&#x03BC;

But, at least for me, is more common to use:
MICRO SIGN	U+00B5	MICRO SIGN	µ

So I'm using:
```python
REFIX_MICRO = [u"&#x03BC;", u"&#x00B5", "u", "micro"]
```
Which looks pretty lame, and I hope the cut & paste worked ;-), but includes both: the micro sign and the greek letter.


## Lowercase omega issue (#134)

The ohm detection is wrong:

https://github.com/SchrodingersGat/KiBoM/blob/06a14866d8166cfa71ae8ac1a48bda0c160fb380/kibom/units.py#L28

We always apply `lower()` so we never really get uppercase omega.
This is the correct list:

```python
UNIT_R = ["r", "ohms", "ohm", u'\u03c9']
```

BTW, I found that an uncommon unicode that we also support is:

'OHM SIGN' (U+2126)
*SI unit of resistance, named after G. S. Ohm, German physicist preferred representation is U+03A9*

The lowercase is the same for:

'GREEK CAPITAL LETTER OMEGA' (U+03A9)

So the above code covers both.