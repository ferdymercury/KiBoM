"""
Simple tests

- Simple cases for:
  - CSV
  - HTML
  - XML
  - XLSX
- Output in:
  - Same dir as netlist
  - Subdir relative to netlist
  - Unrelated dir (most test are this case)
  - Unrelated deep subdir
- Variants
  - Matrix in kibom-variante
  - V1+V3 from kibom-variante
- Components units
  - Sort and groups of RLC_sort

For debug information use:
pytest-3 --log-cli-level debug

"""

import os
import sys
import shutil
import logging
# Look for the 'utils' module from where the script is running
prev_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if prev_dir not in sys.path:
    sys.path.insert(0, prev_dir)
# Utils import
from utils import context  # noqa: E402

BOM_DIR = 'BoM'
KIBOM_TEST_COMPONENTS = ['C1', 'C2', 'C3', 'C4', 'R1', 'R2', 'R3', 'R4', 'R5', 'R7', 'R8', 'R9', 'R10']
EXCLUDE_TEST = ['R6']


def check_kibom_test_netlist(rows, components, exclude=EXCLUDE_TEST, groups=5, comps=KIBOM_TEST_COMPONENTS):
    """ Checks the kibom-test.xml expected results """
    # Groups
    assert len(rows) == groups
    logging.debug(str(groups) + " groups OK")
    # Components
    if comps:
        assert len(components) == len(comps)
        logging.debug(str(len(comps)) + " components OK")
    # Excluded
    if exclude:
        for ex in exclude:
            assert ex not in components
        logging.debug(str(len(exclude)) + " not fitted OK")
    # All the other components
    if comps:
        for c in comps:
            assert c in components
        logging.debug("list of components OK")


def check_dnc(rows, comp):
    for row in rows:
        if row.find(comp) != -1:
            fields = row.split(',')
            assert fields[6] == '1 (DNC)'
            logging.debug(comp + " is DNC OK")
            return


def test_bom_simple_csv():
    prj = 'kibom-test'
    ext = 'csv'
    ctx = context.TestContext('BoMSimpleCSV', prj, ext)
    ctx.run(no_config_file=True)
    out = prj + '_bom_A.' + ext
    rows, components = ctx.load_csv(out)
    check_kibom_test_netlist(rows, components)
    check_dnc(rows, 'R7')
    ctx.clean_up()


def test_bom_simple_html():
    prj = 'kibom-test'
    ext = 'html'
    ctx = context.TestContext('BoMSimpleHTML', prj, ext)
    ctx.run(no_config_file=True)
    out = prj + '_bom_A.' + ext
    rows, components, rows_dnf, dnf = ctx.load_html(out)
    check_kibom_test_netlist(rows, components, groups=5)
    assert len(dnf) == 1
    assert 'R6' in dnf
    ctx.clean_up()


def test_bom_simple_xml():
    prj = 'kibom-test'
    ext = 'xml'
    ctx = context.TestContext('BoMSimpleXML', prj, ext)
    ctx.run(no_config_file=True)
    out = prj + '_bom_A.' + ext
    rows, components = ctx.load_xml(out)
    check_kibom_test_netlist(rows, components)
    ctx.clean_up()


def test_bom_simple_xlsx():
    prj = 'kibom-test'
    ext = 'xlsx'
    ctx = context.TestContext('BoMSimpleXLSX', prj, ext)
    ctx.run(no_config_file=True)
    out = prj + '_bom_A.' + ext
    rows, components = ctx.load_xlsx(out)
    check_kibom_test_netlist(rows, components)
    ctx.clean_up()


def test_bom_deep_subdir():
    prj = 'kibom-test'
    ext = 'csv'
    ctx = context.TestContext('BoMDeepSubdir', prj, ext)
    sub_dir = os.path.join('1', '2', '3')
    extra = ['-d', os.path.abspath(os.path.join(ctx.output_dir, sub_dir))]
    ctx.run(no_config_file=True, no_subdir=True, extra=extra)
    out = os.path.join(sub_dir, prj + '_bom_A.' + ext)
    rows, components = ctx.load_csv(out)
    check_kibom_test_netlist(rows, components)
    ctx.clean_up()


def test_bom_same_dir():
    """ The default behavior: put the output along with the netlist """
    prj = 'kibom-test'
    ext = 'csv'
    ctx = context.TestContext('BoMSameDir', prj, ext)
    ctx.run(no_config_file=True, no_subdir=True)
    fn = prj + '_bom_A.' + ext
    out = os.path.join(ctx.get_board_dir(), fn)
    rows, components = ctx.load_csv(out)
    check_kibom_test_netlist(rows, components)
    # Move the result to the output dir, avoid pollution
    os.rename(out, ctx.get_out_path(fn))
    ctx.clean_up()


def test_bom_rel_dir():
    """ Relative sub directory (from netlist) """
    prj = 'kibom-test'
    ext = 'csv'
    ctx = context.TestContext('BoMRelSubDir', prj, ext)
    sub_dir = os.path.join('1', '2', '3')
    extra = ['-d', sub_dir]
    ctx.run(no_config_file=True, no_subdir=True, extra=extra)
    fn = prj + '_bom_A.' + ext
    out = os.path.join(ctx.get_board_dir(), sub_dir, fn)
    rows, components = ctx.load_csv(out)
    check_kibom_test_netlist(rows, components)
    # Move the result to the output dir, avoid pollution
    os.rename(out, ctx.get_out_path(fn))
    shutil.rmtree(os.path.join(ctx.get_board_dir(), '1'))
    ctx.clean_up()


def test_variant_t1_1():
    prj = 'kibom-variante'
    ext = 'csv'
    ctx = context.TestContext('BoMVar_t1_1', prj, ext)
    extra = ['-r', 'V1']
    ctx.run(no_config_file=True, extra=extra)
    out = prj + '_bom_A_(V1).' + ext
    rows, components = ctx.load_csv(out)
    assert len(rows) == 2
    assert len(components) == 2
    assert 'R1' in components
    assert 'R2' in components
    assert 'R3' not in components
    assert 'R4' not in components
    check_dnc(rows, 'R2')
    ctx.clean_up()


def test_variant_t1_2():
    prj = 'kibom-variante'
    ext = 'csv'
    ctx = context.TestContext('BoMVar_t1_2', prj, ext)
    extra = ['-r', 'V2']
    ctx.run(no_config_file=True, extra=extra)
    out = prj + '_bom_A_(V2).' + ext
    rows, components = ctx.load_csv(out)
    assert len(rows) == 1
    assert len(components) == 2
    assert 'R1' in components
    assert 'R2' not in components
    assert 'R3' in components
    assert 'R4' not in components
    ctx.clean_up()


def test_variant_t1_3():
    prj = 'kibom-variante'
    ext = 'csv'
    ctx = context.TestContext('BoMVar_t1_3', prj, ext)
    extra = ['-r', 'V3']
    ctx.run(no_config_file=True, extra=extra)
    out = prj + '_bom_A_(V3).' + ext
    rows, components = ctx.load_csv(out)
    assert len(rows) == 1
    assert len(components) == 2
    assert 'R1' in components
    assert 'R2' not in components
    assert 'R3' not in components
    assert 'R4' in components
    ctx.clean_up()


def test_variant_t1_4():
    prj = 'kibom-variante'
    ext = 'csv'
    ctx = context.TestContext('BoMVar_t1_4', prj, ext)
    ctx.run(no_config_file=True)
    out = prj + '_bom_A.' + ext
    rows, components = ctx.load_csv(out)
    assert len(rows) == 2
    assert len(components) == 3
    assert 'R1' in components
    assert 'R2' in components
    assert 'R3' in components
    assert 'R4' not in components
    check_dnc(rows, 'R2')
    ctx.clean_up()


def test_variant_t1_5():
    """ default union V3 """
    prj = 'kibom-variante'
    ext = 'csv'
    ctx = context.TestContext('BoMVar_t1_1', prj, ext)
    extra = ['-r', 'V1,V3']
    ctx.run(no_config_file=True, extra=extra)
    out = prj + '_bom_A_(V1,V3).' + ext
    rows, components = ctx.load_csv(out)
    assert len(rows) == 1
    assert len(components) == 2
    assert 'R1' in components
    assert 'R2' not in components
    assert 'R3' not in components
    assert 'R4' in components
    ctx.clean_up()


def test_sort_1():
    prj = 'RLC_sort'
    ext = 'csv'
    ctx = context.TestContext('BoMSort1', prj, ext)
    ctx.run(no_config_file=True)
    out = prj + '_bom_A.' + ext
    rows, components = ctx.load_csv(out)
    check_kibom_test_netlist(rows, components, exclude=None, groups=14, comps=None)
    exp = ['C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C1', 'C2', 'C3', 'C4', 'C11', 'C12',
           'R5', 'R4', 'R9', 'R10', 'R3', 'R2', 'R1', 'R8', 'R7']
    assert components == exp
    ctx.clean_up()


def test_datasheet_link():
    prj = 'links'
    ext = 'html'
    ctx = context.TestContext('DataSheetLink', prj, ext, 'datasheet_link')
    ctx.run()
    out = prj + '.' + ext
    rows, components, rows_dnf, dnf = ctx.load_html(out, 3, False)
    assert len(rows) == 2
    assert len(rows_dnf) == 1
    for c in components + dnf:
        assert c.strip().startswith('<a href')
        assert 'pdf' in c
        logging.debug(c + ' OK')
    ctx.clean_up()


def test_digikey_link():
    prj = 'links'
    ext = 'html'
    ctx = context.TestContext('DigiKeyLink', prj, ext, 'digikey_link')
    ctx.run()
    out = prj + '.' + ext
    rows, components, rows_dnf, dnf = ctx.load_html(out, 5, False)
    assert len(rows) == 2
    assert len(rows_dnf) == 1
    for c in components + dnf:
        assert c.strip().startswith('<a href')
        assert 'digikey' in c
        logging.debug(c + ' OK')
    ctx.clean_up()
