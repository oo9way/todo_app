from django.contrib import admin
from todo.models import Todo
import requests


def send_tasks_to_telegram(self, request, queryset):
    
    for todo in queryset:
        text = f"{todo.id}. {todo.name}\n"
        text += f"Description: {todo.description}\n"
        text += f"Status: {todo.status}"
        # send_msg_with_bot(text)
        TOKEN = "7221386127:AAGa7bBn421GJmIZcQZPoHDnGA-R2pdcs_I"
        CHAT_ID = 1921103181

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"

        requests.get(url)
    

# def send_msg_with_bot(text):

send_tasks_to_telegram.short_description = "Telegramga yuborish"
    



@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status")
    search_fields = ("name",)
    list_filter = ("status", )

    actions = (send_tasks_to_telegram, )