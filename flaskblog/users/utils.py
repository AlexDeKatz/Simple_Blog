import os
import secrets
from PIL import Image
from flask import url_for, current_app, flash, redirect
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, extention = os.path.split(form_picture.filename)
    picture_name = random_hex+extention
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_name)
    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)
    return picture_name


def send_reset_email(user):
    print("User: ", user)
    token = user.get_reset_token()
    msg = Message('Password reset Request',
                sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''Hi User,
    
    To reset your password, visit following link:
{url_for('users.reset_token',token=token,_external=True)}

If you did not make this request then simply ignore this email'''
    try:
        mail.send(msg)
    except:
        flash('Email could not be sent as this service is blocked', 'error')
        return redirect(url_for('users.reset_request'))
