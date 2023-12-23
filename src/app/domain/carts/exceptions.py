from decimal import Decimal


class BaseCartDomainError(Exception):
    pass


class CartItemDoesNotExistError(BaseCartDomainError):
    pass


class NotOwnedByUserError(BaseCartDomainError):
    pass


class MaxItemsQtyLimitExceeded(BaseCartDomainError):
    pass


class SpecificItemQtyLimitExceeded(BaseCartDomainError):
    def __init__(self, limit: Decimal, actual: Decimal) -> None:
        self.limit = limit
        self.actual = actual


class ChangeStatusError(BaseCartDomainError):
    pass


class OperationForbiddenError(BaseCartDomainError):
    pass
