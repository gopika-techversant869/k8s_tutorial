Docker fundamentals
----------------------------------
Before Docker we need to know about vm, Before VM we need to know physical server and how we deployed our apps in a server.

In the past, companies bought physical servers to deploy apps. Expensive, slow to set up, and hard to maintain.

![image](https://github.com/user-attachments/assets/20dfcc77-edb2-409d-ae49-84fa20f51b97)

How App Deployment Worked with Physical Servers
-----------------------------------------------------
You have a physical server — a real computer machine in your data center or office.

You install an operating system (like Linux or Windows) on it.

You install all your app dependencies (databases, runtimes, libraries).

You deploy your application directly on that physical server.

The app runs there, serving your users.

Why This Was Challenging
---------------------------------------------------------------------------
If you wanted to deploy multiple apps, you needed multiple physical servers (expensive!).

Setting up servers took time and effort.

Hardware failures meant downtime until fixed or replaced.

Scaling (adding more capacity) meant buying and installing new physical machines.

Here we implement the Virtual Machines
-----------------------------------------------------------------------------
A VM is a software emulation of a physical computer that runs an operating system and applications just like a real computer.

![image](https://github.com/user-attachments/assets/1a751a49-94c0-4c34-b93e-e19aca6f09eb)
