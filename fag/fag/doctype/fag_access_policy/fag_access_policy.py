# Copyright (c) 2025, DonnC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from fag.guard import reset_fag_cache

class FAGAccessPolicy(Document):
	def validate(self):
		if not self.endpoint.startswith("/api/method/"):
			frappe.throw("Endpoint must start with /api/method/")

		# if not any([self.method_get, self.method_post, self.method_delete, self.method_put, self.method_patch, self.method_any]):
		# 	self.method_any = 1

	def after_insert(self):
		reset_fag_cache()

	def on_update(self):
		reset_fag_cache()

	def on_trash(self):
		reset_fag_cache()