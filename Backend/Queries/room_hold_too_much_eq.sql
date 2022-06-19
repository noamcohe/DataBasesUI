-- (12) select each room that "hold" more bigger equipment than 1/4 of their size
select  rid, size, sum(area)
from "room-equipment"
group by rid, size
having sum(area) > size/4;