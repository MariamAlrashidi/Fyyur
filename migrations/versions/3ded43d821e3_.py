"""empty message

Revision ID: 3ded43d821e3
Revises: 
Create Date: 2020-05-15 07:56:49.862176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ded43d821e3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Show')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'shows')
    op.drop_column('Artist', 'website')
    op.drop_column('Venue', 'genres')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'shows')
    op.drop_column('Venue', 'website')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('shows', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('website', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('shows', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_table('Show',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_time', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id'], ['Artist.id'], name='artist_id'),
    sa.ForeignKeyConstraint(['id'], ['Venue.id'], name='venue_id'),
    sa.PrimaryKeyConstraint('id', name='Show_pkey')
    )
    # ### end Alembic commands ###
