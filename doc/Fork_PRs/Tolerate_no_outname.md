# Tolerate no `output_file_name` and/or `variant_file_name_format`

- **Pull-request**: [#121](https://github.com/SchrodingersGat/KiBoM/pull/121)
- **Opened**: 2020-07-18
- **Status**: Open
- **Branch**: tolerate_no_filename

## Description

If a INI file doesn't contain `output_file_name` and/or `variant_file_name_format` an exception is raised.

This was reported as issue [#70](https://github.com/SchrodingersGat/KiBoM/issues/70) and I hit it trying to find a minimal config to extract only the headings.

This patch adds fallbacks to the current default values, avoiding an exception.


