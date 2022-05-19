import gspread

class SheetsConnector:

    def __init__(self):
        self._url = 'https://docs.google.com/spreadsheets/d/1EYZ3ErXQWKHsDUb2-vHPucRW0Ev3XW1n24mTlrVQM60/edit#gid=0'
        self._wks = gspread.service_account().open_by_url(self._url).sheet1
        self._key_cell = self._wks.find('Key')
        self._start_date_cell = self._wks.find('Start date')
        self._address_cell = self._wks.find('Other Name (If Applicable)')
        self._email_cell = self._wks.find('Personal Email')
        self._bundle_cell = self._wks.find('Peripheral Bundle - Including 27" Monitor')
        self._first_cell = self._wks.find('Preferred First Name')
        self._last_cell = self._wks.find('Last Name')
        self._summary_cell = self._wks.find('Summary')
        self._assignee_cell = self._wks.find('Assignee')
        self._description_cell = self._wks.find('Computer Equipment')

    def get_newline_row(self):
        key_list = self.get_key_list()
        new_line = len(key_list) + 1
        return new_line

    def update_row(self, tkt_obj):
        next_line_available = self.get_newline_row()
        self._wks.update_cell(next_line_available, self._key_cell.col, tkt_obj.get_key())
        self._wks.update_cell(next_line_available, self._start_date_cell.col, tkt_obj.get_start_date())
        self._wks.update_cell(next_line_available, self._address_cell.col, tkt_obj.get_other_name())
        self._wks.update_cell(next_line_available, self._email_cell.col, tkt_obj.get_personal_email())
        self._wks.update_cell(next_line_available, self._bundle_cell.col, tkt_obj.get_peripheral_bundle())
        self._wks.update_cell(next_line_available, self._first_cell.col, tkt_obj.get_preferred_firstname())
        self._wks.update_cell(next_line_available, self._last_cell.col, tkt_obj.get_lastname())
        self._wks.update_cell(next_line_available, self._summary_cell.col, tkt_obj.get_summary())
        self._wks.update_cell(next_line_available, self._assignee_cell.col, tkt_obj.get_assignee())
        self._wks.update_cell(next_line_available, self._description_cell.col, tkt_obj.get_computer_equipment())
        print(f'New entry added on line {next_line_available}')

    def get_key_list(self):
        return self._wks.col_values(self._key_cell.col)
