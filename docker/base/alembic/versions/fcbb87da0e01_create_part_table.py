"""create Part table

Revision ID: fcbb87da0e01
Revises: f0afe547ab12
Create Date: 2021-02-21 20:53:51.655706

"""
from alembic import op
import sqlalchemy as sa
from enum import unique


# revision identifiers, used by Alembic.
revision = 'fcbb87da0e01'
down_revision = 'f0afe547ab12'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Part',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('Part')
