from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nick_name=None, address=None,
                 home_number=None, mobile_number=None, birth_day=None, birth_month=None, birth_year=None,
                 email=None, notes=None, id=None, work_number=None, fax_number=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None, email2=None, email3=None, second_number=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nick_name
        self.address = address
        self.home_number = home_number
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.fax_number = fax_number
        self.second_number = second_number
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (
        self.id, self.first_name, self.last_name, self.address, self.nickname, self.address,
        self.home_number, self.mobile_number, self.work_number, self.fax_number, self.second_number, self.birth_day,
        self.birth_month, self.birth_year, self.email, self.email2, self.email3, self.notes)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.first_name is None or
                other.first_name is None or self.first_name == other.first_name) and (self.last_name is None or
                other.last_name is None or self.last_name == other.last_name) and (self.address is None or other.address
                is None or self.address == other.address)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
