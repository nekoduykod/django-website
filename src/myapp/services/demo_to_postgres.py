import json

import psycopg2


connection = psycopg2.connect(
    dbname="projects",
    user="",
    password="",
    host="localhost",
    port="5432"
)

cursor = connection.cursor()


with open('D:\projects\Django_scraping\projects_data.json', 'r') as file:
    data = json.load(file)


for project_id, project_info in data['projects'].items():
    title = project_info['project_name']
    date = project_info['boardapprovaldate']
    amount = project_info['curr_total_commitment']
    status = project_info['projectstatusdisplay']
    location = project_info['countryname'][0]
    project_type = ', '.join(project_info['projectfinancialtype'])

    sectors = []
    for i in range(1, 4):
        sector_key = f'sector{i}'
        if sector_key in project_info:
            sectors.append(project_info[sector_key]['Name'])
    sector = ', '.join(sectors)

    sql = """
    INSERT INTO myapp_projects (project_id, title, date, amount, status, location, sector, type)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (project_id, title, date, amount, status, location, sector, project_type))

connection.commit()

cursor.close()
connection.close()

print("Data loaded into Django model successfully!")