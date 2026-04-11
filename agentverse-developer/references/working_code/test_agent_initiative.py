from google.adk.evaluation.agent_evaluator import AgentEvaluator
from google.adk.evaluation.eval_set import EvalSet  
import pytest
import json

@pytest.mark.asyncio
async def test_agent_initiative():
    # Define the evaluation criteria
    evaluation_criteria = {
      "response_match_score": 0.0
    }

    # Define the path to your evalset file
    eval_set_filepath = "shadowblade/test.evalset.json"

    # 1. Read the JSON file into a dictionary
    with open(eval_set_filepath, 'r') as f:
        eval_set_data = json.load(f)

    # 2. Create an EvalSet object from the dictionary using the correct class
    eval_set_object = EvalSet(**eval_set_data)

    # 3. Call the evaluation method with the correctly typed object
    await AgentEvaluator.evaluate_eval_set(
        agent_module="shadowblade",
        eval_set=eval_set_object,
        criteria=evaluation_criteria,
        print_detailed_results=True,
    )