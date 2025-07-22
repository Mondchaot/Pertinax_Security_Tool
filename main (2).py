from fastapi import FastAPI
from app.api import routes_monitor, routes_auth, routes_update

app = FastAPI(title="Pertinax Security API")

app.include_router(routes_monitor.router, prefix="/monitor")
app.include_router(routes_auth.router, prefix="/auth")
app.include_router(routes_update.router, prefix="/update")
if __name__ == '__main__':
    pass
