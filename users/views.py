from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from users.forms import UserForm

# Create or Update User
def create_or_update_user(request, id=None):
    if id:
        user = get_object_or_404(User, id=id)
    else:
        user = None

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)

    return render(request, 'user_form.html', {'form': form})

# List Users
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

# Delete User
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')

    return render(request, 'user_confirm_delete.html', {'user': user})
