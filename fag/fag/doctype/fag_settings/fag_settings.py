# Copyright (c) 2025, DonnC and contributors
# For license information, please see license.txt

# import frappe
from fag.guard import reset_fag_cache
from frappe.model.document import Document


class FAGSettings(Document):
	def on_update(self):
		reset_fag_cache()
