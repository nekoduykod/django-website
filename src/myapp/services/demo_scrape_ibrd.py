'''This is basic url'''
# https://projects.worldbank.org/en/projects-operations/projects-list?os=0


''' Financing Type (Type) - IBRD; Sector - Health ''' 
# https://projects.worldbank.org/en/projects-operations/projects-list?projectfinancialtype_exact=IBRD&os=0&sector_exact=Health

'''XHR''' 
# https://search.worldbank.org/api/v2/projects?format=json&fct=projectfinancialtype_exact,status_exact,regionname_exact,themev2_level1_exact,themev2_level2_exact,themev2_level3_exact,sector_exact,countryshortname_exact,cons_serv_reqd_ind_exact,esrc_ovrl_risk_rate_exact&fl=id,regionname,countryname,projectstatusdisplay,project_name,countryshortname,pdo,impagency,cons_serv_reqd_ind,url,boardapprovaldate,closingdate,projectfinancialtype,curr_project_cost,ibrdcommamt,idacommamt,totalamt,grantamt,borrower,lendinginstr,envassesmentcategorycode,esrc_ovrl_risk_rate,sector1,sector2,sector3,theme1,theme2,%20%20status,totalcommamt,proj_last_upd_date,curr_total_commitment,curr_ibrd_commitment,curr_ida_commitment,last_stage_reached_name,theme_list,ida_cmt_usd_amt,cmt_usd_amt,projectcost&apilang=en&srt=id&order=desc&rows=20&projectfinancialtype_exact=IBRD&sector_exact=Health&os=0"

import json

import requests


url = "https://search.worldbank.org/api/v2/projects?format=json&rows=200&fct=projectfinancialtype_exact,status_exact,regionname_exact,themev2_level1_exact,themev2_level2_exact,themev2_level3_exact,sector_exact,countryshortname_exact,cons_serv_reqd_ind_exact,esrc_ovrl_risk_rate_exact&fl=id,regionname,countryname,projectstatusdisplay,project_name,countryshortname,pdo,impagency,cons_serv_reqd_ind,url,boardapprovaldate,closingdate,projectfinancialtype,curr_project_cost,ibrdcommamt,idacommamt,totalamt,grantamt,borrower,lendinginstr,envassesmentcategorycode,esrc_ovrl_risk_rate,sector1,sector2,sector3,theme1,theme2,%20%20status,totalcommamt,proj_last_upd_date,curr_total_commitment,curr_ibrd_commitment,curr_ida_commitment,last_stage_reached_name,theme_list,ida_cmt_usd_amt,cmt_usd_amt,projectcost&apilang=en&projectfinancialtype_exact=IBRD&os=0&sector_exact=Health"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open('projects_data.json', 'w') as file:
        json.dump(data, file)

    print("JSON data saved to project_data.json.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)