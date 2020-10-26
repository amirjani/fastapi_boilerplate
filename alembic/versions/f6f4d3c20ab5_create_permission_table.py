"""create permission table

Revision ID: f6f4d3c20ab5
Revises: fb46825a41d9
Create Date: 2020-10-26 14:34:47.182831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6f4d3c20ab5'
down_revision = 'fb46825a41d9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "permission",
        sa.Column("id", sa.Integer(), nullable=False),

        sa.Column("is_primary", sa.Boolean(), nullable=False, default=False),
        sa.Column("name", sa.VARCHAR(32), nullable=False),

        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("deleted_at", sa.TIMESTAMP(timezone=True), nullable=True),

        sa.PrimaryKeyConstraint("id")
    )

    op.create_index(op.f("index_permission_is_primary"), "permission", ["is_primary"])
    op.create_index(op.f("index_permission_name"), "permission", ["name"])
    op.create_index(op.f("index_permission_created_at"), "permission", ["created_at"])
    op.create_index(op.f("index_permission_deleted_at"), "permission", ["deleted_at"])


def downgrade():
    op.drop_index("index_permission_is_primary", table_name="permission")
    op.drop_index("index_permission_name", table_name="permission")
    op.drop_index("index_permission_created_at", table_name="permission")
    op.drop_index("index_permission_deleted_at", table_name="permission")
    op.drop_table("permission")
