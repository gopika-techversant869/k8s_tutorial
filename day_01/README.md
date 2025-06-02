# k8s_tutorial

Kubernets Archetecture
----------------------
Kubernetes architecture is, at its core, a distributed system. It automates the deployment, scaling, and management of containerised apps across multiple machines. This distributed nature lets Kubernetes handle large workloads. It maintains high resilience and efficiency.

![image](https://github.com/user-attachments/assets/28d7917d-bb5d-4f58-a39a-04ba772c4bea)


Components of Archetecture:

Api Server:
------------

client interact with the cluster using api server

![api server](https://github.com/user-attachments/assets/ffbb16f1-a84e-40a8-ae96-c5490b96da95)

Etcd:
-------
A distributed key-value store. It is Kubernetes' single source of truth, storing config data and state info.

Scheduler:
------------
