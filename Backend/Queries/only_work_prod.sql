-- (7) Name of the soldiers who have only work products
select SoldierId, sfName, slName
from "work_soldiers_equipment"
except
select SoldierId, sfName, slName
from "dwork-sol-equipment"
group by SoldierId, sfName, slName;