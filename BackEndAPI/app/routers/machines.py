import pika
import json
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.training_schema import StartTrainingRequest, StopTrainingRequest

router = APIRouter()

def send_message_to_broker(message: dict):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='training')
    channel.basic_publish(
        exchange='',
        routing_key='training',
        body=json.dumps(message)
    )
    connection.close()

@router.post("/start_training")
async def start_training(request: StartTrainingRequest):
    try:
        message = {
            "action": "start_training",
            "userid": str(request.userid),
            "trainingsetid": str(request.trainingsetid)
        }
        send_message_to_broker(message)
        return {"message": "Training started", "userid": request.userid, "trainingsetid": request.trainingsetid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/stop_training")
async def stop_training(request: StopTrainingRequest):
    try:
        message = {
            "action": "stop_training",
            "trainingid": str(request.trainingid)
        }
        send_message_to_broker(message)
        return {"message": "Training stopped", "trainingid": request.trainingid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status_training")
async def status_training():
    try:
        message = {"action": "status_training"}
        send_message_to_broker(message)
        return {"message": "Training status requested"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate")
async def generate():
    try:
        message = {"action": "generate"}
        send_message_to_broker(message)
        return {"message": "Generate requested"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))