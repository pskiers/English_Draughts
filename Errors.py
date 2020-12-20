class BoardRowCountError(ValueError):
    pass


class RowLengthError(ValueError):
    pass


class PieceOnAWhiteSquareError(ValueError):
    pass


class NotAllowedThingOnTheBoardError(ValueError):
    pass


class NonIterableRowError(TypeError):
    pass


class NonIterableBoardError(TypeError):
    pass
