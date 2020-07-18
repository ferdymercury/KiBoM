# Added "join" to join fields like voltage, current, etc. with the value

- **Pull-request**: [#115](https://github.com/SchrodingersGat/KiBoM/pull/115), was [#81](https://github.com/SchrodingersGat/KiBoM/pull/81)
- **Opened**: 2020-07-17 (previous 2020-03-11)
- **Status**: Merged (2020-07-17)
- **Branch**: join_fields_2 (previous was join_fields)

## Description

1 nF 50 V isn't the same as 1 nF 100 V and having separated columns for each possible modifier is an overkill. Joining the fields to the value is compact and natural.

## How to use

Define a section named `[JOIN]`. In this section each entry is the name of a field, followed by the name of the fields that will be added to its column.
Use tab (ASCII 9) as separator. Example:

```
[JOIN]
Value	Voltage	Current	Power	Tolerance
```

This will attach the `Voltage`, `Current`, `Power` and `Tolerance` fields to the `Value` field. All case sensitive.

## Limitations

Fields are case sensitive.

## Example

Schematic: [join.sch](../../tests/input_samples/join.sch)

### Without `JOIN`

Configuration: [no_join.ini](examples/no_join.ini)
Generated: [BoM](https://htmlpreview.github.io/?https://github.com/INTI-CMNB/KiBoM/blob/master/doc/Fork_PRs/examples/no_join.html)

### With `JOIN`

In `[JOIN]` section we set:

```
Value	Tolerance	Voltage
manf	manf#
```

Configuration: [dk_link.ini](examples/join.ini)
Generated: [BoM](https://htmlpreview.github.io/?https://github.com/INTI-CMNB/KiBoM/blob/master/doc/Fork_PRs/examples/join.html)


