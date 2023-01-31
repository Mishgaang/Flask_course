"""Added new field

Revision ID: 5f34a9f7fb24
Revises: a3b7ad74be2c
Create Date: 2023-01-31 14:27:26.128575

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = '5f34a9f7fb25'
down_revision = '5f34a9f7fb24'
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()
    connection.execute(
        text(
            """
                UPDATE films
                SET test = 100
                WHERE title like '%Phoenix%'
            """
        )
    )


def downgrade():
    connection = op.get_bind()
    connection.execute(
        text(
            """
                UPDATE films
                SET test = NULL
                WHERE title like '%Phoenix%'
            """
        )
    )
