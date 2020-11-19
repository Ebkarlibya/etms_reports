# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "etms_reports"
app_title = "Etms Reports"
app_publisher = "ebkar solutions"
app_description = "Custom Reports"
app_icon = "octicon octicon-graph"
app_color = "black"
app_email = "admin@ebkar.ly"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/etms_reports/css/etms_reports.css"
# app_include_js = "/assets/etms_reports/js/etms_reports.js"

# include js, css files in header of web template
# web_include_css = "/assets/etms_reports/css/etms_reports.css"
# web_include_js = "/assets/etms_reports/js/etms_reports.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "etms_reports.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "etms_reports.install.before_install"
# after_install = "etms_reports.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "etms_reports.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }
# Fixtures
fixtures = [
     {
         "dt": "Custom Field",
         "filters": [
           ["fieldname", "in", ["account_currency", "account_balance"]]
         ]
     },
     {
         "dt": "Custom Script",
         "filters": [
            ["name", "in", ["Bank Account-Client"]]
         ]
     }
]

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
	"Bank Account": {
        "validate": "etms_reports.customs.bank_account.validate",
		# "on_update": "method",
		# "on_cancel": "method",
		# "on_trash": "method"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"etms_reports.tasks.all"
# 	],
# 	"daily": [
# 		"etms_reports.tasks.daily"
# 	],
# 	"hourly": [
# 		"etms_reports.tasks.hourly"
# 	],
# 	"weekly": [
# 		"etms_reports.tasks.weekly"
# 	]
# 	"monthly": [
# 		"etms_reports.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "etms_reports.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "etms_reports.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "etms_reports.task.get_dashboard_data"
# }

