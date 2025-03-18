
SELECT department,job,
	   SUM(CASE WHEN quarter_num = 1 THEN count_employees ELSE 0 END) AS Q1,
	   SUM(CASE WHEN quarter_num = 2 THEN count_employees ELSE 0 END) AS Q2,
	   SUM(CASE WHEN quarter_num = 3 THEN count_employees ELSE 0 END) AS Q3,
	   SUM(CASE WHEN quarter_num = 4 THEN count_employees ELSE 0 END) AS Q4
FROM
( 
	SELECT D.department,J.job,QUARTER(HE.datetime) AS quarter_num,COUNT(HE.id) as count_employees
	FROM hired_employees as HE
	LEFT JOIN departments as D ON HE.department_id = D.id
	LEFT JOIN jobs as J ON HE.job_id = J.id
    WHERE YEAR(datetime) = 2021
	GROUP BY D.department,J.job,quarter_num
) base_query
GROUP BY department,job
-- We use ifnull to send the null values at the bottom of the order so the report is more appealing
ORDER BY ifnull(department,'zz') ASC,job ASC