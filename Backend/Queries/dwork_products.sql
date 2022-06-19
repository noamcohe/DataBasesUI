-- (8) Select a list of all the products that doesn't work
select E.Id,
       E.Name,
       E.worker
from Equipment E
where E.worker == FALSE
group by E.Id, E.Name, E.worker;