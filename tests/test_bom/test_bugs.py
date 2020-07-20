"""
Bugs tests

- Columns aren't case-insensitive.

For debug information use:
pytest-3 --log-cli-level debug

"""

import os
import sys
import logging
# Look for the 'utils' module from where the script is running
prev_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if prev_dir not in sys.path:
    sys.path.insert(0, prev_dir)
# Utils import
from utils import context  # noqa: E402


def test_column_sensitive():
    """ Test if the COLUMN_ORDER section can contain columns in lowercase """
    prj = 'links'
    ext = 'csv'
    ctx = context.TestContext('ColumnSensitive', prj, ext, 'column_sensitive')
    ctx.run()
    out = prj + '.' + ext
    heads = ctx.load_csv_header(out)
    logging.debug(heads)
    assert len(heads) == 4
    ctx.clean_up()
