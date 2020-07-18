# Added 'digikey_link' to make a column with links to digikey P/Ns

- **Pull-request**: [#114](https://github.com/SchrodingersGat/KiBoM/pull/114), was [#80](https://github.com/SchrodingersGat/KiBoM/pull/80)
- **Opened**: 2020-07-17 (previous 2020-03-11)
- **Status**: Merged (2020-07-17)
- **Branch**: digikey_link_2 (previous was digikey_link)

## Description

Digi-Key is one of the most complete electronic parts providers. Is often used as a reference.

If you have a field containing the Digi-Key part number you can make its column to contain links to the Digi-Key web page for this component.

## How to use

Define the `digikey_link` option in the configuration file (i.e. `bom.ini`).

The value for this option is the column you want to convert into a link to the Digi-Key.
Note that this field must be a valid Digi-Key part number.
Example:

```
digikey_link = digikey#
```

This will make entries in the column `digikey#` (Digi-Key part number) links to the component's web page.

You can specify more than one fiel name using tab (ASCII 9) as separator:

```
digikey_link = digikey#	digikey_alt#
```

## Limitations

- Only available for HTML.
- Could break if Digi-Key changes it web layout. Please report any problem.

## Example

Schematic: [links.sch](../../tests/input_samples/links.sch)

### Without `digikey_link`

Configuration: [dk_no_link.ini](examples/dk_no_link.ini)
Generated: [BoM](https://htmlpreview.github.io/?https://github.com/INTI-CMNB/KiBoM/blob/master/doc/Fork_PRs/examples/dk_no_link.html)

### With `digikey_link`

In `[BOM_OPTIONS]` section we set:

```
digikey_link = digikey#
```

Configuration: [dk_link.ini](examples/dk_link.ini)
Generated: [BoM](https://htmlpreview.github.io/?https://github.com/INTI-CMNB/KiBoM/blob/master/doc/Fork_PRs/examples/dk_link.html)

