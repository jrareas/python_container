"""create account table

Revision ID: f0afe547ab12
Revises: 
Create Date: 2021-02-21 20:27:37.191897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0afe547ab12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True),
        sa.Column('email', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('User')
