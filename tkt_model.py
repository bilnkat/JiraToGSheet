class Tkt_Entry:

    def __init__(self, key, summary, assignee, start_date_10800, email_10826, bundle_10836, equipment, other_name_10825, first_10839, last_10840, status):
        self._key = key
        self._summary = summary
        self._assignee = assignee
        self._start_date = start_date_10800
        self._personal_email = email_10826
        self._peripheral_bundle = bundle_10836
        self._computer_equipment = equipment
        self._other_name = other_name_10825
        self._preferred_firstname = first_10839
        self._lastname = last_10840
        self._status = status

    def get_key(self):
        return self._key

    def get_summary(self):
        return self._summary

    def get_assignee(self):
        return self._assignee

    def get_start_date(self):
        return self._start_date

    def get_personal_email(self):
        return self._personal_email

    def get_peripheral_bundle(self):
        return self._peripheral_bundle

    def get_computer_equipment(self):
        return self._computer_equipment

    def get_other_name(self):
        return self._other_name

    def get_preferred_firstname(self):
        return self._preferred_firstname

    def get_lastname(self):
        return self._lastname

    def get_status(self):
        return self._status
