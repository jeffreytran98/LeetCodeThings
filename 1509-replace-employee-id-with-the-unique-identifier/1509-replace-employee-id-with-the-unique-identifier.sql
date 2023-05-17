# Write your MySQL query statement below

#Select which columns you want
SELECT unique_id, name
#From which Table you want
FROM Employees
#Left JOIN - Returns ALL rows on Left (Employees.id) that match with Right (EmployeeUNI.id) w/ Null where unapplicable
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id