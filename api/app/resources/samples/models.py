from flask_restx import fields


def sample(api):
    return api.model("Sample", model={
        "id": fields.Integer(
            readonly=True,
        ),
        "name": fields.String,
    })
