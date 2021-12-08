test_select = ('''
  SELECT *
  FROM public.staff;
''')

test_insert = ('''
  INSERT INTO public.test_table
  VALUES(%s);
''')

create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl1;
''')

create_table = ('''
    CREATE TABLE IF NOT EXISTS petl1.annual_ticket_sales (
        year TEXT PRIMARY KEY,
        tickets_sold TEXT NOT NULL,
        total_box_office TEXT NOT NULL,
        total_inflation_adjusted_box_office TEXT NOT NULL,
        average_ticket_price TEXT NOT NULL
    );
    
''')

create_table2 = ('''
    CREATE TABLE IF NOT EXISTS petl1.highest_grossers (
        year TEXT PRIMARY KEY,
        movie TEXT NOT NULL,
        genre TEXT NOT NULL,
        mpaa_rating TEXT NOT NULL,
        distributor TEXT NOT NULL,
        total_for_year TEXT NOT NULL,
        total_in_2019_dollars TEXT NOT NULL,
        tickets_sold TEXT NOT NULL
    );
''')

create_insert = ('''
    INSERT INTO petl1.annual_ticket_sales
    VALUES(%s, %s, %s, %s, %s);
''')

create_insert2 = ('''
    INSERT INTO petl1.highest_grossers
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
''')

create_table3 = ('''
    CREATE TABLE IF NOT EXISTS petl1.popular_creative_types (
        rank TEXT PRIMARY KEY,
        creative_types TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
''')

create_insert3 = ('''
    INSERT INTO petl1.popular_creative_types
    VALUES(%s, %s, %s, %s, %s, %s);
''')

create_table4 = ('''
    CREATE TABLE IF NOT EXISTS petl1.top_distributors (
        rank TEXT PRIMARY KEY,
        distributors TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
''')

create_insert4 = ('''
    INSERT INTO petl1.top_distributors
    VALUES(%s, %s, %s, %s, %s, %s);
''')

create_table5 = ('''
    CREATE TABLE IF NOT EXISTS petl1.top_genres (
        rank TEXT PRIMARY KEY,
        genres TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
''')

create_insert5 = ('''
    INSERT INTO petl1.top_genres
    VALUES(%s, %s, %s, %s, %s, %s);
''')

create_table6 = ('''
    CREATE TABLE IF NOT EXISTS petl1.top_grossing_ratings (
        rank TEXT PRIMARY KEY,
        mpaa_ratings TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
''')

create_insert6 = ('''
    INSERT INTO petl1.top_grossing_ratings
    VALUES(%s, %s, %s, %s, %s, %s);
''')

create_table7 = ('''
    CREATE TABLE IF NOT EXISTS petl1.top_grossing_sources (
        rank TEXT PRIMARY KEY,
        sources TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
''')

create_insert7 = ('''
    INSERT INTO petl1.top_grossing_sources
    VALUES(%s, %s, %s, %s, %s, %s);
''')

create_table8 = ('''
    CREATE TABLE IF NOT EXISTS petl1.top_production_methods (
        rank TEXT PRIMARY KEY,
        production_methods TEXT NOT NULL,
        movies TEXT NOT NULL,
        total_gross TEXT NOT NULL,
        average_gross TEXT NOT NULL,
        market_share TEXT NOT NULL
    );
''')

create_insert8 = ('''
    INSERT INTO petl1.top_production_methods
    VALUES(%s, %s, %s, %s, %s, %s);
''')

create_table9 = ('''
    CREATE TABLE IF NOT EXISTS petl1.wide_releases_count (
        year TEXT PRIMARY KEY,
        warner_bros TEXT NOT NULL,
        walt_disney TEXT NOT NULL,
        _20th_century_fox TEXT NOT NULL,
        paramount_pictures TEXT NOT NULL,
        sony_pictures TEXT NOT NULL,
        universal TEXT NOT NULL,
        total_major_6 TEXT NOT NULL,
        total_other_studios TEXT NOT NULL
    );
''')

create_insert9 = ('''
    INSERT INTO petl1.wide_releases_count
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
''')
