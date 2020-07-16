# Avoid destroying the current locale's decimal point

- **Pull-request**: [#111](https://github.com/SchrodingersGat/KiBoM/pull/111)
- **Opened**: 2020-07-16
- **Status**: Open
- **Branch**: locale_decimal_point_in_value

## Description

The units parser currently prunes any comma.
But for many locales this is the decimal point separator.
This patch converts the current locale decimal point into a point.

It means you are free to use the decimal point for your current locale.
For me, using es_AR.UTF-8 means I can use "4,7k" instead of "4.7k".
Note that I can still use "4.7k".
