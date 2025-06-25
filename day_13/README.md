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




