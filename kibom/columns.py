# -*- coding: utf-8 -*-


class ColumnList:

    # Default columns (immutable)
    COL_REFERENCE = 'References'
    COL_REFERENCE_L = COL_REFERENCE.lower()
    COL_DESCRIPTION = 'Description'
    COL_DESCRIPTION_L = COL_DESCRIPTION.lower()
    COL_VALUE = 'Value'
    COL_VALUE_L = COL_VALUE.lower()
    COL_FP = 'Footprint'
    COL_FP_L = COL_FP.lower()
    COL_FP_LIB = 'Footprint Lib'
    COL_FP_LIB_L = COL_FP_LIB.lower()
    COL_PART = 'Part'
    COL_PART_L = COL_PART.lower()
    COL_PART_LIB = 'Part Lib'
    COL_PART_LIB_L = COL_PART_LIB.lower()
    COL_SHEETPATH = 'Sheetpath'
    COL_SHEETPATH_L = COL_SHEETPATH.lower()
    COL_DATASHEET = 'Datasheet'
    COL_DATASHEET_L = COL_DATASHEET.lower()

    # Default columns for groups
    COL_GRP_QUANTITY = 'Quantity Per PCB'
    COL_GRP_QUANTITY_L = COL_GRP_QUANTITY.lower()
    # COL_GRP_TOTAL_COST = 'Total Cost'
    # COL_GRP_TOTAL_COST_L = COL_GRP_TOTAL_COST.lower()
    COL_GRP_BUILD_QUANTITY = 'Build Quantity'
    COL_GRP_BUILD_QUANTITY_L = COL_GRP_BUILD_QUANTITY.lower()

    # Generated columns
    _COLUMNS_GEN_L = [
        COL_GRP_QUANTITY_L,
        COL_GRP_BUILD_QUANTITY_L,
    ]

    # Default columns
    _COLUMNS_DEFAULT = [
        COL_DESCRIPTION,
        COL_PART,
        COL_PART_LIB,
        COL_REFERENCE,
        COL_VALUE,
        COL_FP,
        COL_FP_LIB,
        COL_SHEETPATH,
        COL_GRP_QUANTITY,
        COL_GRP_BUILD_QUANTITY,
        COL_DATASHEET
    ]

    # Default columns
    # These columns are 'immutable'
    _COLUMNS_PROTECTED_L = {
        COL_REFERENCE_L: 1,
        COL_GRP_QUANTITY_L: 1,
        COL_VALUE_L: 1,
        COL_PART_L: 1,
        COL_PART_LIB_L: 1,
        COL_DESCRIPTION_L: 1,
        COL_DATASHEET_L: 1,
        COL_FP_L: 1,
        COL_FP_LIB_L: 1,
        COL_SHEETPATH_L: 1
    }

    def __str__(self):
        return " ".join(map(str, self.columns))

    def __repr__(self):
        return self.__str__()

    def __init__(self, cols=_COLUMNS_DEFAULT):

        self.columns = []
        self.columns_l = {}

        # Make a copy of the supplied columns
        for col in cols:
            self.AddColumn(col)

    def _hasColumn(self, col):
        return col.lower() in self.columns_l

    """
    Remove a column from the list. Specify either the heading or the index
    """
    def RemoveColumn(self, col):
        if type(col) is str:
            self.RemoveColumnByName(col)
        elif type(col) is int and col >= 0 and col < len(self.columns):
            self.RemoveColumnByName(self.columns[col])

    def RemoveColumnByName(self, name):

        name = name.lower()
        # First check if this is in an immutable colum
        if name in self._COLUMNS_PROTECTED_L:
            return

        # Column does not exist, return
        if name not in self.columns_l:
            return

        try:
            name = self.columns_l[name]
            index = self.columns.index(name)
            del self.columns[index]
        except ValueError:
            return

    # Add a new column (if it doesn't already exist!)
    def AddColumn(self, col):

        # Already exists?
        if self._hasColumn(col):
            return

        # To enable fast lowercase search
        self.columns_l[col.lower()] = col
        # Case sensitive version
        self.columns.append(col)
