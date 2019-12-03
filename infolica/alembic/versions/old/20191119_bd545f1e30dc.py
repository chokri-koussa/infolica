"""init

Revision ID: bd545f1e30dc
Revises: 23699963ba13
Create Date: 2019-11-19 16:51:32.988773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd545f1e30dc'
down_revision = '23699963ba13'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cadastre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_cadastre')),
    schema='general'
    )
    op.create_table('operateur',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.Text(), nullable=False),
    sa.Column('prenom', sa.Text(), nullable=False),
    sa.Column('entree', sa.Date(), nullable=False),
    sa.Column('sortie', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_operateur')),
    schema='general'
    )
    op.create_table('plan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_plan')),
    schema='general'
    )
    op.drop_index('my_index', table_name='models')
    op.drop_table('models')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('value', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_models')
    )
    op.create_index('my_index', 'models', ['name'], unique=1)
    op.drop_table('plan', schema='general')
    op.drop_table('operateur', schema='general')
    op.drop_table('cadastre', schema='general')
    # ### end Alembic commands ###
