"""add index to user table

Revision ID: f43ca57f0770
Revises: 50d2e4a63143
Create Date: 2020-11-01 20:37:51.744054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f43ca57f0770'
down_revision = '50d2e4a63143'
branch_labels = None
depends_on = None


def upgrade():
    op.create_foreign_key(
        "foreign_key_user_language", "user", "language", ["language_id"], ["id"]
    )

    op.create_foreign_key(
        "foreign_key_user_country", "user", "country", ["country_id"], ["id"]
    )


def downgrade():
    pass
