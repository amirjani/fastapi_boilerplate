from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dae9a17f9d6'
down_revision = 'f6f4d3c20ab5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "role_permission",

        sa.Column("role_id", sa.BigInteger(), nullable=False),
        sa.Column("permission_id", sa.BigInteger(), nullable=False),

        sa.ForeignKeyConstraint(["role_id"], ["role.id"], ),
        sa.ForeignKeyConstraint(["permission_id"], ["permission.id"], ),
    )

    op.create_index(op.f("index_role_permission_role_id"), "role_permission", ["role_id"])
    op.create_index(op.f("index_role_permission_permission_id"), "role_permission", ["permission_id"])


def downgrade():
    op.drop_index("index_role_permission_role_id", table_name="role_permission")
    op.drop_index("index_role_permission_permission_id", table_name="role_permission")
    op.drop_table("role_permission")

