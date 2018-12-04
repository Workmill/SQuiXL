CREATE TABLE Options (
    id   INTEGER       PRIMARY KEY AUTOINCREMENT,
    name VARCHAR (255) 
);


CREATE TABLE Options_values (
    options_id INT           REFERENCES Options (ip),
    [key]      VARCHAR (255),
    value      VARCHAR (255),
    PRIMARY KEY (
        options_id,
        [key]
    )
);

CREATE VIEW view_options AS
    SELECT Options.id AS options_id,
           Options.name AS options_name,
           Options_values.[key] AS [key],
           Options_values.value AS value
      FROM Options
           INNER JOIN
           Options_values ON Options.id = Options_values.options_id;
