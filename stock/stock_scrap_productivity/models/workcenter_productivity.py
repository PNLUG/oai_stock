from odoo import models, fields


class MrpWorkcenterProductivity(models.Model):
    _inherit = "mrp.workcenter.productivity"

    # new fields
    # scrap movement _todo_ corretto?
    scrap_ids = fields.One2many(
        comodel_name="stock.scrap",
        inverse_name="productivity_id",
        string="Scraps",
        copy=False,
        )

    # _todo_ sistemare visualizzazione campo in form scrap ordinato wc/pdy
    def name_get(self):
        res = []
        for record in self:
            res.append((
                record.id,
                "{}: {}".format(record.workcenter_id.name, record.loss_id.name)
                ))
        return res
