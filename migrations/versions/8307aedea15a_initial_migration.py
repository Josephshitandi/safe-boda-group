"""Initial Migration

Revision ID: 8307aedea15a
Revises: 
Create Date: 2020-11-04 16:18:51.812178

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8307aedea15a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
