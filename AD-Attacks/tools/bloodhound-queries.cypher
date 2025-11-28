/*
bloodhound-queries.cypher
Basic safe queries for analyzing AD structure.
These do not show attack paths or offensive edges.
Author: (you)
*/

MATCH (u:User)
RETURN u.name AS User, u.enabled AS Enabled
ORDER BY User;

MATCH (c:Computer)
RETURN c.name AS Computer, c.operatingsystem AS OS
ORDER BY Computer;

MATCH (g:Group)
RETURN g.name AS Group, g.highvalue AS HighValue
ORDER BY Group;

MATCH (d:Domain)
RETURN d.name AS Domain, d.functionallevel AS FunctionalLevel;

