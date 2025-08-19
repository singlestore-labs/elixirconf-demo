# Elixirconf Demo

### 1. Set up environment

1. Create and active a Python virtual environment by running:

```sh
python3 -m venv ./.venv
source ./.venv/bin/activate
```

2. Create a `.env` file in the root of the project based on the `.env.example` file.
3. Install dependencies by running:

```sh
pip install -r requirements.txt
```

### 2. Create database

1. [Create a SingleStore database](https://portal.singlestore.com/intention/cloud?utm_source=yaroslav&utm_medium=github&utm_campaign=community-access&utm_content=elixirconf-demo)
2. Create tables by running:

```sh
python scripts/create_tables.py
```

### 3. Generate data

1. Generate data by running:

```sh
python scripts/generate_data.py
```

### 4. Load data

1. Load data into the database by running:

```sh
python scripts/load_data.py
```
