CREATE TABLE IF NOT EXISTS products (
	id SERIAL NOT NULL, 
	product_name VARCHAR(100) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (product_name)
);

CREATE TABLE IF NOT EXISTS categories (
	id SERIAL NOT NULL, 
	category_name VARCHAR(100) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (category_name)
);

CREATE TABLE IF NOT EXISTS product_category (
	id SERIAL NOT NULL, 
	product_id INTEGER, 
	category_id INTEGER, 
	PRIMARY KEY (id), 
	CONSTRAINT unique_product_category UNIQUE (product_id, category_id), 
	FOREIGN KEY(product_id) REFERENCES products (id), 
	FOREIGN KEY(category_id) REFERENCES categories (id)
);
