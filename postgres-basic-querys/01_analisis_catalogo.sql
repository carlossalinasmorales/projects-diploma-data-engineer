--5 PELICULAS CON TARIFA ENTRE 3 Y 5 QUE CONTENGAN LA PALABRA ACTION EN SU DESCRIPCION

select title as titulo, description as descripcion, rental_rate as tarifa
from film
where description ilike '%action%'
	and rental_duration between 3 and 5
order by rental_rate desc
limit 5;