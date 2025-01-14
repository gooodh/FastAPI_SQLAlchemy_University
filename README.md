# FastAPI_SQLAlchemy_Temp
This project is a ready-made template for developing scalable web applications based on Facetapi with a full-fledged authentication and authorization system. The project includes a modular architecture, supports flexible logging with logo ru, and database interaction via SQLAlchemy with asynchronous support.
## The main structure of the project
```
├── app/
│   ├── auth/                   
│   │   ├── auth.py             
│   │   ├── dao.py              
│   │   ├── dependencies.py     
│   │   ├── models.py           
│   │   ├── router.py           
│   │   ├── schemas.py          
│   │   └── utils.py            
│   ├── dao/                    
│   │   └── base.py             
│   ├── migration/              
│   │   ├── versions/           
│   │   ├── env.py              
│   │   ├── README              
│   │   └── script.py.mako      
│   ├── static/                 
│   │   └── .gitkeep            
│   ├── config.py               
│   ├── database.py             
│   ├── exceptions.py           
│   ├── main.py                 
├── data/                       
│   └── db.sqlite3              
├── .env                        
├── .gitignore                  
├── alembic.ini                 
├── README.md                   
└── requirements.txt            
```
