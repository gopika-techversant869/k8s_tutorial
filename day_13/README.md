K8s Services
---------------------
In Kubernetes, a Service is a fundamental concept that provides a stable network endpoint for a set of Pods. It acts as an abstraction layer, allowing other applications or external clients to reliably access your applications running in Pods, even as those Pods are created, destroyed, and have their IP addresses changed.

Why we implemented the service
--------------------------------
Without a service
----------------

![serv (1)](https://github.com/user-attachments/assets/27931270-862e-43d4-8350-573cc6a17cc4)


In Kubernetes:

A Pod is the smallest deployable unit — it runs your app/container.

Pods are temporary:

        - They can be restarted if they crash.
        
        - They can be replaced when you scale up/down.
        
        - Each new Pod gets a new IP address.
        
So you can’t rely on the Pod’s IP staying the same.

With service
-----------------

![serv (2)](https://github.com/user-attachments/assets/9f8cf78f-c106-473a-90fb-d0ac734a6e97)

A Service:

        - Selects Pods using a label (like app=my-app).
        
        - Watches the list of matching Pods (even when they change).
        
        - Provides a fixed IP address and a DNS name like:

                    - IP: 10.96.0.1
                    
                    - DNS: my-service.default.svc.cluster.local

So the client doesn’t need to worry about which Pod or IP — it just calls the Service.

Types of Services in K8s
-------------------------

![s](https://github.com/user-attachments/assets/7883e9c1-de80-4e09-b080-331869dd376c)



1.ClusterIP
----------------

-Default type

-Exposes the Service internally within the cluster

-Cannot be accessed from outside

![image](https://github.com/user-attachments/assets/5857fffe-2ce3-465a-998e-7ab8ed66e170)

How to create and test clusterIp service
---------------------------------------------

1.Here we have to create a deployment.yaml file 

                apiVersion: apps/v1
                kind: Deployment
                metadata:
                  name: backend
                spec:
                  replicas: 1
                  selector:
                    matchLabels:
                      app: backend
                  template:
                    metadata:
                      labels:
                        app: backend
                    spec:
                      containers:
                        - name: backend
                          image: nginx
                          ports:
                            - containerPort: 80

2.Apply the deployment to the cluster

                kubectl apply -f deployement.yaml

3.Create the clusterIp service: cluster-service.yaml

                apiVersion: v1
                kind: Service
                metadata:
                  name: backend-service
                spec:
                  selector:
                    app: backend
                  ports:
                    - port: 80
                      targetPort: 80
                  type: ClusterIP

        
        In the selector we provide the label of the pods that we created in the deployment.
        

4.Apply the cluster manifetst to the cluster

                kubectl apply -f service.yaml

5.Verify the service status

                kubectl get svc backend-service

        then you get the following:

                NAME              TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
                backend-service   ClusterIP   10.96.130.94   <none>        80/TCP    106m


6.Create a test pod to access the service

        
        kubectl run test-client --rm -it --image=busybox --restart=Never -- sh

                | Part              | Meaning                                                |
                | ----------------- | ------------------------------------------------------ |
                | `kubectl run`     | Run a quick pod                                        |
                | `test-client`     | Name of the pod                                        |
                | `--rm`            | Automatically delete it after you're done              |
                | `-it`             | Interactive terminal (so you can type commands inside) |
                | `--image=busybox` | Use a tiny Linux container with basic tools            |
                | `--restart=Never` | Just a one-time pod (not a deployment)                 |
                | `-- sh`           | Start a shell inside the pod                           |



7.Test the service inside the shell

        wget -qO- http://service-name 

        For example: wget -qO- http://backend-service

        Then you get like this:

                                <!DOCTYPE html>
                                <html>
                                <head>
                                <title>Welcome to nginx!</title>
                                <style>
                                html { color-scheme: light dark; }
                                body { width: 35em; margin: 0 auto;
                                font-family: Tahoma, Verdana, Arial, sans-serif; }
                                </style>
                                </head>
                                <body>
                                <h1>Welcome to nginx!</h1>
                                <p>If you see this page, the nginx web server is successfully installed and
                                working. Further configuration is required.</p>
                                
                                <p>For online documentation and support please refer to
                                <a href="http://nginx.org/">nginx.org</a>.<br/>
                                Commercial support is available at
                                <a href="http://nginx.com/">nginx.com</a>.</p>
                                
                                <p><em>Thank you for using nginx.</em></p>
                                </body>
                                </html>



List all serives in the k8s
---------------------------
        kubectl get svc -A

        NAMESPACE     NAME              TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)                  AGE
        default       backend-service   ClusterIP   10.96.130.94   <none>        80/TCP                   131m
        default       kubernetes        ClusterIP   10.96.0.1      <none>        443/TCP                  2d20h
        kube-system   kube-dns          ClusterIP   10.96.0.10     <none>        53/UDP,53/TCP,9153/TCP   2d20h


2.NodePort
----------------------
A NodePort is one of the Kubernetes Service types that allows external access to your app running inside the cluster.

It exposes your app on a static port (30000–32767) on each worker node's IP address, making it accessible from outside the cluster

Here we create the cluster like this because we use kind cluster

                kind: Cluster
                apiVersion: kind.x-k8s.io/v1alpha4
                nodes:
                  - role: control-plane
                    extraPortMappings:
                      - containerPort: 30080
                        hostPort: 30080
                        protocol: TCP
                  - role: worker

That means:

        - Each Kubernetes node is a Docker container.
        
        - So, you can’t directly access NodePorts (like localhost:30080) unless you explicitly forward ports from your host to the container.
       
        - NodePort opens ports on the Kubernetes node (Docker container).

        - But you’re running curl http://localhost:30080 from your host machine, not from inside the container.
        
        - Without port forwarding (extraPortMappings), that traffic won’t reach the container.











