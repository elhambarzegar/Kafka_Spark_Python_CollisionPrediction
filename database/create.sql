-- Database: postgres_pyspark

-- DROP DATABASE postgres_pyspark;

CREATE DATABASE postgres_pyspark
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	

-- Table: public.collisions

-- DROP TABLE public.collisions;

CREATE TABLE public.collisions
(
    "X" text COLLATE pg_catalog."default",
    "Y" text COLLATE pg_catalog."default",
    "INDEX_" text COLLATE pg_catalog."default",
    "ACCNUM" text COLLATE pg_catalog."default",
    "YEAR" text COLLATE pg_catalog."default",
    "DATE" text COLLATE pg_catalog."default",
    "TIME" text COLLATE pg_catalog."default",
    "HOUR" text COLLATE pg_catalog."default",
    "STREET1" text COLLATE pg_catalog."default",
    "STREET2" text COLLATE pg_catalog."default",
    "OFFSET" text COLLATE pg_catalog."default",
    "ROAD_CLASS" text COLLATE pg_catalog."default",
    "DISTRICT" text COLLATE pg_catalog."default",
    "WARDNUM" text COLLATE pg_catalog."default",
    "DIVISION" text COLLATE pg_catalog."default",
    "LATITUDE" text COLLATE pg_catalog."default",
    "LONGITUDE" text COLLATE pg_catalog."default",
    "LOCCOORD" text COLLATE pg_catalog."default",
    "ACCLOC" text COLLATE pg_catalog."default",
    "TRAFFCTL" text COLLATE pg_catalog."default",
    "VISIBILITY" text COLLATE pg_catalog."default",
    "LIGHT" text COLLATE pg_catalog."default",
    "RDSFCOND" text COLLATE pg_catalog."default",
    "ACCLASS" text COLLATE pg_catalog."default",
    "IMPACTYPE" text COLLATE pg_catalog."default",
    "INVTYPE" text COLLATE pg_catalog."default",
    "INJURY" text COLLATE pg_catalog."default",
    "FATAL_NO" text COLLATE pg_catalog."default",
    "INITDIR" text COLLATE pg_catalog."default",
    "VEHTYPE" text COLLATE pg_catalog."default",
    "MANOEUVER" text COLLATE pg_catalog."default",
    "DRIVACT" text COLLATE pg_catalog."default",
    "DRIVCOND" text COLLATE pg_catalog."default",
    "PEDTYPE" text COLLATE pg_catalog."default",
    "PEDACT" text COLLATE pg_catalog."default",
    "PEDCOND" text COLLATE pg_catalog."default",
    "CYCLISTYPE" text COLLATE pg_catalog."default",
    "CYCACT" text COLLATE pg_catalog."default",
    "CYCCOND" text COLLATE pg_catalog."default",
    "PEDESTRIAN" text COLLATE pg_catalog."default",
    "CYCLIST" text COLLATE pg_catalog."default",
    "AUTOMOBILE" text COLLATE pg_catalog."default",
    "MOTORCYCLE" text COLLATE pg_catalog."default",
    "TRUCK" text COLLATE pg_catalog."default",
    "TRSN_CITY_VEH" text COLLATE pg_catalog."default",
    "EMERG_VEH" text COLLATE pg_catalog."default",
    "PASSENGER" text COLLATE pg_catalog."default",
    "SPEEDING" text COLLATE pg_catalog."default",
    "AG_DRIV" text COLLATE pg_catalog."default",
    "REDLIGHT" text COLLATE pg_catalog."default",
    "ALCOHOL" text COLLATE pg_catalog."default",
    "DISABILITY" text COLLATE pg_catalog."default",
    "POLICE_DIVISION" text COLLATE pg_catalog."default",
    "HOOD_ID" text COLLATE pg_catalog."default",
    "NEIGHBOURHOOD" text COLLATE pg_catalog."default",
    "ObjectId" text COLLATE pg_catalog."default",
    "INVAGE" text COLLATE pg_catalog."default",
    create_at time with time zone,
    status text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.collisions
    OWNER to postgres;
	
	
	
-- Table: public.weather

-- DROP TABLE public.weather;

CREATE TABLE public.weather
(
    "Date" text COLLATE pg_catalog."default",
    "Time" text COLLATE pg_catalog."default",
    "Temp" text COLLATE pg_catalog."default",
    "Weather" text COLLATE pg_catalog."default",
    "Wind" text COLLATE pg_catalog."default",
    "Humidity" text COLLATE pg_catalog."default",
    "Visibility" text COLLATE pg_catalog."default",
    "Barometer" text COLLATE pg_catalog."default",
    create_at time with time zone,
    status text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE public.weather
    OWNER to postgres;