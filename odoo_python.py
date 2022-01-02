interval_count = fields.Integer(string="Interval Count")
interval = fields.Char(string="Interval")


# NAME GET Method
@api.depends('interval_count','interval')
def name_get(self):
    result = []
    for rec in self:
        name = str(rec.interval_count) + ' ' + rec.interval
        result.append((rec.id, name))
    return result

