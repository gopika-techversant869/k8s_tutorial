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

Cheat sheets for kubernets commands
-----------------------------------

https://kubernetes.io/docs/reference/kubectl/quick-reference/


For the learning purpose first we create the pod 
------------------------------------------------
we already create the cluster : refer day_10

Here the node role is basically control plane but it act as both like control plane and worker node

Just you enter the following command:
                kubectl get nodes -o wide

You can see:
------------
               NAME          STATUS   ROLES           AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE       KERNEL-VERSION      CONTAINER-RUNTIME
        kind-control-plane   Ready    control-plane   5m    v1.28.0   172.18.0.2    <none>        Ubuntu 22.04   5.15.0-89-generic   containerd://1.6.20


In imperative way:
--------------------
**Note** : Here we create a pod for an nginx application:

1.Create the Pod in Imperative way(directly tell to the cluster)
----------------------------------------------------------------

                kubectl run your-pod-name --image image-name --port port-name
                
                (for eg : kubectl run nginx-pod --image nginx:latest --port 80)

output:
-----

                   pod/nginx-pod created

2.Check th status of the pod
-----------------------------------------
                 kubectl get pods

output:
-------

                NAME         READY   STATUS    RESTARTS   AGE
                nginx-pod    1/1     Running   0          92m
                nginx-pod1   1/1     Running   0          14m

3.Get more details about the pod:
--------------------------------------
Use the command:  

                kubectl describe pod your-pod-name 
                (for eg: kubectl descride pod nginx-pod)
output:
--------

                Name:             nginx-pod
                Namespace:        default
                Priority:         0
                Service Account:  default
                Node:             kind-control-plane/172.19.0.2
                Start Time:       Fri, 20 Jun 2025 08:47:21 +0530
                Labels:           run=nginx-pod
                Annotations:      <none>
                Status:           Running
                IP:               10.244.0.5
                IPs:
                  IP:  10.244.0.5
                Containers:
                  nginx-pod:
                    Container ID:   containerd://bd47e3346b9d0a19b890007451badfd282f04a40090012a13181c5af7ca91f2f
                    Image:          nginx:latest
                    Image ID:  your     docker.io/library/nginx@sha256:6784fb0834aa7dbbe12e3d7471e69c290df3e6ba810dc38b34ae33d3c1c05f7d
                    Port:           80/TCP
                    Host Port:      0/TCP
                    State:          Running
                      Started:      Fri, 20 Jun 2025 08:47:42 +0530
                    Ready:          True
                    Restart Count:  0
                    Environment:    <none>
                    Mounts:
                      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7pkkz (ro)
                Conditions:
                  Type                        Status
                  PodReadyToStartContainers   True 
                  Initialized                 True 
                  Ready                       True 
                  ContainersReady             True 
                  PodScheduled                True 
                Vyourolumes:
                  kube-api-access-7pkkz:
                    Type:                    Projected (a volume that contains injected data from multiple sources)
                    TokenExpirationSeconds:  3607
                    ConfigMapName:           kube-root-ca.crt
                    Optional:                false
                    DownwardAPI:             true
                QoS Class:                   BestEffort
                Node-Selectors:              <none>
                Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
                Events:                      <none>
                
4)Get the logs:
--------------------
Use the following 

                kubectl logs nginx-pod

5)To access the Nginx web page from our local browser for testing
-------------------------------------------------------------------
Open a new terminal window and run

                kubectl port-forward pod/your-pod-name hostport:pod port
                
                (For eg: kubectl port-forward pod/nginx-pod 8080:80)

                You need to run this in background : kubectl port-forward pod/ngnx-pod 8080:80 &
                
Then open your browser and go to  http://localhost:8080

output:
----------------

![Screenshot from 2025-06-20 10-56-28](https://github.com/user-attachments/assets/3ae8c708-4198-4bd0-a8b0-15d988aa0faf)


6)Delete the pod
---------------------------
Kubectl delete pod podname


How to create the pod in Declarative way
---------------------------------------------
1)Create the pod definition file like yaml or json
-------------------------------------------------------

   Open the terminal use nano command to create a yaml file

                           
                        apiVersion: v1
                        kind: Pod
                        metadata:
                          name: nginx-pod-declarative # Name of your pod
                          labels:
                            app: nginx-declarative      # Labels 
                        spec:
                          containers:
                          - name: nginx-container       # Name of the container within the Pod
                            image: nginx:latest         # The Docker image to use
                            ports:
                            - containerPort: 80         # The port the application inside the container listens on

2)Apply the yaml file to the cluster
----------------------------------------------

Use the command:

                kubectl apply -f file-name.yaml
                (eg: kubectl apply -f test.yaml)

**Then you find the status and test the application**



How to create a service for this pod for access publically
----------------------------------------------------------------------------


