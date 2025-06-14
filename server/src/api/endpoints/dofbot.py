from fastapi import APIRouter, status, Depends
from api.dtos.dofbot import DofbotController as DofbotControllerDto
from api.endpoints.api_list import API_DOFBOT_CONTROLLER, API_DOFBOT_CONTROLLER_SET_NEWTRAL
from core.models.dofbot import DofbotControl
from core.models.config import Config
from frameworks.config.config_manager import ConfigManager
from usecases.dofbot.dofbot_controller import DofBotController as DofBotControllerService

router = APIRouter()

@router.post(API_DOFBOT_CONTROLLER)
def control_dofbot(dofbot: DofbotControllerDto, dofbot_controller: DofBotControllerService, config: Config = Depends(ConfigManager.get_config)):
    dofbot_control_params = DofbotControl(
        servo1=dofbot.servo1,
        servo2=dofbot.servo2,
        servo3=dofbot.servo3,
        servo4=dofbot.servo4,
        servo5=dofbot.servo5,
        servo6=dofbot.servo6
    )

    dofbot_controller.control_dofbot(dofbot_control_params, config)
    return {status.HTTP_200_OK: "DOFBOT controlled successfully"}


@router.get(API_DOFBOT_CONTROLLER_SET_NEWTRAL)
def set_newtral_position(dofbot_controller: DofBotControllerService):
    dofbot_controller.set_newtral_position()
    return {status.HTTP_200_OK: "DOFBOT set to newtral position successfully"}