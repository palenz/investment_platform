DROP TABLE investments;
DROP TABLE investors;
DROP TABLE companies;

CREATE TABLE investors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)    
);

CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    industry VARCHAR(255)
);

CREATE TABLE investments (
    id SERIAL PRIMARY KEY,
    investor_id INT REFERENCES investors(id) ON DELETE CASCADE,
    company_id INT REFERENCES companies(id) ON DELETE CASCADE,
    equity NUMERIC,
    payment INT,
    date_of_investment DATE
);