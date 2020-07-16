# Optimize the regex used to match component values

- **Pull-request**: [#110](https://github.com/SchrodingersGat/KiBoM/pull/110)
- **Opened**: 2020-07-16
- **Status**: Open
- **Branch**: optimize_units_regex

## Description

The regex used in units.py is huge, applied to all components many
times and compiled every time.

This patch uses a global variable to compile it once and reuse the
compiled regex.
