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

![Untitled Diagram](https://github.com/user-attachments/assets/c9cd4a21-43cf-466f-b62b-6bc1b8e6eacf)

If replication controller implemented
--------------------------------------------------

![image](https://github.com/user-attachments/assets/d2593e2f-944a-4c4a-9d2d-6175913754ed)


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


How can we scale up the RC?
---------------------------------

There are 2 main ways to scale up a ReplicationController:

1. Using kubectl scale command

            kubectl scale rc your-rc-name --replicas=5

            - This updates the RC's replica count from, say, 3 → 5
            
            -  Kubernetes will create 2 new pods with matching labels

 2. Edit YAML (declarative approach)

    If you created your RC from a YAML file, you can scale it by updating the replicas value.
                                    
                                   
    - Open your rc.yaml:
                                    

                                    apiVersion: v1
                                    kind: ReplicationController
                                    metadata:
                                      name: myapp-rc
                                    spec:
                                      replicas: 5   # Change this number
                                      selector:
                                        app: myapp
                                      template:
                                        metadata:
                                          labels:
                                            app: myapp
                                        spec:
                                          containers:
                                          - name: nginx
                                            image: nginx
    
    - Then apply the change:
                                    
                                   
                   kubectl apply -f rc.yaml

      

Limitations of replication controller
--------------------------------------------------
        - ReplicationControllers use only equality-based selectors.
        - They lack built-in rollback functionality.
        - They manage only a single Pod template.
        - There is no revision history tracking.

Selector
---------------
A selector is how Kubernetes matches Pods with a controller (like RC or ReplicaSet).

How the selector works:
-----------------------

                        selector:
                          app: nginx
                          
This means:

“Control all pods where the label app is exactly nginx.”

RC Cannot Do Flexible Matching
            Let’s say you have 3 types of pods:
            
            app: nginx
            
            app: apache
            
            app: node

You want to control only nginx and apache, not node.

With ReplicationController, this is not possible.

That means:
------------------
RC’s selector works like:

            selector:
              key1: value1
              key2: value2
Which means:

            Pod must have key1=value1 AND
            
            Pod must have key2=value2

So app: nginx AND app: apache is impossible, because a pod can’t have the same label key (app) with two different values.


To resolve these issue k8s implemented the ReplicaSet
-------------------------------------------------------------------


Replicaset
-----------------------
This is the direct successor to ReplicationController, primarily improving label selectors.


ReplicaSet supports:

 - Simple match (matchLabels)

 - Set-based match (matchExpressions)

1. Simple Selector (matchLabels)
   
This works exactly like in RC — only exact key=value match.


                        apiVersion: apps/v1
                        kind: ReplicaSet
                        metadata:
                          name: myapp-rs
                        spec:
                          replicas: 3
                          selector:
                            matchLabels:
                              app: nginx
                              tier: frontend
                          template:
                            metadata:
                              labels:
                                app: nginx
                                tier: frontend
                            spec:
                              containers:
                              - name: nginx
                                image: nginx
What it does:

Selects pods with:

            app=nginx
            
            tier=frontend

2. Set-Based Selector (matchExpressions)

Now you can use logic like:

            In / NotIn
            
            Exists / DoesNotExist

Example: Match nginx or apache

            selector:
              matchExpressions:
              - key: app
                operator: In
                values:
                  - nginx
                  - apache



 3. Example with multiple expressions

Example: Match only frontend nginx or apache pods in dev

            selector:
              matchExpressions:
              - key: app
                operator: In
                values: [nginx, apache]
              - key: tier
                operator: In
                values: [frontend]
              - key: env
                operator: In
                values: [dev]
Matches pods with:

            app=nginx or app=apache
            
            tier=frontend
            
            env=dev

Flexible control for managing complex environments


Look at the following exampe and scale this rs same as the rc.

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



Possible Issues or Considerations with ReplicaSet
----------------------------------------------------------------

1. Not use directly (Its not a good method)

you usually manage ReplicaSets through Deployments.

If you use a ReplicaSet directly (without a Deployment), you lose features like:

            Rolling updates
            
            Version history
            
            Rollbacks

**Best Practice**: Use Deployment → It internally creates and manages ReplicaSets for you.

2. Risk of Conflicting Label Selectors

If two ReplicaSets have overlapping selectors:

            - They might both try to adopt or control the same pod
            
            - This can lead to conflicts or unpredictable behavior

**Solution**: Use unique labels.


Deployment
-------------------
                        apiVersion: apps/v1
                        kind: Deployment
                        metadata:
                          name: nginx-deployment
                        spec:
                          replicas: 3
                          selector:
                            matchLabels:
                              app: nginx
                          template:
                            metadata:
                              labels:
                                app: nginx
                            spec:
                              containers:
                              - name: nginx
                                image: nginx:1.25
                                ports:
                                - containerPort: 80


![image](https://github.com/user-attachments/assets/dc0d98fa-51af-47d9-abf6-833f05108985)

