"""empty message

Revision ID: 6246b889ce75
Revises: 0119e79e34bf
Create Date: 2021-06-22 14:03:02.403556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6246b889ce75'
down_revision = '0119e79e34bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('talent', sa.Boolean(), nullable=False))
    op.add_column('Venue', sa.Column('description', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'description')
    op.drop_column('Venue', 'talent')
    op.drop_column('Venue', 'website_link')
    op.drop_column('Venue', 'genres')
    # ### end Alembic commands ###
