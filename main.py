# # from fastapi import FastAPI, Request
# # from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse    

# # app=FastAPI()

# # @app.get('/submit')

# # async def save_data(request :Request):
# #   data= await request.Body
# #   print(data)
  
 
# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse

# app = FastAPI()

# @app.post('/submit')  # Changed to POST
# async def save_data(request: Request):
#     data = await request.body()  # Correct method call
#     print(data)
#     return JSONResponse(content={"message": "Data received"})

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,JSONResponse,RedirectResponse

app=FastAPI()

contacts=[
    {
    "name":"veera",
    "phno":6281748974
    },
    {
     "name":"amar",
     "phno":848977448
    }   
    ]

@app.post('/add/contacts')
async def add_tasks(request :Request):
    data = request.json
    contacts.append(data)
    return contacts

@app.get('/contacts')
def get_all_tasks():
    return contacts
