ReplicationController,Replicaset and deployment
-----------------------------------------------------
Create a multinode cluster
---------------------------
1.Create the yaml file or custom configuration file for creating the multinode cluster
---------------------------------------------------------------------------------------
            kind: Cluster
            apiVersion: kind.x-k8s.io/v1alpha4
            nodes:
              - role: control-plane
                image: kindest/node:v1.29.2
              - role: worker
                image: kindest/node:v1.29.2
              - role: worker
                image: kindest/node:v1.29.2

2.Create the cluster
-------------------------

            kind create cluster --config multi-node.yaml --name multicluster

Here You're telling Kind to use a custom configuration file (multi-node.yaml) that defines how the cluster should be built — including:

            - How many nodes (control-plane and workers)
            
            - What Kubernetes version (if specified)
            
            - Extra settings (like port mappings, volume mounts, etc.)

Why use a config?
----------------------
Without a config file, Kind just creates a single-node cluster by default:
But with a config file, you can:

         - Create multi-node clusters
          
         - Choose specific versions
          
         - Add port mappings (for local access)
          
         - Enable mount volumes, etc.


3.check the status
-----------------------------

kubectl get nodes

out:
-----
                    NAME                         STATUS   ROLES           AGE   VERSION
                    multicluster-control-plane   Ready    control-plane   90m   v1.29.2
                    multicluster-worker          Ready    <none>          89m   v1.29.2
                    multicluster-worker2         Ready    <none>          89m   v1.29.2
                    

4.Describe the nodes
---------------------------

    kubectl describe nodes



Replication controller
-------------------------------

Refer documentation: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/

1.First create the yaml file:
-------------------------

                  apiVersion: v1
                  kind: ReplicationController
                  metadata:
                    name: nginx
                  spec:
                    replicas: 3
                    selector:
                      app: nginx
                    template:
                      metadata:
                        name: nginx
                        labels:
                          app: nginx
                      spec:
                        containers:
                        - name: nginx
                          image: nginx
                          ports:
                          - containerPort: 80
                        
Here to find the apiversion and kind you can use this command - kubectl explain rc

Apply the file to the cluster
-----------------------------

      kubectl apply -f replication.yaml

Check the status of rc
---------------------------
        kubectl get rc


                NAME    DESIRED   CURRENT   READY   AGE
                nginx   3         3         3       82m


To describe the rc
---------------------

      kubectl describe rc


Output:
-----------
                          Name:         nginx
                          Namespace:    default
                          Selector:     app=nginx
                          Labels:       app=nginx
                          Annotations:  <none>
                          Replicas:     3 current / 3 desired
                          Pods Status:  3 Running / 0 Waiting / 0 Succeeded / 0 Failed
                          Pod Template:
                            Labels:  app=nginx
                            Containers:
                             nginx:
                              Image:         nginx
                              Port:          80/TCP
                              Host Port:     0/TCP
                              Environment:   <none>
                              Mounts:        <none>
                            Volumes:         <none>
                            Node-Selectors:  <none>
                            Tolerations:     <none>
                          Events:            <none>

Limitations of replication controller
--------------------------------------------------
        - ReplicationControllers use only equality-based selectors.
        - They lack built-in rollback functionality.
        - They manage only a single Pod template.
        - There is no revision history tracking.


Replicaset
-----------------------
This is the direct successor to ReplicationController, primarily improving label selectors.

create the yaml file:

apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: rs-simple
spec:
  replicas: 2
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: nginx
        image: nginx:1.25

Same as the apply to cluster, verify status and describe


Deployment
-------------------


