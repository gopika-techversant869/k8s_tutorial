Namespaces in K8s
-----------------------

A namespace in Kubernetes is like a virtual cluster inside your actual cluster.

It’s a logical separation used to organize and manage resources like pods, services, deployments, etc.

        - Organize resources	
        - Avoid name conflicts	
        - Set resource limits	
        - Control access (RBAC)	
        - support	Let multiple apps/teams share the same cluster securely

For Example:
--------------------------

Let’s say you have two environments:

  - Production
  
  - Development

Instead of running everything in the same namespace (default), you create:

          kubectl create namespace prod
          kubectl create namespace dev
  
Now, you can deploy the same app in both:

          kubectl apply -f myapp.yaml -n prod
          kubectl apply -f myapp.yaml -n dev
          
Each one will have its own:

              - Pod
              
              - Service
              
              - Deployment
              
              - Logs


The same you just related to the real life example
--------------------------------------------------------
        - Kubernetes cluster is like a building.
        - Each namespace is like an apartment — separate and isolated.
        - Every apartment can have similar rooms (like kitchen, bedroom), just like namespaces can have resources (pods, services) with the same names.
        - There’s no conflict because everything is scoped within its own namespace.


You can list the namespaces in the cluster as:
---------------------------------------------------

                Kubectl get ns

Output like this
-----------------------

                NAME                 STATUS   AGE
                default              Active   7d9h
                kube-node-lease      Active   7d9h
                kube-public          Active   7d9h
                kube-system          Active   7d9h
                local-path-storage   Active   7d9h

These are the the default nmespces in the k8s.



You can describe the namespaces like:
--------------------------------------
                kubectl describe namespace default

out:
----------
                Name:         default
                Labels:       kubernetes.io/metadata.name=default
                Annotations:  <none>
                Status:       Active
                
                No resource quota.
                
                No LimitRange resource.

View All Resources in the Default Namespace:
--------------------------------------------------

                kubectl get all -n default


Note:**If we create any Kubernetes resource without specifying a namespace, it is automatically created in the default namespace.**

We have to create the namespace in two ways such as Imperative way and Declarative way
-----------------------------------------------------------------------------------------
In Imperative way:
---------------------

                kubectl create namespace my-namespace

In declarative way
------------------------------
Create a Yaml file 

                apiVersion: v1
                kind: Namespace
                metadata:
                  name: my-namespace
Then deploy this:

                kubectl apply -f yamlfile name

Creating resourses using namespaces like:
------------------------------------------

Create Using kubectl CLI with -n Option (Imperative)

You directly tell kubectl which namespace to use:

For creating a deployment:

                kubectl create deployment nginx-deploy --image=nginx -n namespace name
                
Or apply a YAML file:

                kubectl apply -f deployment.yaml -n dev

Or you can mention the namespace in the yaml file like:
                apiVersion: apps/v1
                kind: Deployment
                metadata:
                  name: nginx-deploy
                  namespace: dev   # 🔹 Set the namespace here
                spec:
                  replicas: 2
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
                        image: nginx
                        
Then apply this with kubectl
        
