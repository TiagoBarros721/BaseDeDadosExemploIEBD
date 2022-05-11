CREATE TABLE IF NOT EXISTS User (
    nome_de_utilizador TEXT,
    nome_da_conta TEXT,
    seguidores INTEGER,
    descricao TEXT,
    pais TEXT,
    loc_detalhes TEXT,
    data_nascimento TEXT
);
CREATE TABLE IF NOT EXISTS TipoPost (descricao TEXT, cor_do_texto TEXT);
CREATE TABLE IF NOT EXISTS Post (
    autor INTEGER texto TEXT,
    texto TEXT,
    tipo_de_post INTEGER
);