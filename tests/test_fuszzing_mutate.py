import pytest
from endpoints.reg_adm_event import RegAdmEvent
import random
import string
import copy
import allure


def mutate_payload(payload):
    mutated_payload = copy.deepcopy(payload)
    for key in mutated_payload:
        if isinstance(mutated_payload[key], int):
            mutated_payload[key] = random.choice([-1, 0, 2 ** 31, random.randint(-100000, 100000)])
        elif isinstance(mutated_payload[key], str):
            mutated_payload[key] = ''.join(
                random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
        elif isinstance(mutated_payload[key], list):
            mutated_payload[key] = random.choice([[], None, [random.choice(range(1000))], mutated_payload[key] * 2])
        elif isinstance(mutated_payload[key], dict):
            mutated_payload[key] = mutate_payload(mutated_payload[key])
        elif mutated_payload[key] is None:
            mutated_payload[key] = random.choice([0, "", {}, []])
    return mutated_payload

@pytest.mark.parametrize("test_run", range(10))
def test_fuzzing_admin_event_regist(test_run):
    reg_adm_ev = RegAdmEvent()
    payload = reg_adm_ev.create_gen_payload()
    mutated_payload = mutate_payload(payload)
    reg_adm_ev.reg_adm_event(pay_load=mutated_payload)
    with allure.step("Mutated Payload"):
        allure.attach(str(mutated_payload), name="Mutated Payload", attachment_type=allure.attachment_type.JSON)
    if reg_adm_ev.response.status_code == 200:
        try:
            reg_adm_ev.assert_response_body()
        except AssertionError as e:
            with allure.step("Error during response validation"):
                allure.attach(str(e), name="AssertionError", attachment_type=allure.attachment_type.TEXT)
            with allure.step(f"Server returned error code: {reg_adm_ev.response.status_code}"):
                allure.attach(str(reg_adm_ev.response_json), name="Error Response",
                              attachment_type=allure.attachment_type.TEXT)
            raise
    elif reg_adm_ev.response.status_code in [400, 500]:
        with allure.step(f"Server returned error code: {reg_adm_ev.response.status_code}"):
            allure.attach(str(reg_adm_ev.response_json), name="Error Response",
                          attachment_type=allure.attachment_type.TEXT)
    else:
        pytest.fail(f"Unexpected status code: {reg_adm_ev.response.status_code}")