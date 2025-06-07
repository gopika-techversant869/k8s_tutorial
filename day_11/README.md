# k8s_tutorial

Kubernets Archetecture
----------------------
Kubernetes architecture is, at its core, a distributed system. It automates the deployment, scaling, and management of containerised apps across multiple machines. This distributed nature lets Kubernetes handle large workloads. It maintains high resilience and efficiency.

![image](https://github.com/user-attachments/assets/28d7917d-bb5d-4f58-a39a-04ba772c4bea)


Components of Archetecture:

Api Server:
------------

client interact with the cluster using api server

![Apiserver](https://github.com/user-attachments/assets/9026eb2f-1b6c-4f19-b8b0-0e33f3474821)


Etcd:
-------
A distributed key-value store. It is Kubernetes' single source of truth, storing config data and state info.

![Untitled Diagram](https://github.com/user-attachments/assets/3fc0cfd7-69f8-49fe-a9cc-b961c5b0a5d8)

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



