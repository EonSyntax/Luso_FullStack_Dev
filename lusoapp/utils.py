from django.contrib.auth import get_user_model

def create_admin_user():
    User = get_user_model()
    if not User.objects.filter(username="Admin@Luso").exists():
        User.objects.create_superuser("Admin@Luso", "lusointegrate@gmail.com", "Password@Luso")
        print("✅ Superuser Admin@Luso created.")
    else:
        print("ℹ️ Superuser Admin@Luso already exists.")