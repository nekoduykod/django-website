import json

import pandas as pd
# from myapp.models import Projects


with open('D:\projects\Django_scraping\projects_data.json', 'r') as file:
    data = json.load(file)

project_id_list = []
title_list = []
date_list = []
amount_list = []
status_list = []
location_list = []
sector_list = []
type_list = []


for project_id, project_info in data['projects'].items():

    project_id_list.append(project_id)
    title_list.append(project_info['project_name'])
    date_list.append(project_info['boardapprovaldate'])
    amount_list.append(project_info['curr_total_commitment'])
    status_list.append(project_info['projectstatusdisplay'])
    location_list.append(project_info['countryname'][0])
    type_list.append(', '.join(project_info['projectfinancialtype']))

    sectors = []
    for i in range(1, 4):
        sector_key = f'sector{i}'
        if sector_key in project_info:
            sectors.append(project_info[sector_key]['Name'])
    sector_list.append(', '.join(sectors))



df = pd.DataFrame({
    'project_id': project_id_list,
    'title': title_list,
    'date': date_list,
    'amount': amount_list,
    'status': status_list,
    'location': location_list,
    'sector': sector_list,
    'type': type_list
})


df.to_csv('demo_cleaned_data.csv', index=False)
print('CSV created')