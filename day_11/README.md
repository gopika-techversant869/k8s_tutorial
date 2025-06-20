Communicate to the cluster
----------------------------

You can interact with the cluster in two ways:

![Untitled Diagram](https://github.com/user-attachments/assets/9d4921dc-3835-4af3-953e-434b05420586)


Imperative way 
----------------
The imperative approach involves directly telling Kubernetes to perform an action through kubectl commands.

When to Use Imperative:
-------------------------------

        - Quick debugging or troubleshooting.
        - One-time administrative tasks.
        - Experimentation and learning Kubernetes concepts.
        - Generating initial YAML templates


Declarative way
---------------------------
The declarative approach involves defining the desired state of your Kubernetes resources in configuration files (YAML or JSON, predominantly YAML) and then applying these files to the cluster.

When to use:
---------------------

          - Production deployments.
          - Managing complex applications with multiple components (Pods, Deployments, Services, ConfigMaps, Secrets, etc.).
          - Version controlling your infrastructure.
          - Implementing CI/CD pipelines.


For the learning purpose first we create the pod 
------------------------------------------------
In imperative way:
--------------------
