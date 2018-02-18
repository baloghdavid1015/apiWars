
DROP TABLE IF EXISTS public.users;
CREATE TABLE users (
    user_id integer,
    user_name text NOT NULL,
    password text NOT NULL
);





INSERT INTO public.users VALUES (1, 'Alma', 'asdfadhfsadhgfa');
INSERT INTO public.users VALUES (2, 'Körte', 'ahdjgasdjhgads');
INSERT INTO public.users VALUES (3, 'Szilva', 'ashjdgajhdgas');
SELECT pg_catalog.setval('users_id_seq', 3, true);