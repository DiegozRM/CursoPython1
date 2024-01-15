from voluptuous.error import MultipleInvalid
from voluptuous.schema_builder import ALLOW_EXTRA, Schema
from rest_framework.exceptions import ValidationError

def validate_data(validators, data: dict, all_required = False, only_message = False, full_errors = False):

    try:
        validate = Schema(validators, extra = ALLOW_EXTRA, required = all_required)
        return validate(data)
    except (MultipleInvalid) as e:
        raise ValidationError({ '.'.join(str(element) for element in error.path): [(error.msg if not full_errors else error.__str__()).capitalize()] for error in e.errors } if not only_message else str(e).capitalize())