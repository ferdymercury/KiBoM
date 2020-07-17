# Skip the DNF HTML list if it will contain 0 rows

- **Pull-request**: [#113](https://github.com/SchrodingersGat/KiBoM/pull/113)
- **Opened**: 2020-07-17
- **Status**: Open
- **Branch**: skip_dnf_list_if_empty

## Description

The DNF (Do Not Fit) components are listed in a separated list when `html_generate_dnf` is `1`.
It was introduced by [Separate section for "Do Not Fit" components](Separate_DNF.md).

The problem is that when this list is empty we get a table with headings but no content.
This patch removes the table.
