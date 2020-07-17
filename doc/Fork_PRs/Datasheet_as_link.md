# Adds an option to make a column to contain datasheet links

- **Pull-request**: [#112](https://github.com/SchrodingersGat/KiBoM/pull/112), was [#79](https://github.com/SchrodingersGat/KiBoM/pull/79)
- **Opened**: 2020-07-16 (previous 2020-03-11)
- **Status**: Open
- **Branch**: datasheet_link_2 (previous datasheet_link)

## Description

Having a separated column for the datasheet is an overkill. We can make that another column contains this information as a link. The part number is a suitable column.

This patch allows configuring it.

## How to use

Define the `datasheet_as_link` option in the configuration file (i.e. `bom.ini`).

The value for this option is the column you want to convert into a link to the datasheet. Example:

```
datasheet_as_link = manf#
```

This will make entries in the column `manf#` (manufacturer part number) links to the datasheet.

## Limitations

Only available for HTML

## Example

Schematic: [links.sch](../../tests/input_samples/links.sch)

### Without `datasheet_as_link`

Configuration: [ds_no_link.ini](examples/ds_no_link.ini)
Generated: [BoM](examples/ds_no_link.html)

### With `datasheet_as_link`

In `[BOM_OPTIONS]` section we set:

```
datasheet_as_link = manf#
```

And in the `[IGNORE_COLUMNS]` section we add `Datasheet`. So we save one column.

Configuration: [ds_link.ini]( examples/ds_link.ini)
Generated: [BoM](examples/ds_link.html)

