# k8s_tutorial

Kubernets Archetecture
----------------------
Kubernetes architecture is, at its core, a distributed system. It automates the deployment, scaling, and management of containerised apps across multiple machines. This distributed nature lets Kubernetes handle large workloads. It maintains high resilience and efficiency.

![image](https://github.com/user-attachments/assets/28d7917d-bb5d-4f58-a39a-04ba772c4bea)



Cluster
------------------------

![pod](https://github.com/user-attachments/assets/1e91630a-b7f8-4333-aceb-3c67f8266f5a)




Components of Archetecture:

Api Server:
------------

client interact with the cluster using api server

![Apiserver](https://github.com/user-attachments/assets/9026eb2f-1b6c-4f19-b8b0-0e33f3474821)


Etcd:
-------
A distributed key-value store. It is Kubernetes' single source of truth, storing config data and state info.

![Untitled Diagram](https://github.com/user-attachments/assets/3fc0cfd7-69f8-49fe-a9cc-b961c5b0a5d8)



controller
------------------------

| Controller                 | What It Controls                               | Real Example                              |
| -------------------------- | ---------------------------------------------- | --------------------------------------------- |
| **Deployment Controller**  | Manages Deployment → Creates ReplicaSets       | You apply a Deployment YAML                   |
| **ReplicaSet Controller**  | Ensures correct number of Pods are running     | Creates 3 Pods if you asked for 3             |
| **Node Controller**        | Watches Nodes → Detects Node failures          | Marks Node `NotReady` if it misses heartbeats |
| **Job Controller**         | Manages Jobs → Runs a task to completion       | Used for batch/one-time tasks                 |
| **DaemonSet Controller**   | Ensures 1 Pod runs on *every* Node             | Useful for logging agents, node exporters     |
| **StatefulSet Controller** | Manages Pods with stable identity              | Useful for databases, Zookeeper, etc.         |
| **Service Controller**     | Creates cloud load balancers (if cloud-native) | Exposes your app to external traffic          |

For example:
Node controller:
-------------------
![controller (1)](https://github.com/user-attachments/assets/cbd3fd5d-0ba2-448f-bb6c-102a06a8635d)

Deployement controller:
-----------------------------
![pod (1)](https://github.com/user-attachments/assets/264b4168-1941-4bce-bcb3-5fc1a14eed96)


Job controller
-----------------------------
Run a one-time task to completion like a script.

![replicaset](https://github.com/user-attachments/assets/188c00a0-de78-4608-acf0-3e43fd43ad86)

Service controller
-------------------------

![Editor _ Mermaid Chart-2025-06-19-085416](https://github.com/user-attachments/assets/42529f61-b2ef-4782-9066-0e83578f4602)


Scheduler:
------------
Assign the best node.

Kubelet:
---------------
Kubelet manages containers on each node and receives instructions from the Kubernetes API server to ensure Pods run correctly.

![kubelet](https://github.com/user-attachments/assets/618f0809-6627-4002-ab74-933e94c2d5e3)

Kube proxy:
-----------
Used for pods to pod communication

![kubelet](https://github.com/user-attachments/assets/ca13c39e-6164-4adc-9015-eae0b55cb646)



