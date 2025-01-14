from fastapi import APIRouter, HTTPException
import pika

router = APIRouter()

def send_message_to_broker(message: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='training')
    channel.basic_publish(exchange='', routing_key='training', body=message)
    connection.close()

@router.post("/start_training")
async def start_training():
    try:
        send_message_to_broker("start training")
        return {"message": "Training started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/stop_training")
async def stop_training():
    try:
        send_message_to_broker("stop training")
        return {"message": "Training stopped"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status_training")
async def status_training():
    try:
        send_message_to_broker("status training")
        return {"message": "Training status requested"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate")
async def generate():
    try:
        send_message_to_broker("generate")
        return {"message": "Generate requested"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))