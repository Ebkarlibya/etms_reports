# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
# from erpnext.accounts.doctype.payment_entry.payment_entry import get_account_details

def execute(filters=None):
    columns = get_columns(filters)

    data = get_data(filters)


    return columns, data

def get_columns(filters):
    return [
		{
			"fieldname": "account_name",
			"label": "Account Name",
			"fieldtype": "data",
            "read_only": 1,
            "width": 150
			
		},
		{
			"fieldname": "account",
			"label": "Company Account",
			"fieldtype": "Link",
			"options": "Account",
            "width": 150
		},
		{
			"fieldname": "bank",
			"label": "Bank",
			"fieldtype": "Link",
			"options": "Bank",
            "width": 120
		},
		{
			"fieldname": "website",
			"label": "Website",
			"fieldtype": "Data",
			"read_only": 1,
            "width": 120
		},
        {
            "fieldname": 'account_currency',
            "label": "Account Currency",
            "fieldtype": "Read Only",
            "options": "Currency",
            "width": 120
        },
        {
            "fieldname": 'account_balance',
            "label": "Account Balance",
            "fieldtype": "Read Only",
            "width": 120
        },
        {
			"fieldname": "company",
			"label": "Company",
			"fieldtype": "data",
            "read_only": 1,
            "width": 120
			
		},
	]
    
def get_data(filters):
    row = {}
    idx = 0
    data = []
    filters_dict = {}

    # if(filters.get('bank')):
    #     res = frappe.db.sql(f"select * from `tabBank Account` where bank='{filters.get('bank')}'", as_dict=1)
    # else:
    #     res = frappe.db.sql("select * from `tabBank Account`", as_dict=1)
    if(filters.get("account")):
        filters_dict["account"]=filters.get("account")

    if(filters.get("account_currency")):
        filters_dict["account_currency"]=filters.get("account_currency")
    
    res = frappe.get_all("Bank Account", fields=['*'], filters=filters_dict)

    while (idx < len(res)):
        # details = get_account_details(res[idx].account, '')
        row = {
        	'account_name': res[idx].account_name,
            'account': res[idx].account,
            'bank': res[idx].bank,
            'website': res[idx].website,
            'account_currency': res[idx].account_currency,
            'account_balance': res[idx].account_balance,
            'company': res[idx].account,
        }
        data.append(row)
        idx+=1

    return res
