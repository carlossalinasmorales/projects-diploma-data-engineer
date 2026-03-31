--DATOS CLIENTES QUE RENTARON EN 2005-05-24

select 
customer.first_name as nombre, 
customer.last_name as apellido, 
customer.email as correo, 
rental.rental_date as fecha
from customer inner join rental on customer.customer_id = rental.customer_id
	where cast(rental.rental_date as date) = '2005-05-24'
order by last_name asc;