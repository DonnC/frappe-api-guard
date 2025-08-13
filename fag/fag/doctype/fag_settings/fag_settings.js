// Copyright (c) 2025, DonnC and contributors
// For license information, please see license.txt

frappe.ui.form.on("FAG Settings", {
	refresh(frm) {
		frm.add_custom_button(__("Reset Cache"), function () {
			frm.call({
				method: "fag.guard.reset_fag_cache",
				callback: function (r) {
					frappe.msgprint(r.message);
				},
			});
		});
	},
});
