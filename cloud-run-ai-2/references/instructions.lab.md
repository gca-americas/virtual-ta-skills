---
id: cloud-run-adk-bq-mcp
summary: Learn how to build and deploy AI Agents with Gemma 4 and BigQuery MCP server in Cloud Run
categories: Cloud Run, Gemma 4, GPU, ADK, BigQuery
tags: web
feedback_link: https://github.com/googlecodelabs/feedback/issues/new?title=[cloud-run-adk-bq-mcp]:&labels[]=content-platform&labels[]=cloud
analytics_account: UA-66226300-1
keywords: docType:Codelab,product:CloudRun

---

# Build and Deploy AI Agents with Gemma 4 and BigQuery MCP server in Cloud Run

[Codelab Feedback](https://github.com/googlecodelabs/feedback/issues/new?title=[cloud-run-adk-bq-mcp]:&labels[]=content-platform&labels[]=cloud)

## Introduction

> aside positive
>
> **Note:** This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA
features are available "as is" and might have limited support. For more information, [see the launch stage descriptions](https://cloud.google.com/products/#product-launch-stages)

### Overview

### What you'll learn

* How to deploy a Gemma 4 model on a [Cloud Run](https://cloud.google.com/run)
RTX 6000 Pro GPU with [vLLM](https://docs.vllm.ai/en/stable)
* How to create an AI Agent using
[Agent Development Kit (ADK)](https://adk.dev/) and use Gemma 4 with it.
* How to give AI Agents access to structured data in BigQuery using
[BigQuery MCP server](https://docs.cloud.google.com/bigquery/docs/use-bigquery-mcp).

**Gemma 4** is a family of Apache 2-licensed open weight models from Google
DeepMind. The models are multimodal, multilingual, offer reasoning, and an
efficient architecture.

**Cloud Run** is a serverless environment for containers with support for GPUs.

**Agent Development Kit (ADK)** is an open-source agent development framework that
lets you build, debug, and deploy reliable AI agents at enterprise scale.

**BigQuery** is a fully managed, serverless enterprise data warehouse
that allows you store, query, and analyze massive datasets.

**Model Context Protocol (MCP)** standardizes how large language models (LLMs)
and AI applications or agents connect to external data sources.
MCP servers let you use their tools, resources, and prompts to take actions
and get updated data from their backend service.
**BigQuery MCP Server** gives your AI agents a direct, secure
way to analyze data in BigQuery.
This fully managed MCP server removes management overhead,
enabling you to focus on developing intelligent agents.

> aside positive
>
> **Note:** This codelab uses the **Gemma 4 31B Instruction-Tuned** model.
The codelab demonstrates how to use Run:ai Model Streamer
and Direct VPC Egress minimize the time the model takes to load
from Cloud Storage during container startup.
For more information, visit the [GPU best practices guide](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices#loading-storing-models-tradeoff).

## Setup and Requirements

> aside positive
> This entire lab can be executed on the command line. You can use CloudShell
> (click the prompt icon at the top right of the console) to start the
> environment.

Start from setting default project and Cloud Run region:

```bash
# set the project
gcloud config set project <YOUR_PROJECT_ID>
```

Replace `<YOUR_PROJECT_ID>` with your Google Cloud Project Id.

```bash
# set Cloud Run region
gcloud config set run/region <CLOUD-RUN-REGION>
```
Replace `<CLOUD-RUN-REGION>` with one of the following Cloud regions:

* `us-central1`
* `asia-southeast1`

Here are environment variables that will be used throughout this codelab. You
can save these in an environment file and "source" it. Make sure to correctly
set the value of you project ID and optionally the region.

```bash
# Model name on HuggingFace Hub
export MODEL_NAME="google/gemma-4-31B-it"

# Cloud Run Service name
export SERVICE_NAME="gemma4-rtx-vllm-codelab"

# Cloud Project and Region for Cloud Run
export GOOGLE_CLOUD_PROJECT=$(gcloud config get project -q)
export GOOGLE_CLOUD_REGION=$(gcloud config get run/region -q)

# Service account for Cloud Run service
export SERVICE_ACCOUNT="vllm-service-sa"
export SERVICE_ACCOUNT_EMAIL="${SERVICE_ACCOUNT}@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com"

# GCS Bucket for the model cache.
export MODEL_CACHE_BUCKET="${GOOGLE_CLOUD_PROJECT}-${GOOGLE_CLOUD_REGION}-hf-model-cache"
# Model cache location in GSC bucket
export GCS_MODEL_LOCATION="gs://${MODEL_CACHE_BUCKET}/model-cache/${MODEL_NAME}"

# VPC Network for Direct VPC Egress
export VPC_NETWORK="vllm-${GOOGLE_CLOUD_REGION}-net"
export VPC_SUBNET="vllm-${GOOGLE_CLOUD_REGION}-subnet"
export SUBNET_RANGE="10.8.0.0/26"
```

> aside positive
>
> **Note:** It's useful to save this snippet as a script file
and re-use it in the future, in cases when Cloud Shell session is reset.
Save it as `env.sh` and run `source env.sh` to set the environment variables
when running subsequent steps.
**Do not commit `env.sh` to version control systems.**


Enable APIs needed for this Codelab.
API changes may take 2-3 minutes to take effect.

```bash
gcloud services enable --project "${GOOGLE_CLOUD_PROJECT}" \
    run.googleapis.com \
    cloudbuild.googleapis.com \
    artifactregistry.googleapis.com \
    iam.googleapis.com \
    compute.googleapis.com \
    vpcaccess.googleapis.com \
    storage.googleapis.com \
    bigquery.googleapis.com \
    aiplatform.googleapis.com
```

## Create Service Account

If you don't specify a service account when the Cloud Run service
or job is created, Cloud Run uses Compute Engine default service account.
A separate Service Account for Cloud Run service is recommended
to avoid running the service with excessive permissions.

### Create Service Account for Cloud Run service

```bash
gcloud iam service-accounts create ${SERVICE_ACCOUNT} \
  --project "${GOOGLE_CLOUD_PROJECT}" \
  --display-name "vLLM Service Account"
```

## Setup Cloud Storage

Create a Cloud Storage bucket to store the model weights.
This will allow using Direct VPC Egress for downloading model weights faster
every time Cloud Run starts a service instance.

Combined with Run:ai Model Streamer feature in vLLM,
it significantly reduces model loading time.

### Create a bucket

Make sure it's a single-region bucket co-located with Cloud Run service.

```bash
gcloud storage buckets create "gs://${MODEL_CACHE_BUCKET}" \
    --uniform-bucket-level-access --public-access-prevention \
    --project "${GOOGLE_CLOUD_PROJECT}" --location "${GOOGLE_CLOUD_REGION}"
```

## Retrieve and Cache Model Weights

Next, download the Gemma 4 model to your Cloud Storage bucket.
Models weights are dozens of gigabytes,
and downloading them to your local machine or Cloud Shell first
may be unfeasible.
Instead, use Cloud Build with enough storage to hold model weights.

### Copy Model Weights from a shared Cloud Storage Bucket

Google Cloud has a hosts a publicly accessible Cloud Storage Bucket
with Gemma 4 model weights.

To copy them to your storage bucket, run the command:

```bash
gcloud builds submit --project="${GOOGLE_CLOUD_PROJECT}" --region="${GOOGLE_CLOUD_REGION}" --no-source \
    --substitutions="_MODEL_NAME=${MODEL_NAME},_GCS_MODEL_LOCATION=${GCS_MODEL_LOCATION}" \
    --config=/dev/stdin <<'EOF'
steps:
- name: 'gcr.io/google.com/cloudsdktool/google-cloud-cli:slim'
  entrypoint: 'bash'
  args:
  - '-c'
  - |
    gcloud config set storage/parallel_composite_upload_enabled True
    gcloud config set storage/parallel_composite_upload_threshold 150M
    gcloud config set storage/sliced_object_download_threshold 150M
    MODEL_NAME="$_MODEL_NAME"
    SHORT_NAME="$${MODEL_NAME#*/}"
    gcloud storage cp -r -D "gs://vertex-model-garden-public-us/gemma4/$${SHORT_NAME}" "$_GCS_MODEL_LOCATION"
EOF
```

> aside negative
>
> **Note:** This operation takes significant time, from 10 to 30 minutes.

## Configure Networking for Direct VPC Egress

[Direct VPC Egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc)
configuration requires creating a network and subnet with
[Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access)
enabled.

This allows Cloud Run services to connect to the set of
external IP addresses used by Google APIs and services, including Cloud Storage.

### Create a Network

```bash
gcloud compute networks create "$VPC_NETWORK" \
        --subnet-mode=custom \
        --bgp-routing-mode=regional \
        --project "$GOOGLE_CLOUD_PROJECT"
```

### Create a Subnet

```bash
gcloud compute networks subnets create "$VPC_SUBNET" \
        --network="$VPC_NETWORK" \
        --region="$GOOGLE_CLOUD_REGION" \
        --range="$SUBNET_RANGE" \
        --enable-private-ip-google-access \
        --project "$GOOGLE_CLOUD_PROJECT"
```

## Configure Service Account Access Policy

Cloud Run Service Account needs permissions to access model weights in
the Storage Bucket you created.

```bash
gcloud storage buckets add-iam-policy-binding "gs://${MODEL_CACHE_BUCKET}" \
    --member "serviceAccount:${SERVICE_ACCOUNT_EMAIL}" \
    --role "roles/storage.admin" \
    --project "${GOOGLE_CLOUD_PROJECT}"
```

## Initialize Configuration Variables

Define the variables for both the vLLM inference engine and the Cloud Run service.

```bash
# vLLM variables
export MAX_MODEL_LEN="32767"    # 32767 to improve concurrency. Keep it empty to use model's maximim context length (256K)
export QUANTIZATION_TYPE="fp8"  # Model quantization for faster performance and lower memory usage.
export KV_CACHE_DTYPE="fp8"     # KV-cache quantization to save GPU memory.
export GPU_MEM_UTIL="0.95"      # Fraction of GPU memory to be used by the vLLM engine.
export TENSOR_PARALLEL_SIZE="1" # Partitioning model across GPUs (1 here as we have only 1 GPU).
export MAX_NUM_SEQS="16"         # Max concurrent requests vLLM processes in one batch.

# Cloud Run variables
export CLOUD_RUN_CPU_NUM=20
export CLOUD_RUN_MEMORY_GB=80
export CLOUD_RUN_MAX_INSTANCES=1
export CLOUD_RUN_CONCURRENCY=16
```

> aside positive
>
> **Note on Tuning for Performance:**
> Tuning these variables is a balance between throughput and latency:
> *   **`MAX_NUM_SEQS` vs `CLOUD_RUN_CONCURRENCY`**: `CLOUD_RUN_CONCURRENCY` should be at least as large as `MAX_NUM_SEQS`. For optimal utilization with traffic spikes, set it slightly higher (e.g., 2x).
> *   **Memory Pressure**: `MAX_MODEL_LEN` and `MAX_NUM_SEQS` both consume GPU memory for the KV cache. If you encounter Out-of-Memory (OOM) errors with large context lengths, consider reducing `MAX_NUM_SEQS`.
> *   **Latency**: Higher concurrency (`MAX_NUM_SEQS`) increases total throughput but can increase individual request latency.
> *   **Scaling**: `CLOUD_RUN_MAX_INSTANCES` allows you to scale horizontally. If your single-instance latency is acceptable but you need more total capacity, increase this value.

## Deploy to Cloud Run

### Prepare vLLM Container Command Line

vLLM requires plenty of parameters to run large models fast and efficiently.
These parameters will be passed as arguments to the container deployed to
Cloud Run.

```bash
CONTAINER_ARGS=(
    "vllm"
    "serve"
    "${GCS_MODEL_LOCATION}"
    "--served-model-name" "${MODEL_NAME}"
    "--enable-log-requests"
    "--enable-chunked-prefill"
    "--enable-prefix-caching"
    "--generation-config" "auto"
    "--enable-auto-tool-choice"
    "--tool-call-parser" "gemma4"
    "--reasoning-parser" "gemma4"
    "--dtype" "bfloat16"
    "--quantization" "${QUANTIZATION_TYPE}"
    "--kv-cache-dtype" "${KV_CACHE_DTYPE}"
    "--max-num-seqs" "${MAX_NUM_SEQS}"
    "--gpu-memory-utilization" "${GPU_MEM_UTIL}"
    "--tensor-parallel-size" "${TENSOR_PARALLEL_SIZE}"
    "--load-format" "runai_streamer"
    "--port" "8080"
    "--host" "0.0.0.0"
)

if [[ "${MAX_MODEL_LEN}" != "" ]]; then
    CONTAINER_ARGS+=("--max-model-len" "${MAX_MODEL_LEN}")
fi

export CONTAINER_ARGS_STR="${CONTAINER_ARGS[*]}"
```

### Deploy Cloud Run Service

Run the following command to deploy the Cloud Run service. Note the GPU type
(`RTX 6000 Pro`), the base image (`pytorch-vllm-serve:gemma4`), and the need
to be authenticated to invoke the service (`--no-allow-unauthenticated`).

```bash
gcloud beta run deploy "${SERVICE_NAME}" \
    --image="us-docker.pkg.dev/vertex-ai/vertex-vision-model-garden-dockers/pytorch-vllm-serve:gemma4" \
    --project "${GOOGLE_CLOUD_PROJECT}" \
    --region "${GOOGLE_CLOUD_REGION}" \
    --service-account "${SERVICE_ACCOUNT_EMAIL}" \
    --execution-environment gen2 \
    --no-allow-unauthenticated \
    --cpu="${CLOUD_RUN_CPU_NUM}" \
    --memory="${CLOUD_RUN_MEMORY_GB}Gi" \
    --gpu=1 \
    --gpu-type=nvidia-rtx-pro-6000 \
    --no-gpu-zonal-redundancy \
    --no-cpu-throttling \
    --max-instances ${CLOUD_RUN_MAX_INSTANCES} \
    --concurrency ${CLOUD_RUN_CONCURRENCY} \
    --network ${VPC_NETWORK} \
    --subnet ${VPC_SUBNET} \
    --vpc-egress all-traffic \
    --set-env-vars "MODEL_NAME=${MODEL_NAME}" \
    --set-env-vars "GOOGLE_CLOUD_PROJECT=${GOOGLE_CLOUD_PROJECT}" \
    --set-env-vars "GOOGLE_CLOUD_REGION=${GOOGLE_CLOUD_REGION}" \
    --port=8080 \
    --timeout=3600 \
    --cpu-boost \
    --startup-probe tcpSocket.port=8080,initialDelaySeconds=240,failureThreshold=40,timeoutSeconds=10,periodSeconds=15 \
    --command "bash" \
    --args="^;^-c;${CONTAINER_ARGS_STR}"
```

This will take a few minutes to deploy. Once done, you will have a GPU-powered
environment serving Gemma 4 using a serverless infrastructure with autoscaling
including scale to zero (no traffic, no cost).

> aside negative
>
> **Note:** If the service deployment fails with referring to GPU availability
or quota, skip testing the service,
and continue with **Create a Data Agent using Agent Development Kit**
section.
The agent can use Gemini 3.5 Flash Lite in Gemini Enterprise Agent Platform
if there is no Gemma 4 service to use.

## Test the Service

Once deployed, you can interact with your Gemma 4 model using
the vLLM OpenAI-compatible API.

### Get Service URL

Retrieve the URL of your deployed Cloud Run service.

```bash
SERVICE_URL=$(gcloud run services describe $SERVICE_NAME --project "${GOOGLE_CLOUD_PROJECT}" --region "${GOOGLE_CLOUD_REGION}" --format 'value(status.url)')
echo "Service URL: $SERVICE_URL"
```

### Run Inference

Send a prompt to the model using `curl`.

```bash
curl -s "$SERVICE_URL/v1/chat/completions" \
  -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "'"${MODEL_NAME}"'",
  "messages": [
    {"role": "user", "content": "Why is the sky blue?"}
  ],
  "chat_template_kwargs": {
    "enable_thinking": true
  },
  "skip_special_tokens": false
}' | jq -r '.choices[0].message.content'
```

## Create a Data Agent using Agent Development Kit

### Write agent's code

From Cloud Shell Terminal or your local terminal,
create a root directory for your agentic app:

```bash
mkdir data_agent
```

Open Cloud Shell Editor or another text editor,
and create `agent.py` in `data_agent` directory:

```none
data_agent/
    agent.py
```

**agent.py**

```python
import os
import subprocess

from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

import google.auth
from google.auth.transport.requests import Request
from google.oauth2 import id_token

# Fetch Application Default Credentials (ADC)
application_default_credentials, project_id = google.auth.default()
application_default_credentials.refresh(Request())

# Retrieve Google Cloud project to use.
project_id = os.getenv("GOOGLE_CLOUD_PROJECT", project_id)
if not project_id:
    raise ValueError("GOOGLE_CLOUD_PROJECT environment variable is not set.")

if os.getenv("GOOGLE_GENAI_USE_ENTERPRISE", "").lower() not in ["true", "1"]:
    # Using Cloud Run for hosting LLM with LiteLLM wrapper
    api_base = os.getenv(
        "API_BASE",
        os.environ.get("OPENAI_API_BASE", "")
    ).rstrip("/")
    if not api_base:
        raise ValueError("API_BASE environment variable is not set")
    if not api_base.endswith("/v1"):
        api_base += "/v1"

    model_name = os.getenv("MODEL_NAME")
    if not model_name:
        raise ValueError("MODEL_NAME environment variable is not set")
    # Format required by LiteLLM for OpenAI-compatible APIs
    model_name=f"openai/{model_name}"

    # To access the model's Cloud Run service,
    # we need an identity token.
    try:
        model_service_token_string = id_token.fetch_id_token(Request(), api_base)
    except Exception as e:
        # Fallback with using gcloud CLI to get the identity token
        model_service_token_string = subprocess.check_output(
            f"gcloud auth print-identity-token -q",
            shell=True
        ).decode().strip()

    # Gemma 4 in vLLM requires additional parameters in the request body.
    extra_body={
        "chat_template_kwargs": {
            "enable_thinking": True
        },
        "skip_special_tokens": False
    }
    # Configure the model with LiteLLM and an OpenAI-compatible endpoint
    custom_model = LiteLlm(
      model=model_name,
      base_url=api_base,
      api_key=model_service_token_string,
      extra_body=extra_body
    )
    model = custom_model
else:
    # Gemini API in Agent Platform fallback
    model = "gemini-3.5-flash-lite"

# Initialize the MCP Toolset with the connection parameters
bigquery_toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://bigquery.googleapis.com/mcp",
        headers={
            "Authorization": f"Bearer {application_default_credentials.token}",
            "x-goog-user-project": project_id, # This is used for billing
        },
        tool_filter=[
            'get_dataset_info',
            'list_table_ids',
            'get_table_info',
            # Using readonly is a security measure to prevent accidental data modification.
            'execute_sql_readonly',
        ]
    )
)

# Configure the agent

system_instruction = f"""
You are a helpful assistant that can answer questions about data in BigQuery.
To answer the user's question, use data you have access to by using tools `list_table_ids` and `get_table_info`.
Your data is in `bigquery-public-data.new_york_citibike` dataset
   (Citi Bike trips and stations in the NYC area.
    It includes trip records starting from September 2013 and is updated daily.)

Plan of action:
0. ALWAYS start by analyzing dataset.
1. Analyze your data, investigate schema and dimensions by querying distrinct values of columns using `execute_sql_readonly`.
   Output information about tables, columns, their data types and sets of values (for dimensions).
   Note which columns can be joined or used in aggregations/filters, and what type conversion may be needed for joining or aggregating.
   DO NOT MAKE ASSUMPTIONS ABOUT DATA (structure, type, values, relationships) BASED ON YOUR PRIOR KNOWLEDGE. ALWAYS VERIFY YOUR ASSUMPTIONS.
2. Understand and interpret the user's question.
3. Formulate a plan to answer the user's question.
4. Write a SQL query to retrieve relevant data in necessary form.
   This is where you must pay extra attention to column types and dimensions' sets of values.
5. Retrieve data by generating BigQuery SQL and using `execute_sql_readonly`.
   Always use Dry Run to verify SQL correctness.
   Use `{project_id}` to run BigQuery queries (`project_id` parameter of `execute_sql_readonly`).

Do not use LaTeX in your responses. When giving a final answer, use Markdown.
"""

root_agent = LlmAgent(
    model=model,
    name="data_agent",
    instruction=system_instruction,
    description="A helpful assistant that can answer questions using NYC Citibike data.",
    tools=[bigquery_toolset]
)
```

ADK also requires `__init__.py` and `requirements.txt` for deployment:

* `__init__.py` must have an import for the agent.
* `requirements.txt` list Python dependencies:
`google-adk` for Agent Development Kit, `litellm` for LiteLLM library
that ADK leverages for using non-Gemini models,
and `mcp` for Model Context Protocol client.

These commands help you create `__init__.py` and `requirements.txt`:

```bash
echo "from . import agent" > data_agent/__init__.py
echo -e "google-adk==2.4.*\nlitellm\nmcp==1.29.*" > data_agent/requirements.txt
```

The final folder structure should look like this:

```none
data_agent/
    __init__.py
    agent.py
    requirements.txt
```

### Try the agent locally

Agent Development Kit comes with `adk` CLI tool -
an interactive terminal interface for testing your agents.
This is useful for quick testing, scripted interactions, and CI/CD pipelines.
One of the features it provides is `adk web` -
[ADK Web Interface](https://adk.dev/runtime/web-interface/) -
a simple way to interactively develop and debug your agents.
ADK Web is not meant for use in production deployments,
but makes it very straightforward to try the agent.

> aside negative
>
> **Note:** Before running this command,
make sure your current directory has `data_agent` directory in it (with `ls` command).

This command launches `adk web` that starts a local web server on port 8080.

```bash
export API_BASE=$(gcloud run services describe $SERVICE_NAME \
  --project $GOOGLE_CLOUD_PROJECT \
  --region $GOOGLE_CLOUD_REGION \
  --format 'value(status.url)')

# If Gemma 4 deployment failed, use Gemini fallback
if [[ "${API_BASE}" == "" ]]; then
  export GOOGLE_GENAI_USE_ENTERPRISE=true
else
  export GOOGLE_GENAI_USE_ENTERPRISE=false
fi

uv tool run --with litellm,"mcp==1.29.*" --from "google-adk[mcp]==2.4.*" adk web --allow_origins="*" --port 8080 .
```

One the service started, open the local ADK Web page: http://localhost:8080/.

**If you are using Google Cloud Shell**, click Web Preview
![](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg)
button.

In the ADK Web UI, ask the agent about data it has access to:

```text
What data do you have?
```

> aside negative
>
> **Note:** First request to the agent may take a few minutes if
previously deployed Gemma 4 service is scaled down to zero by Cloud Run.
It takes about 3-4 minutes to start and load the model.

The agent code will use Gemma 4 model deployed to Cloud Run.
The model will use BigQuery MCP tools to explore the citibike dataset.
It will give you an overview of available tables and fields
in the Citibike dataset.

## Deploy the agent to Cloud Run

This command will deploy the agent to Cloud Run using ADK CLI.

```bash
export API_BASE=$(gcloud run services describe $SERVICE_NAME \
  --project $GOOGLE_CLOUD_PROJECT \
  --region $GOOGLE_CLOUD_REGION \
  --format 'value(status.url)')

# If Gemma 4 deployment failed, use Gemini fallback
if [[ "${API_BASE}" == "" ]]; then
  export GOOGLE_GENAI_USE_ENTERPRISE=true
else
  export GOOGLE_GENAI_USE_ENTERPRISE=false
fi

uv tool run --from google-adk==2.4.0 \
  adk deploy cloud_run \
      --with_ui \
      --project $GOOGLE_CLOUD_PROJECT \
      --region $GOOGLE_CLOUD_REGION \
      --service_name gemma4-data-agent \
      --app_name data_agent \
      data_agent \
      -- \
      --allow-unauthenticated \
      --max-instances 1 \
      --set-env-vars GOOGLE_GENAI_USE_ENTERPRISE=${GOOGLE_GENAI_USE_ENTERPRISE},MODEL_NAME="${MODEL_NAME}",API_BASE="${API_BASE}",GOOGLE_CLOUD_PROJECT="${GOOGLE_CLOUD_PROJECT}"
```

### Try the agent

We used `--with_ui` option for our agent deployment.
It deployed the agent with
[ADK Web Interface](https://adk.dev/runtime/web-interface/).

1. Open the agent URL in the web browser.
`adk deploy` command returned it, and you can also retrieve the URL by runninng
`gcloud run services` command:

```bash
gcloud run services describe gemma4-data-agent \
  --project $GOOGLE_CLOUD_PROJECT \
  --region $GOOGLE_CLOUD_REGION \
  --format 'value(status.url)'
```

2. Ask the agent to reason on the available Citibike data:

```text
We have budget for 3 coffee trucks.
We want to find the best city bike stations to place our coffee trucks.
```

The agent should explore Citibike dataset using BigQuery MCP server,
run a few SQL queries, and return a list of 3 citibike stations.

## Congratulations!

Congratulations for completing the codelab!

We recommend reviewing the [Cloud Run](https://cloud.google.com/run)
documentation.

#### What we've covered

* How to deploy Gemma 4 model on a Cloud Run RTX 6000 Pro GPU
* How to configure Direct VPC Egress and vLLM model streaming
with Cloud Storage for faster service startup.
* How to create and deploy an AI Agent with Agent Development Kit
that uses Gemma 4 LLM and BigQuery MCP server.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used
in this tutorial,
you can either delete the project or delete the individual resources.

### Option 1: Delete Resources

**Delete the Cloud Run Services**

```bash
gcloud run services delete gemma4-data-agent \
      --project "${GOOGLE_CLOUD_PROJECT}" \
      --region "${GOOGLE_CLOUD_REGION}" \
      --quiet
gcloud run services delete $SERVICE_NAME \
      --project "${GOOGLE_CLOUD_PROJECT}" \
      --region "${GOOGLE_CLOUD_REGION}" \
      --quiet
```

**Delete the Service Account**

```bash
gcloud iam service-accounts delete \
      ${SERVICE_ACCOUNT_EMAIL} \
      --project "${GOOGLE_CLOUD_PROJECT}" \
      --quiet
```

**Delete the Cloud Storage Bucket**

```bash
gcloud storage rm --recursive gs://$MODEL_CACHE_BUCKET
```

**Delete the VPC Network and Subnet**

```bash
gcloud compute networks subnets delete $VPC_SUBNET \
    --region "${GOOGLE_CLOUD_REGION}" \
    --project "${GOOGLE_CLOUD_PROJECT}" \
    --quiet

gcloud compute networks delete $VPC_NETWORK \
    --project "${GOOGLE_CLOUD_PROJECT}" \
    --quiet
```

### Option 2: Delete the Project

To delete the entire project, go to
[Manage Resources](https://console.cloud.google.com/cloud-resource-manager),
select the project you created in Step 2, and choose Delete. If you delete the
project, you'll need to change projects in your Cloud SDK. You can view the list
of all available projects by running `gcloud projects list`.
If you'd like to stick to the command line, you can also use this command:

```bash
gcloud projects delete ${GOOGLE_CLOUD_PROJECT}
```
