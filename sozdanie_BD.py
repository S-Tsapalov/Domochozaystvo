# cur.execute('''CREATE TABLE zadachi
# (id SERIAL PRIMARY KEY,
# name VARCHAR(255),
# start_data DATETIME,
# end_data DATETIME,
# opisanie TEXT,
# schetchik_perenosov INTEGER)''')
# conn.commit()

# cur.execute('''CREATE TABLE zadachi_na_den
# (id SERIAL PRIMARY KEY,
# id_del INTEGER,
# )''')
# conn.commit()

# cur.execute('''CREATE TABLE products
# (id SERIAL PRIMARY KEY,
# name_product VARCHAR(255),
# mera INTEGER)''')
# conn.commit()

# cur.execute('''CREATE TABLE mera_scheta #шт, гр, пачки
# (id SERIAL PRIMARY KEY,
# mera VARCHAR(15)''')
# conn.commit()

# cur.execute('''CREATE TABLE culinarnaya_kniga
# (id SERIAL PRIMARY KEY,
# recept TEXT,
# kkal INTEGER,
# products JSONB)''')

# conn.commit()

# cur.execute('''CREATE TABLE plan_pitaniya
# (
# id SERIAL PRIMARY KEY,
# date DATE,
# recept INTEGER,
# )''')
# conn.commit()

# cur.execute('''CREATE TABLE zapas_productov
# (id SERIAL PRIMARY KEY,
# product INTEGER,
# colichestvo INTEGER,
# )''')
# conn.commit()