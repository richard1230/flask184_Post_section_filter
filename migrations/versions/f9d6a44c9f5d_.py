"""empty message

Revision ID: f9d6a44c9f5d
Revises: bcd1ceec0210
Create Date: 2019-12-26 22:54:41.905035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9d6a44c9f5d'
down_revision = 'bcd1ceec0210'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('banner', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('banner', 'create_time')
    # ### end Alembic commands ###