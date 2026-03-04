# Document your edge case here
- To get marks for this section you will need to explain to your tutor:
1) The edge case you identified

One edge case would be if two student had the same name. Currently, we do not show a unqiue identifier attached to a student on the FE.
Therefore, we can just show it so the user can tell the difference between students with the same name.

2) How you have accounted for this in your implementation

On the FE, I have added a spot for the ID to be seen. This could be something like a zID in the future. <td>{s.id}</td>
