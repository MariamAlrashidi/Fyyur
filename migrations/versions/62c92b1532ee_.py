"""empty message

Revision ID: 62c92b1532ee
Revises: bf3c309da710
Create Date: 2020-05-17 11:35:55.042838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62c92b1532ee'
down_revision = 'bf3c309da710'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('Show', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.add_column('Show', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.alter_column('Show', 'start_time',
               existing_type=sa.DATE(),
               nullable=False)
    op.drop_constraint('artist_id', 'Show', type_='foreignkey')
    op.drop_constraint('venue_id', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'])
    op.alter_column('Venue', 'genres',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'genres',
               existing_type=sa.TEXT(),
               nullable=True)
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('venue_id', 'Show', 'Venue', ['id'], ['id'])
    op.create_foreign_key('artist_id', 'Show', 'Artist', ['id'], ['id'])
    op.alter_column('Show', 'start_time',
               existing_type=sa.DATE(),
               nullable=True)
    op.drop_column('Show', 'venue_id')
    op.drop_column('Show', 'artist_id')
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###