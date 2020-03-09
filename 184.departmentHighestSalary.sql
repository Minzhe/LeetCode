SELECT s.Department, e.Name AS Employee, e.Salary
FROM (
    SELECT e.DepartmentId AS Id, 
        d.Name as Department, 
        MAX(e.Salary) AS Salary
    FROM Employee e
    JOIN Department d ON e.DepartmentId = d.Id
    GROUP BY e.DepartmentId
) s, Employee e
WHERE s.Id = e.DepartmentId AND s.Salary = e.Salary

