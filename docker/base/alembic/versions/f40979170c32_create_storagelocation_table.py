"""create StorageLocation table

Revision ID: f40979170c32
Revises: 9d8e26a24f7c
Create Date: 2021-02-21 20:54:41.030570

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey

# revision identifiers, used by Alembic.
revision = 'f40979170c32'
down_revision = '9d8e26a24f7c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'StorageLocation',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('StorageLocation')