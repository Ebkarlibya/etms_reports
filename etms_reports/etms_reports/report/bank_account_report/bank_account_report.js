// Copyright (c) 2016, ebkar solutions and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Bank Account Report"] = {
	"filters": [
		{
			"fieldname": "bank",
			"label": __("Bank"),
			"fieldtype": "Link",
            "options": "Bank",
        },
        {
            "fieldname": "account_currency",
            "label": __("Account Currency"),
            "fieldtype": 'Link',
            "options": "Currency"
        },
        {
            "fieldname": "company",
            "label": __("Company"),
            "fieldtype": 'Link',
            "options": "Company"
        }
	]
};