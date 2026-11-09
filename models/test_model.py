from odoo import models, fields, api

class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Test Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Enables Chatter/Audit trail

    name = fields.Char(string='Title', required=True, tracking=True)
    notes = fields.Text(string='Notes')
    active = fields.Boolean(string='Active', default=True)
    
    # Selection field for state management
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    # Priority rating star system
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string='Priority', default='1')

    # Computed field
    character_count = fields.Integer(
        string='Notes Character Count', 
        compute='_compute_character_count', 
        store=True
    )

    @api.depends('notes')
    def _compute_character_count(self):
        for record in self:
            record.character_count = len(record.notes) if record.notes else 0

    # Action buttons for state transitions
    def action_start(self):
        self.state = 'in_progress'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    def action_reset(self):
        self.state = 'draft'