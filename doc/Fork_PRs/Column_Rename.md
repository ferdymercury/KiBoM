# Add a mechanism to rename columns

- **Pull-request**: [#120](https://github.com/SchrodingersGat/KiBoM/pull/120)
- **Opened**: 2020-03-18
- **Status**: Open
- **Branch**: column_rename

## Description

Column names displayed in the table head are the names of the KiCad fields or the internal names used by KiBoM.
Sometimes the names aren't pretty. As an example is common to use `manf#` for the part name used by the component manufacturer.
Using long names for KiCad fields is a bad idea.

This patch allows to rename the columns names so you can use pretty names in the headings.

## How to use

You must define a `COLUMN_RENAME` section in the configuration file.
Then add entries with the name of the original field and the name you want, separated by a tab (ASCII 9).
Here is an example:

```
[COLUMN_RENAME]
manf#	Manufacturer part number
```

Note that you must use a tab as separator. Using a space won't work because *Manufacturer part number* also has spaces.

## Limitations

The separator must be a tab.

## Example

Schematic: [links.sch](../../tests/input_samples/links.sch)

### Without `COLUMN_RENAME`

Configuration: [ds_no_link.ini](examples/col_no_rename.ini)
Generated: [BoM](https://htmlpreview.github.io/?https://github.com/INTI-CMNB/KiBoM/blob/master/doc/Fork_PRs/examples/col_no_rename.html)

### With `COLUMN_RENAME`

We add the following section:

```
[COLUMN_RENAME]
References	Ref
Part	Part number
Value	Value
manf#	Manufacturer part
digikey#	Digi-Key code
```

Configuration: [ds_link.ini](examples/col_rename.ini)
Generated: [BoM](https://htmlpreview.github.io/?https://github.com/INTI-CMNB/KiBoM/blob/master/doc/Fork_PRs/examples/col_rename.html)

## Additional notes

- This patch also makes the `prefs.ignore` list lowercase.
  This is to avoid converting it to lower case all the time.
- `prefs.colRename` is a hash. I saw that various preference options should also be a *dict* instead of a *list*.

