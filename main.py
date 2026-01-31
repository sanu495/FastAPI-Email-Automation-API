import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI, BackgroundTasks
from Utilities.send_email import send_email


app = FastAPI()

class User(BaseModel):
    name:str
    email:str

path_to_file = "templates/Photos/Logo-3.png"


@app.post("/Send_email")
async def send_email_one( user:User, background:BackgroundTasks):

    EmailGenerator = [user.email]
    Name = user.name.upper()
    
    body = {
    "title": "Hey", 
    "name": Name, 
    "message": "Thank you for choosing Cotazzac"
    }


    background.add_task(send_email, subject = f"Welcome to Cotzaac - Let's Get Started {Name}", 
                    email_to = EmailGenerator,
                    data = body,
                    file = path_to_file)
  
    return {"status": "Welcome Email Message sent successfully to", "name": Name, "email": user.email}


if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)