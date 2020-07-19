# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

## [1.8.0] - 2020-07-19
### Added
- Column head names can be customized (rename columns)
- Support for spaces before units in component values.

### Changed
- Conflicts (collisions) in `Config` field aren't reported as warnings.
  They are natural for variants and other uses.
- `alt_wrap` option was removed.
- The locale decimal point is converted into '.' for units computation.
- `M` is mega and `m` milli. Only case sensitive prefix.
- Enhanced the R/L/C sort by unit.
- Display KiBOM version when running script.
- Exit with error count.
- Removed colorama printing.

### Fixed
- Now `output_file_name` and/or `variant_file_name_format` can be empty.
- HTML DNF section is now omitted when empty.
- `+VARIANT` option not working.
- Any column can be rendered as datasheet links (HTML only).
- Any column can be joined.

## [1.6.3] - 2020-04-24
### Fixed
- Problem when no INI file (digikey_link not defined)

## [1.6.2] - 2020-04-23
### Changed
- Switched to Python 3 only to reduce the docker image size.

## [1.6.1] - 2020-03-13
### Added
- Support for "Do Not Change" components.
- Generate a separated list for DNF components (HTML only)
- Support for space as separator in `Config` field.
- Better R/L/C sort (using the units).
- Columns can be joined to save space (i.e. `Voltage` and `Tolerance`
  joined to `Value`)
- Digi-key part numbers can be rendered as web links (HTML only)
- A column can contain links to the datasheet (HTML only)
  Saves one column.

### Changed
- Avoid exposing the local path in outputs.

### Fixed
- `Description` field fallback now also working for KiCad 5.x.
