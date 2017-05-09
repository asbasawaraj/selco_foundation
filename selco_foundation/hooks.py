# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "selco_foundation"
app_title = "Selco Foundation"
app_publisher = "SELCO Foundation"
app_description = "Customizations of selco foundation"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "erp@selcofoundation.org"
app_license = "MIT"

# Includes in <head>
# ------------------
fixtures = ["Custom Field","Custom Script","Property Setter","Print Format"]

# include js, css files in header of desk.html
# app_include_css = "/assets/selco_foundation/css/selco_foundation.css"
# app_include_js = "/assets/selco_foundation/js/selco_foundation.js"

# include js, css files in header of web template
# web_include_css = "/assets/selco_foundation/css/selco_foundation.css"
# web_include_js = "/assets/selco_foundation/js/selco_foundation.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "selco_foundation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "selco_foundation.install.before_install"
# after_install = "selco_foundation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "selco_foundation.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"selco_foundation.tasks.all"
# 	],
# 	"daily": [
# 		"selco_foundation.tasks.daily"
# 	],
# 	"hourly": [
# 		"selco_foundation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"selco_foundation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"selco_foundation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "selco_foundation.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "selco_foundation.event.get_events"
# }
