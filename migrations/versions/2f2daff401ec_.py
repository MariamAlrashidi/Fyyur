"""empty message

Revision ID: 2f2daff401ec
Revises: 83282a4384e3
Create Date: 2020-05-21 10:19:44.598263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f2daff401ec'
down_revision = '83282a4384e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('date_created', sa.DateTime(), nullable=False))
    op.add_column('Artist', sa.Column('date_updated', sa.DateTime(), nullable=False))
    op.add_column('Artist', sa.Column('website', sa.String(), nullable=True))
    op.alter_column('Artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.drop_column('Artist', 'website_link')
    op.add_column('Show', sa.Column('date_created', sa.DateTime(), nullable=False))
    op.add_column('Show', sa.Column('date_updated', sa.DateTime(), nullable=False))
    op.alter_column('Show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('Show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_constraint('Show_venue_id_fkey', 'Show', type_='foreignkey')
    op.drop_constraint('Show_artist_id_fkey', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'], ondelete='CASCADE')
    op.add_column('Venue', sa.Column('date_created', sa.DateTime(), nullable=False))
    op.add_column('Venue', sa.Column('date_updated', sa.DateTime(), nullable=False))
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_column('Venue', 'date_updated')
    op.drop_column('Venue', 'date_created')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('Show_artist_id_fkey', 'Show', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key('Show_venue_id_fkey', 'Show', 'Venue', ['venue_id'], ['id'])
    op.alter_column('Show', 'venue_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('Show', 'artist_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('Show', 'date_updated')
    op.drop_column('Show', 'date_created')
    op.add_column('Artist', sa.Column('website_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.alter_column('Artist', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_column('Artist', 'website')
    op.drop_column('Artist', 'date_updated')
    op.drop_column('Artist', 'date_created')
    # ### end Alembic commands ###
