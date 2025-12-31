import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, BackgroundTasks
from Utilities.send_email import send_email


app = FastAPI()

class User(BaseModel):
    name:str
    email:str


@app.post("/Send_email")
async def send_email_one( user:User): 
   body = {"title":"Hey Good To See You","name":user.name}
   EmailGenerator = [user.email]
   await send_email(subject = "Welcome to Cotazzac - Let's Get Started", 
                    email_to = EmailGenerator,
                    data = body)
  
   return {"status":"success"}


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)