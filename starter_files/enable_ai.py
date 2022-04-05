from statistics import mode
from azureml.core import Workspace
from azureml.core.webservice import Webservice
ws = Workspace.from_config()

name = "best-automl-model"
print(f"Enabling app insights for {name}")
model_service = Webservice(ws, name)
model_service.update(enable_app_insights=True)