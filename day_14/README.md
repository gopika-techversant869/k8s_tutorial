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
              

