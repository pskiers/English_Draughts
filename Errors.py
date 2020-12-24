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


class CoordinatesNotOnTheBoardError(ValueError):
    pass


class ChosenWitheSquareError(ValueError):
    pass


class NotAPushMoveError(ValueError):
    pass


class NotACaptureMoveError(ValueError):
    pass


class SquareTakenError(ValueError):
    pass


class NoPieceOnTheSquareError(ValueError):
    pass


class CapturingNothingError(ValueError):
    pass


class CapturingYourOwnPiceError(ValueError):
    pass
