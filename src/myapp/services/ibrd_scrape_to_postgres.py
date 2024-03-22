import requests
import psycopg2

from config import PG_DB_NAME, PG_USER, PG_PASS, PG_HOST, PG_PORT


with psycopg2.connect(dbname=PG_DB_NAME, user=PG_USER, password=PG_PASS, host=PG_HOST, port=PG_PORT) as connection:
    with connection.cursor() as cursor:
        url = "https://search.worldbank.org/api/v2/projects?format=json&rows=200&fct=projectfinancialtype_exact,status_exact,regionname_exact,themev2_level1_exact,themev2_level2_exact,themev2_level3_exact,sector_exact,countryshortname_exact,cons_serv_reqd_ind_exact,esrc_ovrl_risk_rate_exact&fl=id,regionname,countryname,projectstatusdisplay,project_name,countryshortname,pdo,impagency,cons_serv_reqd_ind,url,boardapprovaldate,closingdate,projectfinancialtype,curr_project_cost,ibrdcommamt,idacommamt,totalamt,grantamt,borrower,lendinginstr,envassesmentcategorycode,esrc_ovrl_risk_rate,sector1,sector2,sector3,theme1,theme2,%20%20status,totalcommamt,proj_last_upd_date,curr_total_commitment,curr_ibrd_commitment,curr_ida_commitment,last_stage_reached_name,theme_list,ida_cmt_usd_amt,cmt_usd_amt,projectcost&apilang=en&projectfinancialtype_exact=IBRD&os=0&sector_exact=Health"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

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

            print("Data loaded into PostgreSQL table!")
        else:
            print("Failed to retrieve data. Status code:", response.status_code)