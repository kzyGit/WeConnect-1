""" User Model """
from api.models.store import Store


class Business():
    """Users Model"""

    def save(self, data):
        """ Save user in the main store """
        Store().save_business(data)
