"""create PartStorageLocation table

Revision ID: fc3442ba0053
Revises: f40979170c32
Create Date: 2021-02-21 20:54:50.470284

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey

# revision identifiers, used by Alembic.
revision = 'fc3442ba0053'
down_revision = 'f40979170c32'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'PartStorageLocation',
        sa.Column('part_id', sa.Integer, ForeignKey('Part.id'), primary_key=True),
        sa.Column('storage_location_id', sa.Integer, ForeignKey('StorageLocation.id'), primary_key=True),
    )


def downgrade():
    op.drop_table('PartStorageLocation')
