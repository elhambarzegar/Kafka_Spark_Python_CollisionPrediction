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