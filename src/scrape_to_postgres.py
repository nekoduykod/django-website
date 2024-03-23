import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydjango.settings")
django.setup()


import requests

from myapp.models import Projects


def scrape_ibrd():
    url = "https://search.worldbank.org/api/v2/projects?format=json&rows=200&fct=projectfinancialtype_exact,status_exact,regionname_exact,themev2_level1_exact,themev2_level2_exact,themev2_level3_exact,sector_exact,countryshortname_exact,cons_serv_reqd_ind_exact,esrc_ovrl_risk_rate_exact&fl=id,regionname,countryname,projectstatusdisplay,project_name,countryshortname,pdo,impagency,cons_serv_reqd_ind,url,boardapprovaldate,closingdate,projectfinancialtype,curr_project_cost,ibrdcommamt,idacommamt,totalamt,grantamt,borrower,lendinginstr,envassesmentcategorycode,esrc_ovrl_risk_rate,sector1,sector2,sector3,theme1,theme2,%20%20status,totalcommamt,proj_last_upd_date,curr_total_commitment,curr_ibrd_commitment,curr_ida_commitment,last_stage_reached_name,theme_list,ida_cmt_usd_amt,cmt_usd_amt,projectcost&apilang=en&projectfinancialtype_exact=IBRD&os=0&sector_exact=Health"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for project_id, project_info in data['projects'].items():
            title = project_info.get('project_name', None)
            date = project_info.get('boardapprovaldate', None)
            amount = project_info.get('curr_total_commitment', None)
            status = project_info.get('projectstatusdisplay', None)
            location = project_info.get('countryname', None)
            project_type = ', '.join(project_info.get('projectfinancialtype', None))

            sectors = []
            for i in range(1, 4):
                sector_key = f'sector{i}'
                if sector_key in project_info:
                    sectors.append(project_info[sector_key]['Name'])
            sector = ', '.join(sectors) if sectors else None

            project = Projects(
                project_id=project_id,
                title=title,
                date=date,
                amount=amount,
                status=status,
                location=location,
                sector=sector,
                type=project_type
            )
            project.save()

        print("Data loaded into PostgreSQL table!")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)


if __name__ == "__main__":
    scrape_ibrd()