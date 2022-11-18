DROP DATABASE MOSSCHAT;
DROP USER 'MOSSUSER'@'localhost';


CREATE USER 'MOSSUSER'@'localhost' IDENTIFIED BY 'YxADUh64Hf_L';
CREATE DATABASE MOSSCHAT;
USE MOSSCHAT
GRANT ALL PRIVILEGES ON MOSSCHAT.* TO 'MOSSUSER'@'localhost';


CREATE TABLE USERS (
    USER_ID VARCHAR(255) PRIMARY KEY,
    USER_NAME VARCHAR(255) UNIQUE NOT NULL,
    EMAIL VARCHAR(255) UNIQUE NOT NULL,
    PASSWORD VARCHAR(255) NOT NULL
);

CREATE TABLE CHANNELS (
    CHANNEL_ID SERIAL PRIMARY KEY,
    USER_ID VARCHAR(255) REFERENCES USERS(USER_ID),
    CHANNEL_NAME VARCHAR(255) UNIQUE NOT NULL,
    ABSTRACT VARCHAR(255)
);

CREATE TABLE MESSAGES (
    MESSAGE_ID SERIAL PRIMARY KEY,
    USER_ID VARCHAR(255) REFERENCES USERS(USER_ID),
    CHANNEL_ID INTEGER REFERENCES CHANNELS(CHANNEL_ID) ON DELETE CASCADE,
    MESSAGE TEXT,
    CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);