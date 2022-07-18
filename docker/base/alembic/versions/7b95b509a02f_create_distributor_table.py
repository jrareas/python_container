"""create Distributor table

Revision ID: 7b95b509a02f
Revises: 2752fb59ca7a
Create Date: 2021-02-21 20:54:17.379485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b95b509a02f'
down_revision = '2752fb59ca7a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Distributor',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('Distributor')
