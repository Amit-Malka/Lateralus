"""Shared Prisma client singleton.

Import `prisma` from this module anywhere in the app to ensure a single
database connection is reused across the entire process lifetime.
"""

from prisma import Prisma

prisma = Prisma()
