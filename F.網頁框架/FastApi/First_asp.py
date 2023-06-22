# 啟動方式:uvicorn First_asp:app --reload

from fastapi import FastAPI
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from datetime import date
from fastapi_scheduler import SchedulerAdmin
from sqlalchemy.ext.asyncio import create_async_engine
from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.requests import Request
from fastapi_amis_admin.amis.components import Form
from fastapi_amis_admin.admin import admin
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.crud.schema import BaseApiOut
from fastapi_amis_admin.models.fields import Field

app = FastAPI()

site = AdminSite(settings=Settings(database_url_async='sqlite+aiosqlite:///amisadmin.db'))

scheduler = SchedulerAdmin.bind(site)

@scheduler.scheduled_job('interval', seconds=60)
def interval_task_test():
    print('interval task is run...')

@scheduler.scheduled_job('cron', hour=3, minute=30)
def cron_task_test():
    print('cron task is run...')

@scheduler.scheduled_job('date', run_date=date(2022, 11, 11))
def date_task_test():
    print('date task is run...')

@site.register_admin
class UserLoginFormAdmin(admin.FormAdmin):
    page_schema = 'UserLoginForm'
    # set form information, optional
    form = Form(title='This is a test login form', submitText='login')

    # create form schema
    class schema(BaseModel):
        username: str = Field(..., title='username', min_length=3, max_length=30)
        password: str = Field(..., title='password')

    # handle form submission data
    async def handle(self, request: Request, data: BaseModel, **kwargs) -> BaseApiOut[Any]:
        if data.username == 'amisadmin' and data.password == 'amisadmin':
            return BaseApiOut(msg='Login successfully!', data={'token': 'xxxxxx'})
        return BaseApiOut(status=-1, msg='Incorrect username or password!')


@app.on_event("startup")
async def startup():
    # Mount the background management system
    site.mount_app(app)
    # Start the scheduled task scheduler
    scheduler.start()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
