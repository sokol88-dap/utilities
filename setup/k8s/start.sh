kubectl apply -f ./utility-namespace.yaml
kubectl create secret generic notify-secret --from-env-file .env --namespace=utility
kubectl apply -f ./db.yaml -n utility
kubectl apply -f ./job_notify.yaml -n utility