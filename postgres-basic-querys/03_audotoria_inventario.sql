--PELICULAS QUE ESTAN EN LA TABLA FILM PERO NO EN INVENTARIO

select 
film.film_id,
film.title as titulo
from film left join inventory on film.film_id = inventory.film_id
	where inventory.inventory_id is null
order by film.film_id asc;