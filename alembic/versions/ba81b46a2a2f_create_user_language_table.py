"""create user_language table

Revision ID: ba81b46a2a2f
Revises: 49985c956d8a
Create Date: 2020-11-13 18:50:15.692031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba81b46a2a2f'
down_revision = '49985c956d8a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user_language",

        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.Column("language_id", sa.BigInteger(), nullable=False),
        sa.Column("is_primary", sa.Boolean(), nullable=False, default=False),

        sa.ForeignKeyConstraint(["user_id"], ["user.id"], ),
        sa.ForeignKeyConstraint(["language_id"], ["language.id"], ),
    )

    op.create_index(op.f("index_user_language_user_id"), "user_language", ["user_id"])
    op.create_index(op.f("index_user_language_language_id"), "user_language", ["language_id"])


def downgrade():
    op.drop_index("index_user_language_user_id", table_name="user_language")
    op.drop_index("index_user_language_language_id", table_name="user_language")
    op.drop_table("user_language")
