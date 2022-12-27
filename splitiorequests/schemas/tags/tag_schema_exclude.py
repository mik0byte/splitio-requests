"""Tag Schema with exclude"""

from marshmallow import Schema, fields, post_dump, post_load, EXCLUDE

from splitiorequests.models.tags.tag import Tag


class TagSchemaExclude(Schema):
    """Tag schema class

    Ignores and exclude unknown fields
    """
    class Meta:
        ordered = True
        unknown = EXCLUDE

    name = fields.Str(required=True)
    objectType = fields.Str(required=True)
    objectName = fields.Str(required=True)

    @post_load
    def load_tag(self, data, **kwargs):
        """Generates and returns Tag object"""
        return Tag(**data)

    @post_dump
    def return_dict(self, data, **kwargs):
        """Converts Schema object into dictionary"""
        return dict(data)
