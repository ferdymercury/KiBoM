# Fix for various configuration details

- **Issue**: [#67](https://github.com/SchrodingersGat/KiBoM/pull/67)
- **Local PR**: [#11](https://github.com/INTI-CMNB/KiBoM/pull/11)
- **Opened**: 2020-07-19
- **Status**: Open
- **Branch**: fix_various_ini_details_1

## Description

The configuration INI has various inconsistencies and errors.
This patch fixes or modifies:

- Added warning if boolean options aren't 0,1,yes,no,true,false
- `as_link` and `digikey_link`: avoid writing "False" boolean, which
  then is loaded as "False" string. Now using '' which is equivalent
  to False. (bool('') -> False). Introduced by me on
  SchrodingersGat/KiBoM#112 and SchrodingersGat/KiBoM#114.
- Put all SECTION_GENERAL options inside the already existing if.
- `backup` also made to default to '' instead of False for coherence.
- `hide_headers` and `hide_pcb_info` now support the same options as
  other booleans. Also write them as '0', not 'False' for coherence
  with all the other booleans.
- `board_variant` write as a string, not an array (bizarre
  ['default']" in created *bom.ini*)
- Add a checkStr method, to make it similar to checkInt and
  checkOption. Making the general options much more compact in the
  code.
- `output_file_name` and `variant_file_name_format` now use a more
  general fallback mechanism (fallback option is documented only for
  Python 3). Better than what I did in SchrodingersGat/KiBoM#121.

