"""create Manufacturer table

Revision ID: 9d8e26a24f7c
Revises: 7b95b509a02f
Create Date: 2021-02-21 20:54:24.505489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d8e26a24f7c'
down_revision = '7b95b509a02f'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'Manufacturer',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('Manufacturer')