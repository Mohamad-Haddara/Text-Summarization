from tortoise import fields, models

# Create new database model
class TextSummary(models.Model):    # Table
    # Column
    url = fields.TextField()
    summary = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add = True)
    
    def __str__(self):
        return self.url
    