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

Working of VM
-------------------------------------------------------
- Hypervisor software runs on a physical server (host).

- It creates virtual hardware (CPU, memory, storage) for each VM.

- Each VM boots its own guest operating system using this virtual hardware.

- The hypervisor manages resource sharing and keeps VMs isolated from each other.

- Apps run inside the VM as if on a real computer.

But we have some demerits for using the VM
---------------------------------------------
- If we deploy an app directly to a VM (like an AWS EC2 instance), we need to:

- Manually install all the dependencies (Python, libraries, MySQL, etc.) on the VM.

- Set up the environment and configure everything ourselves.

Steps: Deploy App in a VM
--------------------------
1.Launch EC2 (Ubuntu, for example).
2.SSH into EC2.
3.Install runtime (e.g., Python, Node, etc.).
4.Install Git
5.Clone the repo
6.Run the app

This looks like:
------------------

![image](https://github.com/user-attachments/assets/c2fa7654-f56d-4dca-9348-04db9188b077)

To solve this we implement the containerization
------------------------------------------------

- We package the app and all its dependencies into a Docker image.

- We build and push the image to Docker Hub.

- Then we create an EC2 instance in AWS.

- On the EC2 VM, we install Docker (just once).

- We pull the image from Docker Hub and run it directly, without worrying about installing dependencies on the VM.
