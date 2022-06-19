-- (10) select a list of all building,
-- and the cost of the equipment that the soldiers who live in this building are lent
-- (for the building safety)
select bid, sum (cost)
from "building-equipment"
group by bid;