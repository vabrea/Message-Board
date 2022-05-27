

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Von",
    "Abrea",
    "Snowboarding"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jon",
    "Doe",
    "Tennis"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jane",
    "Thomas",
    "Painting"
);