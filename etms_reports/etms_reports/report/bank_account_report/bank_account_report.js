// Copyright (c) 2016, ebkar solutions and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Bank Account Report"] = {
	"filters": [
		{
			"fieldname": "account",
			"label": __("Company Account"),
			"fieldtype": "Link",
            "options": "Account",

        },
        {
            "fieldname": "account_currency",
            "label": __("Account Currency"),
            "fieldtype": 'Link',
            "options": "Currency"
        }
	]
};