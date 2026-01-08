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
from supabase import create_client

db_url="https://tafdsjfjdppwfffkbtqy.supabase.co"
db_api="sb_publishable_sre0-TYPssYKIQeuJxjIWw_B6UE8b9_"
db=create_client(db_url,db_api)
app=FastAPI()
# contacts=[
#     {
#     "cont-id":1,
#     "name":"veera",
#     "phno":6281748974
#     },
#     {
#      "cont-id":2,
#      "name":"amar",
#      "phno":848977448
#     }   
#     ]

@app.post('/add/contact')
async def add_contacts(request :Request):
    data =  await request.json()
    result=  db.table('contact_table').insert(data).execute()
    return "sucess"

@app.get('/contact')
def get_all_contact_by_id(contact_id):
    result=  db.table('contact_table').select('*').eq('id',contact_id).execute()
    data = result.data
    return data
    
        
#  @app.get("/contact/{cont_id}")
# def get_contact_by_id(cont_id: int):
#     for c in contacts:
#         if c["cont"] == cont_id:
#             return c   

@app.get('/contacts')
def get_all_contacts():
    result=db.table('contact_table').select('*').execute()
    contacts=result.data
    return contacts
    

@app.put('/contact/{contact_id}')
async def update_contacts(request :Request,contact_id):
    data =  await request.json()
    result=  db.table('contact_table').update(data).eq('id',contact_id).execute()
    return "upadated sucessfully"
    
            
        
    
@app.delete('/contacts/{contacts_id}')
def delete_contacts(contacts_id):
    result=  db.table('contact_table').delete().eq('id',contacts_id).execute()
    return "deleted succesfully"
    