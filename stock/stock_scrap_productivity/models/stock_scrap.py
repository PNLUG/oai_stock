from odoo import models, fields


class StockScrap(models.Model):
    _inherit = "stock.scrap"

    # new fields
    # productivity reference
    productivity_id = fields.Many2one(
        comodel_name="mrp.workcenter.productivity",
        string="Productivity",
        help="Productivity declaration reference",
        index=True,
        ondelete="cascade",
        required=True,
        )
