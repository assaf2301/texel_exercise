# texel_exercise

## Deployment Instructions
1. Trasnfer the 'nginx-texel-deployment' to your k8s master node
2. Create the Deployment by running the following command:
kubectl apply -f /path/to/nginx-texel-deployment.yaml

## Python tests
The code can run only on python3 
1. Enter the 'webserver_validator' dir.
2. Edit the settings.py file and enter the webserver IP.
3. Run the following command from your cli
python main.py
4. If the test fails, a relevant error will be thrown. 
