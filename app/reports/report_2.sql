
WITH avg_emp_hired as (
	
    SELECT AVG(count_employees) as avg_emp
    FROM
    (
		SELECT HE.department_id,COUNT(HE.id) as count_employees
		FROM hired_employees as HE
		WHERE YEAR(datetime) = 2021
		GROUP BY department_id
	) as base_query
)

SELECT D.id,D.department,COUNT(HE.id) as count_employees
FROM hired_employees as HE
LEFT JOIN departments as D ON HE.department_id = D.id
#we use cross join to repeat the avg in each row
CROSS JOIN avg_emp_hired as AEH
WHERE YEAR(datetime) = 2021 
GROUP BY D.id,D.department
#We use the max avg_emp to compare avg_emp with de aggregate of count in one step
HAVING count_employees > MAX(avg_emp)
ORDER BY 1 ASC