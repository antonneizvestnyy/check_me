-- поиск Медиану и средн значение

with t(time_all) as (
select
		age(resolved, started) as time_all
		from jira_custom_data.time_in_status2 as j
		inner join customfieldvalue as cf on cf.issue=j.id
		where cf.stringvalue  = '<ID_VALUE>' --значений несколько
		and j.status = '<STATUS_ISSUE>'
		and j.created >= '2022-01-01'::date 
		and j.resolved <= '2022-10-10'::date
		order by time_all asc)
select
PERCENTILE_CONT(0.5) WITHIN group (order by time_all) as median,
avg(time_all) as average_sum
from t
