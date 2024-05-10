# Classification API

```bash
conda create -n classification_api python=3.12
conda activate classification_api
pip install -r requirements.txt
python download_models.py
```

# Build
```bash
docker image build -t classification_api .
docker save -o classification_api.tar classification_api
```

# Run

```bash
docker load -i classification_api.tar
docker run -p 5002:5002 classification_api
```
