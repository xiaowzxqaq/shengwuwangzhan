CREATE TABLE question (
        type VARCHAR NOT NULL,
        id INTEGER NOT NULL,
        description VARCHAR,
        analysis VARCHAR,
        "choice_0" VARCHAR NOT NULL,
        "choice_1" VARCHAR NOT NULL,
        "choice_2" VARCHAR,
        "choice_3" VARCHAR,
        answer INTEGER NOT NULL,
        PRIMARY KEY (id, type)
);