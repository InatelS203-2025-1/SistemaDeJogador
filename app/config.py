import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://PokedexPlayers_owner:npg_eAMtiHE83pgl@ep-wandering-math-a5s5qiwx-pooler.us-east-2.aws.neon.tech/PokedexPlayers?sslmode=require"
)
