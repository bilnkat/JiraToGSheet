import json
from my_data2 import json_data
from tkt_model import Tkt_Entry
from cdw_sheet_model import SheetsConnector

jira_data = json.loads(json_data)

def get_newhire_tickets_from_jira(tickets):
    tkt_objects = []
    for item in tickets['issues']:
        field = item['fields']
        key = item['key']
        status = field['status']['name']
        start_date = field['customfield_10800']
        address = field['customfield_10825']
        email = field['customfield_10826']
        bundle = field['customfield_10836']['value']
        first = field['customfield_10839']
        last = field['customfield_10840']
        summary = field['summary']
        try:
            assignee = field['assignee']['displayName']
        except:
            assignee = None
        try:
            tmp_list = []
            for tkt in field['description']['content']:
                for item in tkt['content']:
                    if 'text' in item.keys():
                        tmp_list.append(item['text'])
            desc = ' '.join(tmp_list)
            description = desc
        except:
            description = None
        cdw_entry = Tkt_Entry(key=key, summary=summary, assignee=assignee, start_date_10800=start_date, email_10826=email, bundle_10836=bundle, equipment=description, other_name_10825=address, first_10839=first, last_10840=last, status = status)
        tkt_objects.append(cdw_entry)

    return tkt_objects


tickets = get_newhire_tickets_from_jira(jira_data)
wsconnect = SheetsConnector()
for tkt in tickets:
    if tkt.get_key() not in wsconnect.get_key_list() and tkt.get_assignee() and tkt.get_status() != 'Done':
        wsconnect.update_row(tkt)
