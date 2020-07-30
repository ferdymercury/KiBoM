# Fix problems when using lowercase names in COLUMN_ORDER

- **Issue**: [#123](https://github.com/SchrodingersGat/KiBoM/pull/123)
- **Local PR**: [#10](https://github.com/INTI-CMNB/KiBoM/pull/10)
- **Partial PR** [#128](https://github.com/SchrodingersGat/KiBoM/pull/128)
- **Opened**: 2020-07-19
- **Status**: Open
- **Branch**: fix_column_case

## Description

The documentation says this section (as others) are case-insensitive.
The code does some effort, but is not enough.
This patch fixes problems in various classes:

- class ColumList: was case sensitive, now it allows insensitive searchs.
- class xmlElement: did user field look-ups case sensitive.
- class ComponentGroup: getField and upddateFields were case sensitive.

This patch also removes plenty of calls to "lower()" inside loops.
More conversions can be saved now, but needs intensive analisys.

- Configuration example: [tests/config_samples/column_sensitive.ini](https://github.com/INTI-CMNB/KiBoM/blob/master/tests/config_samples/column_sensitive.ini)
- Test netlist: [tests/input_samples/links.xml](https://github.com/INTI-CMNB/KiBoM/blob/master/tests/input_samples/links.xml)

Columns generated in the CSV:

```
references,value,part,description,Description,Part,References,Value
```

After applying the patch:

```
references,value,part,description
```
