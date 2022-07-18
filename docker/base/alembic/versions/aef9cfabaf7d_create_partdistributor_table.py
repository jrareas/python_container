"""create PartDistributor table

Revision ID: aef9cfabaf7d
Revises: fc3442ba0053
Create Date: 2021-02-21 20:55:10.904656

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision = 'aef9cfabaf7d'
down_revision = 'fc3442ba0053'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'PartDistributor',
        sa.Column('part_id', sa.Integer, ForeignKey('Part.id'), primary_key=True),
        sa.Column('distributor_id', sa.Integer, ForeignKey('Part.id'), nullable=False, primary_key=True),
    )


def downgrade():
    op.drop_table('PartDistributor')
