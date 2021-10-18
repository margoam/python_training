from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nick_name=None, address=None,
                 home_number=None, mobile_number=None, birth_day=None, birth_month=None, birth_year=None,
                 email=None, notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nick_name
        self.address = address
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.email = email
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s %s %s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.first_name is None or
                                                                                 other.first_name is None or self.first_name == other.first_name) \
               and (self.last_name is None or other.last_name is None or self.last_name == other.last_name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
